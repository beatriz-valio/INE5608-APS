import hashlib
from datetime import datetime as dt, timedelta

from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.entity.gestor import Gestor
from flanelinha_veloz.exceptions.cpfNotValidException import \
    CPFNotValidException
from flanelinha_veloz.exceptions.emailDoesntMatchException import \
    EmailDoesntMatchException
from flanelinha_veloz.exceptions.emailNotValidException import \
    EmailNotValidException
from flanelinha_veloz.exceptions.employeesAlreadyExistsInTheSystemException import \
    EmployeesAlreadyExistsInTheSystemException
from flanelinha_veloz.exceptions.employeesNotWritedException import \
    EmployeesNotWritedException
from flanelinha_veloz.exceptions.missingDataException import \
    MissingDataException
from flanelinha_veloz.exceptions.passwordDoesntMatchException import \
    PasswordDoesntMatchException
from flanelinha_veloz.exceptions.shiftMatchException import ShiftMatchException
from flanelinha_veloz.persistence.employeesDAO import EmployeesDAO
from flanelinha_veloz.view.employees_boundary import EmployeesBoundary


class EmployeesController:
    def __init__(self, system_controller) -> None:
        self.__system_controller = system_controller
        self.__boundary = EmployeesBoundary()
        self.__employee_dao = EmployeesDAO()

    @property
    def employee_dao(self):
        return self.__employee_dao

    def next_employee(self):
        employees = self.__employee_dao.get_all_funcionarios()
        all_employee = {'cpf': None,
                        'agendamentos': timedelta(hours=0, minutes=0)}
        for employee in employees:
            all_jobs = employee.agendamentos
            duration = timedelta(hours=0, minutes=0)
            for job in all_jobs:
                duration = duration + job.duracao
            if duration >= all_employee['agendamentos']:
                all_employee['cpf'] = employee.cpf
                all_employee['agendamentos'] = duration
        if all_employee['cpf'] is None:
            return None
        else:
            return self.search_for_employee_by_cpf(str(all_employee['cpf']))

    def open_edit_employees_screen(self):
        while True:
            try:
                cpf = self.__system_controller.logged_user.cpf
                employees_cpf = self.search_for_employee_by_cpf(cpf)
                if employees_cpf:
                    cargo = 1 if isinstance(self.search_for_employee_by_cpf(cpf), Gestor) == True else 0
                    values = self.__boundary.update_employees_screen(
                        employees_cpf, cargo)
                    senha_antiga = employees_cpf.senha
                    acao = values['acao']
                    if acao == EmployeesBoundary.SUBMIT:
                        valores = values['valores']
                        del (valores['Calendário'])
                        for value in valores:
                            if valores[value] is None or valores[value] == '':
                                raise MissingDataException
                        email = valores['email']
                        confirmar_email = valores['confirmar_email']
                        if email != confirmar_email:
                            raise EmailDoesntMatchException
                        elif not self.__system_controller.validate_email(
                                email):
                            raise EmailNotValidException
                        else:
                            senha = valores['senha']
                            confirmar_senha = valores['confirmar_senha']
                            turno = [valores['primeiro_turno_entrada_hora'],
                                    valores['primeiro_turno_entrada_minuto'],
                                    valores['primeiro_turno_saido_hora'],
                                    valores['primeiro_turno_saido_minuto'],
                                    valores['segundo_turno_entrada_hora'],
                                    valores['segundo_turno_entrada_minuto'],
                                    valores['segundo_turno_saido_hora'],
                                    valores['segundo_turno_saido_minuto']]
                            if senha != confirmar_senha:
                                raise PasswordDoesntMatchException
                            if senha != senha_antiga:
                                senha = senha.encode('utf-8', 'ignore')
                                senha = hashlib.md5(senha)
                                senha = senha.hexdigest()
                            elif not self.checking_different_shifts(turno):
                                raise ShiftMatchException
                        nome = valores['nome']
                        data_nascimento = dt.strptime(
                            valores['data_nascimento'], "%d/%m/%Y")
                        cpf = int(cpf)
                        genero = valores['genero']
                        sobrenome = valores['sobrenome']
                        cargo = valores['cargo']
                        dias_trabalhados = valores['dias_trabalhados']
                        self.employee_delete(employees_cpf)
                        if cargo == 'Gestor':
                            obj = Gestor(cpf, data_nascimento, email,
                                         genero, nome, senha, sobrenome,
                                         turno, dias_trabalhados)
                            self.employee_registration(obj)
                            self.__boundary.show_message(
                                'Atualização salva com sucesso!', 'green')
                            self.__system_controller.menu_controller.open_menu_manager()
                        else:
                            obj = Funcionario(cpf, data_nascimento, email,
                                              genero, nome, senha,
                                              sobrenome, turno,
                                              dias_trabalhados)
                            self.employee_registration(obj)
                            self.__boundary.show_message(
                                'Atualização salva com sucesso!', 'green')
                            self.__system_controller.menu_controller.open_menu_employer()
                    elif acao == EmployeesBoundary.CANCEL:
                        if employees_cpf.cargo == 'Gestor':
                            self.__system_controller.menu_controller.open_menu_manager()
                        elif employees_cpf.cargo == 'Funcionário':
                            self.__system_controller.menu_controller.open_menu_employer()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    elif acao == EmployeesBoundary.DELETE:
                        self.employee_delete(employees_cpf)
                        self.__system_controller.set_logged_user(None)
                        self.__boundary.show_message(
                            'Funcionário deletado com sucesso!', 'green')
                        self.__system_controller.open_login_screen()
                    else:
                        break
                else:
                    break
            except ValueError:
                self.__boundary.show_message('Nenhum funcionário cadastrado.',
                                             'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_profile_employees_screen(self):
        while True:
            try:
                cpf = self.__system_controller.logged_user.cpf
                employees_cpf = self.search_for_employee_by_cpf(cpf)
                if employees_cpf:
                    cargo = 1 if isinstance(self.search_for_employee_by_cpf(cpf), Gestor) == True else 0
                    values = self.__boundary.profile_employees_screen(
                        employees_cpf, cargo)
                    acao = values['acao']
                    if acao == EmployeesBoundary.UPDATE:
                        self.open_edit_employees_screen()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Não foi possível fazer essa ação!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_add_employees_screen(self):
        while True:
            try:
                values = self.__boundary.registration_employees_screen()
                acao = values['acao']
                all_value_good = True
                if acao == EmployeesBoundary.SUBMIT:
                    valores = values['valores']
                    del (valores['Calendário'])
                    for value in valores:
                        if valores[value] is None or valores[value] == '':
                            all_value_good = False
                    cpf = valores['cpf']
                    if not all_value_good:
                        raise ValueError
                    elif cpf is None or cpf == '':
                        raise EmployeesNotWritedException
                    elif not self.__system_controller.validate_cpf(cpf):
                        raise CPFNotValidException
                    elif self.search_for_employee_by_cpf(cpf):
                        raise EmployeesAlreadyExistsInTheSystemException
                    else:
                        email = valores['email']
                        confirmar_email = valores['confirmar_email']
                        if email != confirmar_email:
                            raise EmailDoesntMatchException
                        elif not self.__system_controller.validate_email(
                                email):
                            raise EmailNotValidException
                        else:
                            senha = valores['senha']
                            confirmar_senha = valores['confirmar_senha']
                            turno = [valores['primeiro_turno_entrada_hora'],
                                    valores['primeiro_turno_entrada_minuto'],
                                    valores['primeiro_turno_saido_hora'],
                                    valores['primeiro_turno_saido_minuto'],
                                    valores['segundo_turno_entrada_hora'],
                                    valores['segundo_turno_entrada_minuto'],
                                    valores['segundo_turno_saido_hora'],
                                    valores['segundo_turno_saido_minuto']]
                            if senha != confirmar_senha:
                                raise PasswordDoesntMatchException
                            elif not self.checking_different_shifts(turno):
                                raise ShiftMatchException
                    if all_value_good:
                        nome = valores['nome']
                        data_nascimento = dt.strptime(
                            valores['data_nascimento'], "%d/%m/%Y")
                        cpf = int(cpf)
                        genero = valores['genero']
                        sobrenome = valores['sobrenome']
                        cargo = valores['cargo']
                        dias_trabalhados = valores['dias_trabalhados']
                        senha = senha.encode('utf-8', 'ignore')
                        senha = hashlib.md5(senha)
                        senha = senha.hexdigest()
                        if cargo == 'Gestor':
                            obj = Gestor(cpf, data_nascimento, email, genero,
                                         nome, senha, sobrenome, turno,
                                         dias_trabalhados)
                        else:
                            obj = Funcionario(cpf, data_nascimento, email,
                                              genero, nome, senha, sobrenome,
                                              turno, dias_trabalhados)
                        self.employee_registration(obj)
                        self.__boundary.show_message(
                            'Cadastramento concluído!', 'green')
                        break
                    else:
                        raise ValueError
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def employee_registration(self, employee):
        if employee is not None and \
                employee not in self.__employee_dao.get_all():
            self.__employee_dao.add(employee)

    def employee_delete(self, employee):
        if employee is not None and \
                employee in self.__employee_dao.get_all():
            self.__employee_dao.remove(employee.cpf)

    def search_for_employee_by_cpf(self, cpf: str):
        try:
            cpf = int(cpf)
            return self.__employee_dao.get(cpf)
        except KeyError:
            self.__boundary.show_message('Nenhum funcionário encontrado!',
                                         'red')

    def checking_different_shifts(self, shifts: list):
        final_return = True
        if (shifts[0] == shifts[2] and shifts[1] == shifts[3]) \
             or (shifts[0] == shifts[4] and shifts[1] == shifts[5]) \
             or (shifts[0] == shifts[6]  and shifts[1] == shifts[7]):
            final_return = False
        elif shifts[6] < shifts[4] or shifts[6] < shifts[2] or shifts[6] < shifts[0]:
            final_return = False
        elif shifts[4] < shifts[2] or shifts[6] < shifts[0]:
            final_return = False
        elif shifts[2] < shifts[0]:
            final_return = False
        return final_return
