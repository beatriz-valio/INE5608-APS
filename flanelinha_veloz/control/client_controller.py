import datetime
import hashlib
from datetime import datetime as dt

from flanelinha_veloz.control.menu_controller import MenuController
from flanelinha_veloz.entity.agendamento import Agendamento
from flanelinha_veloz.entity.cliente import Cliente
from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.entity.servico import Servico
from flanelinha_veloz.entity.vaga import Vaga
from flanelinha_veloz.entity.veiculo import Veiculo
from flanelinha_veloz.exceptions.cpfNotValidException import \
    CPFNotValidException
from flanelinha_veloz.exceptions.emailDoesntMatchException import \
    EmailDoesntMatchException
from flanelinha_veloz.exceptions.emailNotValidException import \
    EmailNotValidException
from flanelinha_veloz.exceptions.establishmentUnavailableTimeSchedule import EstablishmentUnavailableTimeSchedule
from flanelinha_veloz.exceptions.funcionarioNotAvailableException import \
    FuncionarioNotAvailableException
from flanelinha_veloz.exceptions.missingDataException import \
    MissingDataException
from flanelinha_veloz.exceptions.passwordDoesntMatchException import \
    PasswordDoesntMatchException
from flanelinha_veloz.exceptions.spotCarLimitReachedException import \
    SpotCarLimitReachedException
from flanelinha_veloz.exceptions.userAlreadyExistException import \
    UserAlreadyExistException
from flanelinha_veloz.persistence.clienteDAO import ClienteDAO
from flanelinha_veloz.persistence.employeesDAO import EmployeesDAO
from flanelinha_veloz.persistence.establishmentOperationDAO import \
    EstablishmentOperationDAO
from flanelinha_veloz.persistence.scheduleDAO import ScheduleDAO
from flanelinha_veloz.persistence.typesOfServicesDAO import TypesOfServicesDAO
from flanelinha_veloz.persistence.vehicleTypesDAO import VehicleTypesDAO
from flanelinha_veloz.view.client_boundary import ClientBoundary


