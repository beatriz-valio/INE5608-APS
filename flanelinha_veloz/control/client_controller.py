from flanelinha_veloz.entity.cliente import Cliente
from flanelinha_veloz.exceptions.emailDoesntMatchException import EmailDoesntMatchException
from flanelinha_veloz.exceptions.passwordDoesntMatchException import PasswordDoesntMatchException
from flanelinha_veloz.exceptions.userAlreadyExistException import UserAlreadyExistException
from flanelinha_veloz.persistence.clienteDAO import ClienteDAO
from flanelinha_veloz.view.client_boundary import ClientBoundary


def shutdown():
    exit(0)


class ClientController:
    def __init__(self, system_controller):
        self.__client_screen = ClientBoundary()
        self.__client_dao = ClienteDAO()
        self.__system_controller = system_controller

    def return_page(self):
        self.__system_controller.open_login_screen()

    def update_client(self):
        # TODO: Pegar o cliente localmente e atualizar ele com valores novos.
        pass

    def open_create_screen(self):
        while True:
            try:
                client_values = self.__client_screen.open_screen()
                action = client_values['action']
                client_return = client_values['client']
                if action == ClientBoundary.CREATE:
                    already_exist = False
                    cpf = int(client_return['cpf'])
                    if cpf == already_exist:
                        raise UserAlreadyExistException
                    else:
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
                                birth_date = client_return['birth_date']
                                gender = client_return['gender']
                                name = client_return['name']
                                last_name = client_return['last_name']
                                client = Cliente(cpf, birth_date, email, gender, name, password, last_name)
                                self.client_registration(client)
                elif action is None:
                    shutdown()
                else:
                    break
            except ValueError:
                self.__client_screen.show_message('Digite os valores corretos!')

    def client_registration(self, client):
        if isinstance(client, Cliente) and client is not None and client not in self.__client_dao.get_all():
            self.__client_dao.add(client)
            self.__client_screen.show_message('Cadastrado com sucesso!')
        else:
            self.__client_screen.show_message('Dados incorretos!')
