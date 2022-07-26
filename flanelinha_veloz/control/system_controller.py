from flanelinha_veloz.control.car_spot_controller import CarSpotController
from flanelinha_veloz.control.client_controller import ClientController
from flanelinha_veloz.control.employees_controller import EmployeesController
from flanelinha_veloz.control.establishment_operation_controller import \
    EstablishmentOperationController
from flanelinha_veloz.control.login_controller import LoginController
from flanelinha_veloz.control.menu_controller import MenuController
from flanelinha_veloz.control.send_report_controller import SendReportController
from flanelinha_veloz.control.types_of_services_controller import \
    TypesOfServicesController
from flanelinha_veloz.control.vehicle_types_controller import \
    VehicleTypesController
from flanelinha_veloz.entity.abstractUsuario import Usuario
from flanelinha_veloz.entity.estabelecimento import Estabelecimento


class SystemController:

    def __init__(self):
        self.__login_controller = LoginController(self)
        self.__client_controller = ClientController(self)
        self.__employees_controller = EmployeesController(self)
        self.__vehicle_types_controller = VehicleTypesController(self)
        self.__types_of_services_controller = TypesOfServicesController(self)
        self.__car_spot_controller = CarSpotController(self)
        self.__establishment_operation_controller = EstablishmentOperationController(self)
        self.__menu_controller = MenuController(self)
        self.__send_report_controller = SendReportController(self)
        self.__logged_user: Usuario or None = None
        self.__establishment: Estabelecimento = Estabelecimento(0,
            ['Segunda-feira', 'Terça-feira',
            'Quarta-feira', 'Quinta-feira', 'Sexta-feira'],
            ['9:00',
                                                                 '9:30',
                                                                 '10:00',
                                                                 '10:30',
                                                                 '11:00',
                                                                 '11:30',
                                                                 '12:00',
                                                                 '12:30',
                                                                 '13:00',
                                                                 '13:30',
                                                                 '14:00',
                                                                 '14:30',
                                                                 '15:00',
                                                                 '15:30',
                                                                 '16:00',
                                                                 '16:30',
                                                                 '17:00',
                                                                 '17:30',
                                                                 '18:00'])
        self.update_establishment()

    @property
    def establishment(self) -> Estabelecimento:
        return self.__establishment

    @establishment.setter
    def establishment(self, value: Estabelecimento):
        self.__establishment = value

    @property
    def logged_user(self) -> Usuario:
        return self.__logged_user

    def set_logged_user(self, user: Usuario):
        self.__logged_user = user

    @property
    def menu_controller(self):
        return self.__menu_controller

    @property
    def car_spot_controller(self):
        return self.__car_spot_controller

    @property
    def client_controller(self):
        return self.__client_controller

    @property
    def employees_controller(self):
        return self.__employees_controller

    @property
    def vehicle_types_controller(self):
        return self.__vehicle_types_controller

    @property
    def types_of_services_controller(self):
        return self.__types_of_services_controller

    @property
    def establishment_operation_controller(self):
        return self.__establishment_operation_controller

    def open_login_screen(self):
        self.__send_report_controller.verify_date()
        self.__login_controller.open_screen()

    def shutdown(self):
        exit(0)

    def validate_cpf(self, cpf: str) -> bool:
        numbers = [int(digit) for digit in cpf]

        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        sum_of_products = sum(
            a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        sum_of_products = sum(
            a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def validate_email(self, email: str) -> bool:
        has_char_neededs = False
        sum = 0
        for letter in email:
            if letter == '@' or letter == '.':
                sum += 1
            if sum == 2:
                has_char_neededs = True

        return has_char_neededs

    def update_establishment(self):
        establishment_object = self.__establishment_operation_controller.establishment_operation_dao.get()
        if establishment_object:
            self.establishment = establishment_object

    def update_establishment_key(self, key, value):
        if key == 'total_de_vagas':
            self.establishment.total_de_vagas = value
        elif key == 'dias_de_funcionamento':
            self.establishment.dias_de_funcionamento = value
        elif key == 'horarios_de_funcionamento':
            self.establishment.horarios_de_funcionamento = value
        self.__establishment_operation_controller.establishment_operation_dao.add(self.establishment)

    def see_establishment_key(self, key):
        if key == 'total_de_vagas':
            return self.establishment.total_de_vagas
        elif key == 'dias_de_funcionamento':
            return self.establishment.dias_de_funcionamento
        elif key == 'horarios_de_funcionamento':
            return self.establishment.horarios_de_funcionamento
