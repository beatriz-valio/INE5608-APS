from pprint import pprint

from flanelinha_veloz.entity.abstractUsuario import Usuario
from flanelinha_veloz.view.login_boundary import LoginBoundary
from flanelinha_veloz.view.menu_boundary import MenuBoundary


class LoginController:

    def __init__(self, system_controller):
        self.__login_screen = LoginBoundary()
        self.__system_controller = system_controller
        self.__menu_controller = MenuBoundary()

    def check_email_in_clients(self, email, password):
        client_controller = self.__system_controller.client_controller
        print(client_controller.clientDAO.get_all())
        for client in client_controller.clientDAO.get_all():
            if client.email == email and client.senha == password:
                print('Entrou um cliente')
                # Abrir o menu de cliente
                self.save_user(client)
                break

    def check_email_in_employees(self, email, password):
        employees_controller = self.__system_controller.employees_controller
        for employee in employees_controller.employeesDAO.get_all():
            if employee.email == email and employee.senha == password:
                if employee.cargo == 'Gestor':
                    print('Entrou um gestor')
                    # Abrir menu de gestor
                    break
                if employee.cargo == 'Funcionário':
                    print('Entrou um funcionário')
                    # Abrir menu de funcionário
                    break
                self.save_user(employee)

    def save_user(self, client: Usuario):
        self.__system_controller.set_logged_user(client)

    def login(self, client):
        try:
            self.check_email_in_clients(client['email'], client['senha'])
            self.check_email_in_employees(client['email'], client['senha'])
            self.__menu_controller.open_menu_client()
        except Exception as e:
            self.__login_screen.show_message('Dados incorretos!')

        # Essa função será executado quando o botão de login for clicado. Deverá ser pego os dados passados pelo
        # usuário no campos e trazer o arquivo onde estão salvos os acessos de todos os funcionários para comparar o
        # email com email e ver se a senha bate. Caso a senha bater, poderá seguir para a próxima tela (Nesse momento
        # você checará se ele é cliente ou funcionário e dependendo ele vai para a tela X ou Y). Caso a senha não
        # bata, mostrarem uma mensagem de erro para o usuário.

    def register_client(self):
        self.__system_controller.client_controller.open_screen()

    def register_employer(self):
        self.__system_controller.employees_controller.open_screen()

    def open_screen(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                1: self.login,
                2: self.register_client,
                3: self.register_employer,
            }
            while True:
                screen_options = self.__login_screen.open_screen()
                option_number = screen_options['action']
                selected_function = action_options[option_number]
                if option_number == 1:
                    self.login(screen_options['user'])
                else:
                    selected_function()
        except Exception as e:
            self.__login_screen.show_message(str(e))
