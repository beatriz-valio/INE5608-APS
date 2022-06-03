import hashlib
from datetime import datetime as dt

from flanelinha_veloz.entity.cliente import Cliente
from flanelinha_veloz.exceptions.cpfNotValidException import \
    CPFNotValidException
from flanelinha_veloz.exceptions.emailDoesntMatchException import \
    EmailDoesntMatchException
from flanelinha_veloz.exceptions.emailNotValidException import \
    EmailNotValidException
from flanelinha_veloz.exceptions.missingDataException import MissingDataException
from flanelinha_veloz.exceptions.passwordDoesntMatchException import \
    PasswordDoesntMatchException
from flanelinha_veloz.exceptions.userAlreadyExistException import \
    UserAlreadyExistException
from flanelinha_veloz.persistence.clienteDAO import ClienteDAO
from flanelinha_veloz.view.client_boundary import ClientBoundary


class ClientController:
    def __init__(self, system_controller):
        self.__client_screen = ClientBoundary()
        self.__client_dao = ClienteDAO()
        self.__system_controller = system_controller

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
                                    password = password.encode('utf-8', 'ignore')
                                    password = hashlib.md5(password)
                                    password = password.hexdigest()
                                birth_date = dt.strptime(client_return['birth_date'], "%d/%m/%Y")
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
        del (data['Calendário'])
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
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.__system_controller.shutdown,
                2: self.open_update_screen
            }
            while True:
                option_number = self.__client_screen.profile_screen(
                    self.__system_controller.logged_user)
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__client_screen.show_message(str(e))