class ClientController:
    def __init__(self, system_controller):
        self.__client_screen = ClientBoundary()
        self.__client_dao = ClienteDAO()
        self.__employee_dao = EmployeesDAO()
        self.__system_controller = system_controller
        self.__types_of_services_dao = TypesOfServicesDAO()
        self.__vehicle_types_dao = VehicleTypesDAO()
        self.__schedule_dao = ScheduleDAO()
        self.__establishment = EstablishmentOperationDAO().get()
        self.__menu = MenuController(system_controller)

    @property
    def client_dao(self):
        return self.__client_dao

    def search_client(self, cpf: int):
        try:
            return self.__client_dao.get(cpf)
        except KeyError:
            self.__client_screen.show_message('Nenhum cliente encontrado!')

    def open_update_screen(self):
        while True:
            try:
                logged_user = self.__system_controller.logged_user
                if logged_user:
                    client_values = self.__client_screen.open_update_screen(
                        logged_user)
                    old_password = logged_user.senha
                    action = client_values['action']
                    if action == ClientBoundary.UPDATE:
                        client_return = client_values['client']
                        del (client_return['Calendário'])
                        self.check_if_is_complete(client_return)
                        cpf = logged_user.cpf
                        email = client_return['email']
                        c_email = client_return['c-email']
                        if email != c_email:
                            raise EmailDoesntMatchException
                        else:
                            password = client_return['password']
                            c_password = client_return['c-password']
                            if password != c_password:
                                raise PasswordDoesntMatchException
                            else:
                                if password != old_password:
                                    password = password.encode('utf-8',
                                                               'ignore')
                                    password = hashlib.md5(password)
                                    password = password.hexdigest()
                                birth_date = dt.strptime(
                                    client_return['birth_date'], "%d/%m/%Y")
                                gender = client_return['gender']
                                name = client_return['name']
                                last_name = client_return['last_name']
                                client = Cliente(cpf, birth_date, email,
                                                 gender, name, password,
                                                 last_name)
                                self.__client_dao.remove(logged_user.cpf)
                                self.client_registration(client)
                    elif action == ClientBoundary.DELETE:
                        cpf = logged_user.cpf
                        self.delete_client(cpf)
                        self.__system_controller.open_login_screen()
                    elif action is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except ValueError:
                self.__client_screen.show_message(
                    'Digite os valores corretos!', 'red')
            except Exception as e:
                self.__client_screen.show_message(str(e))

    def delete_client(self, cpf: int):
        try:
            if self.check_if_already_exist(cpf):
                self.__system_controller.set_logged_user(None)
                self.__client_dao.remove(cpf)
                self.__client_screen.show_message(
                    'Usuário deletado com sucesso!')
        except KeyError:
            self.__client_screen.show_message(
                'Não foi possível deletar o usuário!')

    def check_if_already_exist(self, cpf: int):
        return self.__client_dao.get(cpf)

    def check_if_is_complete(self, data):
        for value in data:
            if data[value] is None or data[value] == '':
                raise MissingDataException

    def open_create_screen(self):
        while True:
            try:
                client_values = self.__client_screen.open_screen()
                action = client_values['action']
                if action == ClientBoundary.CREATE:
                    client_return = client_values['client']
                    del (client_return['Calendário'])
                    self.check_if_is_complete(client_return)
                    cpf = int(client_return['cpf'])
                    if self.check_if_already_exist(cpf):
                        raise UserAlreadyExistException
                    else:
                        if not self.__system_controller.validate_cpf(str(cpf)):
                            raise CPFNotValidException
                        else:
                            email = client_return['email']
                            c_email = client_return['c-email']
                            if email != c_email:
                                raise EmailDoesntMatchException
                            else:
                                if not self.__system_controller.validate_email(
                                        email):
                                    raise EmailNotValidException
                                else:
                                    password = client_return['password']
                                    c_password = client_return['c-password']
                                    if password != c_password:
                                        raise PasswordDoesntMatchException
                                    else:
                                        password = password.encode('utf-8',
                                                                   'ignore')
                                        password = hashlib.md5(password)
                                        password = password.hexdigest()
                                        birth_date = dt.strptime(
                                            client_return['birth_date'],
                                            "%d/%m/%Y")
                                        gender = client_return['gender']
                                        name = client_return['name']
                                        last_name = client_return['last_name']
                                        client = Cliente(cpf, birth_date,
                                                         email, gender, name,
                                                         password, last_name)
                                        self.client_registration(client)
                elif action is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__client_screen.show_message(
                    'Digite os valores corretos!', 'red')
            except Exception as e:
                self.__client_screen.show_message(str(e))

    def client_registration(self, client):
        if isinstance(client,
                      Cliente) and client is not None and client not in self.__client_dao.get_all():
            self.__client_dao.add(client)
            self.__system_controller.set_logged_user(client)
            self.__client_screen.show_message('Ação realizada com sucesso!',
                                              'green')
        else:
            self.__client_screen.show_message('Dados incorretos!', 'red')

    def open_menu_client(self):
        try:
            while True:
                option = self.__client_screen.profile_screen(
                    self.__system_controller.logged_user)
                if option == ClientBoundary.UPDATE:
                    self.__client_screen.open_update_screen(self.__system_controller.logged_user)
                elif option is None:
                    self.__system_controller.shutdown()
                else:
                    break

        except Exception as e:
            self.__client_screen.show_message(str(e))

    def open_schedule_confirmation_screen(self, values):
        try:
            selected_vehicle_type = self.__system_controller \
                .vehicle_types_controller \
                .search_for_vehicle_types_by_name(
                values['vehicle_type'])
            selected_service_type = self.__system_controller \
                .types_of_services_controller \
                .search_for_types_of_service_by_name(
                values['service_type'])

            total_time: datetime.timedelta = self.__return_total_time(
                selected_vehicle_type,
                selected_service_type)
            total_price = self.__return_total_price(selected_vehicle_type,
                                                    selected_service_type)

            confirmation_values = self.__client_screen \
                .open_schedule_confirmation_screen(total_time,
                                                   total_price)

            action = confirmation_values['action']
            if action == ClientBoundary.SCHEDULE:
                employee = self.__system_controller.employees_controller.next_employee()
                if employee:
                    t = datetime.datetime.strptime(values['time'], "%H:%M")
                    hora_escolhida = datetime.timedelta(hours=t.hour,
                                                        minutes=t.minute)
                    hora_fim = hora_escolhida + total_time
                    dia_escolhido = datetime.datetime.strptime(values['day'],
                                                               '%d/%m/%Y')

                    horario_funcionario = datetime.datetime.strptime(self.__establishment.horarios_de_funcionamento[-1], "%H:%M")
                    horario_funcionario_convertido = datetime.timedelta(hours=horario_funcionario.hour,
                                                        minutes=horario_funcionario.minute)

                    if hora_fim > horario_funcionario_convertido:
                        raise EstablishmentUnavailableTimeSchedule
                    else:
                        vaga = Vaga(dia_escolhido, hora_escolhida,
                                    hora_fim)
                        schedule = Agendamento(
                            self.__system_controller.logged_user,
                            total_time,
                            employee,
                            values['plate'],
                            selected_service_type,
                            vaga,
                            total_price,
                            values['vehicle_type']
                        )
                        if self.vaga_is_available(hora_escolhida, hora_fim,
                                              dia_escolhido):
                            self.schedule_registration(schedule)
                        else:
                            raise SpotCarLimitReachedException
                else:
                    raise FuncionarioNotAvailableException

            elif action is None:
                self.__system_controller.shutdown()
            elif action == ClientBoundary.CANCEL:
                self.open_schedule_service_screen()
            else:
                self.__menu.open_menu_client()

        except Exception as e:
            self.__client_screen.show_message(str(e))

    def schedule_registration(self, schedule):
        if isinstance(schedule,
                      Agendamento) and schedule is not None and schedule \
                not in self.__schedule_dao.get_all():
            self.__schedule_dao.add(schedule)
            client: Cliente = self.__system_controller.logged_user
            employee: Funcionario = self.__system_controller.employees_controller.next_employee()

            client.agendamentos = schedule
            employee.agendamentos = schedule

            self.__client_dao.add(client)
            self.__employee_dao.add(employee)

            self.__client_screen.show_message('Ação realizada com sucesso!',
                                              'green')

        else:
            self.__client_screen.show_message('Dados incorretos!', 'red')

    def vaga_is_available(self, horario_escolhido, horario_fim_escolhido,
                          data_escolhida):
        lista_de_agendamentos = self.__schedule_dao.get_all()
        total_vagas_estabelecimento = self.__establishment.total_de_vagas
        vagas_ocupadas = 0
        if lista_de_agendamentos is None or len(lista_de_agendamentos) == 0:
            return True
        else:
            for agendamento in lista_de_agendamentos:
                if data_escolhida == agendamento.vaga.data:
                    if horario_escolhido < agendamento.vaga.horario_inicio:
                        if agendamento.vaga.horario_inicio < horario_fim_escolhido < agendamento.vaga.horario_fim:
                            vagas_ocupadas += 1
                    elif horario_escolhido == agendamento.vaga.horario_inicio:
                        vagas_ocupadas += 1
                    elif horario_escolhido > agendamento.vaga.horario_inicio:
                        if horario_fim_escolhido < agendamento.vaga.horario_fim or horario_escolhido < agendamento.vaga.horario_fim:
                            vagas_ocupadas += 1

            if vagas_ocupadas < total_vagas_estabelecimento:
                return True
            else:
                return False

    def open_schedule_service_screen(self):
        while True:
            try:
                time_list = self.__system_controller.establishment.horarios_de_funcionamento
                vehicle_list = self.__mapper_list('vehicle')
                service_list = self.__mapper_list('service')
                schedule_values = self.__client_screen.open_schedule_screen(
                    vehicle_list, service_list, time_list)
                action = schedule_values['action']
                if action == ClientBoundary.SCHEDULE:
                    values = schedule_values['schedule']
                    self.check_if_is_complete(values)
                    self.open_schedule_confirmation_screen(values)
                elif action is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__client_screen.show_message(
                    'Digite os valores corretos!', 'red')
            except Exception as e:
                self.__client_screen.show_message(str(e))

    def __return_total_time(self, vehicle_type: Veiculo, service: Servico):
        return vehicle_type.duracao + service.duracao

    def __return_total_price(self, vehicle_type: Veiculo, service: Servico):
        return vehicle_type.preco + service.preco

    def __mapper_list(self, type_item: str):
        item_list = None
        if type_item == 'service':
            item_list = self.__types_of_services_dao.get_all()
        if type_item == 'vehicle':
            item_list = self.__vehicle_types_dao.get_all()
        return list(map(self.__return_item_name, item_list))

    def __return_item_name(self, item: Servico or Veiculo):
        return item.nome
