from flanelinha_veloz.control.client_controller import ClientController
from flanelinha_veloz.control.login_controller import LoginController
from flanelinha_veloz.control.employees_controller import EmployeesController


class SystemController:

    def __init__(self):
        self.__login_controller = LoginController(self)
        self.__client_controller = ClientController(self)
        self.__employees_controller = EmployeesController(self)

    @property
    def client_controller(self):
        return self.__client_controller

    @property
    def employees_controller(self):
        return self.__employees_controller

    def open_login_screen(self):
        self.__login_controller.open_screen()
