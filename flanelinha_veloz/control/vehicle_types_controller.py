from datetime import timedelta, datetime

from sqlalchemy import false
from flanelinha_veloz.entity.veiculo import Veiculo
from flanelinha_veloz.exceptions.durationValueNotValidException import DurationValueNotValidException
from flanelinha_veloz.exceptions.priceValueNotValidException import PriceValueNotValidException
from flanelinha_veloz.persistence.vehicleTypesDAO import VehicleTypesDAO
from flanelinha_veloz.view.vehicle_types_boundary import vehicleTypesBoundary


class VehicleTypesController:
    def __init__(self, system_controller):
        self.__boundary = vehicleTypesBoundary()
        self.__vehicle_types_dao = VehicleTypesDAO()
        self.__system_controller = system_controller
        self.__codigo = 0
    
    def open_screen(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.return_menu_manager,
                1: self.open_create_employees_screen,
                2: self.open_read_employees_screen,
                3: self.open_update_employees_screen,
                4: self.open_delete_employees_screen
            }
            while True:
                option_number = self.__boundary.open_options()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__boundary.show_message(str(e))
    
    def return_menu_manager(self):
        self.__system_controller.menu_controller.open_menu_manager()

    def open_read_employees_screen(self):
        pass

    def open_update_employees_screen(self):
        pass

    def open_delete_employees_screen(self):
        pass

    def open_create_employees_screen(self):
        while True:
            try:
                values = self.__boundary.registration_vehicle_types_screen()
                acao = values['acao']
                all_value_good = True
                if acao == vehicleTypesBoundary.SUBMIT:
                    valores = values['valores']
                    for value in valores:
                        if valores[value] is None or valores[value] == '':
                            all_value_good = False
                    preco = valores['preco']
                    duracao = valores['duracao']
                    preco = float(preco)
                    if not all_value_good:
                        raise ValueError
                    elif not isinstance(preco, float):
                        raise PriceValueNotValidException
                    elif len(duracao)>5 or len(duracao)<3 or not self.validate_duration(duracao):
                        raise DurationValueNotValidException
                    else:
                        duracao = datetime.strptime(duracao,"%H:%M")
                        duracao = timedelta(hours=duracao.hour, minutes=duracao.minute)
                        nome = valores['nome']
                        codigo = self.__codigo
                        obj = Veiculo(codigo, duracao, nome, preco)
                        self.vehicle_types_registration(obj)
                        self.__boundary.show_message(
                            'Cadastramento do tipo de veículo concluído!', 'green')
                        break
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def validate_duration(self, text):
        try:
            hour, minute = [int(w) for w in text.split(':')]
            if hour > 23 or minute > 60:
                return False
            elif not isinstance(hour, int) or not isinstance(minute, int):
                return False
            else:
                return True
        except ValueError:
            return False

    def vehicle_types_registration(self, vehicle_types: Veiculo):
        if vehicle_types is not None and \
                isinstance(vehicle_types, Veiculo) and \
                vehicle_types not in self.__vehicle_types_dao.get_all():
            self.__vehicle_types_dao.add(vehicle_types)
            self.__codigo = self.__codigo + 1

    def vehicle_types_delete(self, vehicle_types: Veiculo):
        if vehicle_types is not None and \
                isinstance(vehicle_types, Veiculo) and \
                vehicle_types in self.__vehicle_types_dao.get_all():
            self.__vehicle_types_dao.remove(vehicle_types.codigo)

    def search_for_vehicle_types_by_codigo(self, codigo: int):
        try:
            return self.__vehicle_types_dao.get(codigo)
        except KeyError:
            self.__boundary.show_message('Nenhum tipo de veículo encontrado!',
                                         'red')
