from flanelinha_veloz.entity.abstractUsuario import Usuario
from flanelinha_veloz.view.login_boundary import LoginBoundary
from flanelinha_veloz.view.menu_boundary import MenuBoundary


class LoginController:

    def __init__(self, system_controller):
        self.__login_screen = LoginBoundary()
        self.__system_controller = system_controller
        self.__menu_controller = MenuBoundary()

    def save_user(self, client: Usuario):
        self.__system_controller.set_logged_user(client)

    def check_email_in_clients(self, email, password):
        client_controller = self.__system_controller.client_controller
        for client in client_controller.clientDAO.get_all():
            if client.email == email and client.senha == password:
                print('Entrou um cliente')
                # Login Cliente
                self.save_user(client)
                return True
        else:
            return False

    def check_email_in_employees(self, email, password):
        employees_controller = self.__system_controller.employees_controller
        # while True:
        for employee in employees_controller.employeeDAO.get_all():
            if employee.email == email and employee.senha == password:
                if employee.cargo == 'Gestor':
                    print('Entrou um gestor')
                    # Login Gestor
                    return employee.cargo
                elif employee.cargo == 'Funcionário':
                    print('Entrou um funcionário')
                    # Login Funcionario
                    return employee.cargo
                self.save_user(employee)
            # else:
            #     return False
            #a@a.com funcionario
            #b@b.com gestor
            #c@c.com cliente

    def login(self, client):
        try:
            # print(self.check_email_in_clients(client['email'], client['senha']))
            # print(self.check_email_in_employees(client['email'], client['senha']))
            # Login Cliente
            if self.check_email_in_clients(client['email'], client['senha']) == True:
                self.__menu_controller.open_menu_client()
            # Login Gestor
            elif self.check_email_in_employees(client['email'], client['senha']) == 'Gestor':
                self.__menu_controller.open_menu_manager()
            # Login Funcionario
            elif self.check_email_in_employees(client['email'], client['senha']) == 'Funcionário':
                self.__menu_controller.open_menu_employer()
            else:
                raise Exception
        except Exception as e:
            self.__login_screen.show_message('Dados incorretos!')

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
