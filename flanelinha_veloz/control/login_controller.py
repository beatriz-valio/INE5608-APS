from flanelinha_veloz.entity.abstractUsuario import Usuario
from flanelinha_veloz.view.login_boundary import LoginBoundary


class LoginController:

    def __init__(self, system_controller):
        self.__logged_user: Usuario or None = None
        self.__login_screen = LoginBoundary()
        self.__system_controller = system_controller

    def save_user(self, client: Usuario):
        self.__logged_user = client
        self.__system_controller.set_logged_user(client)

    def check_email_in_clients(self, email, password):
        client_controller = self.__system_controller.client_controller
        for client in client_controller.client_dao.get_all():
            if client.email == email and client.senha == password:
                self.save_user(client)
                self.__system_controller.menu_controller.open_menu_client()

    def check_email_in_employees(self, email, password):
        employees_controller = self.__system_controller.employees_controller
        for employee in employees_controller.employeeDAO.get_all():
            if employee.email == email and employee.senha == password:
                self.save_user(employee)
                if employee.cargo == 'Gestor':
                    self.__system_controller.menu_controller.open_menu_manager()
                elif employee.cargo == 'Funcionário':
                    self.__system_controller.menu_controller.open_menu_employer()

    def login(self, client):
        self.check_email_in_clients(client['email'], client['senha'])
        self.check_email_in_employees(client['email'], client['senha'])
        if self.__logged_user is None:
            self.__login_screen.show_message('Dados incorretos!')

    def register_client(self):
        self.__system_controller.client_controller.open_create_screen()

    def register_employer(self):
        self.__system_controller.employees_controller.open_add_employees_screen()

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
