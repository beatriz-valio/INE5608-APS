from flanelinha_veloz.exceptions.exceededSpotCarValueNotValidException import ExceededSpotCarValueNotValidException
from flanelinha_veloz.exceptions.missingSpotCarException import MissingSpotCarException
from flanelinha_veloz.exceptions.spotCarValueNotValidException import SpotCarValueNotValidException
from flanelinha_veloz.persistence.carSpotDAO import CarSpotDAO
from flanelinha_veloz.view.car_spot_boundary import CarSpotBoundary


class CarSpotController:
    def __init__(self, system_controller):
        self.__boundary = CarSpotBoundary()
        self.__car_spot_dao = CarSpotDAO()
        self.__system_controller = system_controller
    
    def open_screen(self):
        try:            
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.return_menu_manager,
                1: self.open_registration_car_spot_screen,
                2: self.open_list_car_spot_screen,
                3: self.open_menu_delete_car_spot_screen
            }
            while True:
                option_number = self.__boundary.open_options()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__boundary.show_message(str(e))
    
    def return_menu_manager(self):
        self.__system_controller.menu_controller.open_menu_manager()

    def open_registration_car_spot_screen(self):
        while True:
            try:
                values = self.__boundary.registration_car_spot_screen()
                acao = values['acao']
                if acao == CarSpotBoundary.SUBMIT:
                    valores = values['valores']
                    for value in valores:
                        if valores[value] is None or valores[value] == '':
                            raise MissingSpotCarException

                    try:
                        qtd_vaga = int(valores['qtd_vaga'])
                    except Exception:
                        raise SpotCarValueNotValidException

                    if qtd_vaga <= 0:
                        raise SpotCarValueNotValidException

                    vagas_anteriores = self.__system_controller.see_establishment_key('total_de_vagas')
                    total_vagas = vagas_anteriores + qtd_vaga

                    self.__system_controller.update_establishment_key('total_de_vagas', total_vagas)
                    self.__boundary.show_message(
                        'Quantidade adicionada com sucesso!', 'green')
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

    def open_list_car_spot_screen(self):
        while True:
            try:
                all_car_spot = self.__system_controller.see_establishment_key('total_de_vagas')
                if all_car_spot >= 0:
                    values = self.__boundary.list_car_spot_screen(all_car_spot)
                    acao = values['acao']
                    if acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_menu_delete_car_spot_screen(self):
        while True:
            try:
                all_car_spot = self.__system_controller.see_establishment_key('total_de_vagas')
                if all_car_spot == 0:
                    self.__boundary.show_message(
                    'Sem vagas cadastradas! Não há vagas para excluir.')
                    break
                else:
                    values = self.__boundary.menu_delete_car_spot_screen(all_car_spot)
                    acao = values['acao']
                    if acao == CarSpotBoundary.SUBMIT:
                        valores = values['valores']
                        for value in valores:
                            if valores[value] is None or valores[value] == '':
                                raise MissingSpotCarException

                        try:
                            qtd_vaga = int(valores['qtd_vaga'])
                        except Exception:
                            raise SpotCarValueNotValidException

                        if qtd_vaga > all_car_spot:
                            raise ExceededSpotCarValueNotValidException

                        if qtd_vaga <= 0:
                            raise SpotCarValueNotValidException

                        vagas_anteriores = self.__system_controller.see_establishment_key('total_de_vagas')
                        total_vagas = vagas_anteriores - qtd_vaga

                        self.__system_controller.update_establishment_key('total_de_vagas', total_vagas)
                        self.__boundary.show_message(
                            'Quantidade removida com sucesso!', 'green')
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
