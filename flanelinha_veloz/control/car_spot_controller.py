from flanelinha_veloz.exceptions.exceededSpotCarValueNotValidException import \
    ExceededSpotCarValueNotValidException
from flanelinha_veloz.exceptions.missingSpotCarException import \
    MissingSpotCarException
from flanelinha_veloz.exceptions.spotCarValueNotValidException import \
    SpotCarValueNotValidException
from flanelinha_veloz.view.car_spot_boundary import CarSpotBoundary


class CarSpotController:
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__boundary = CarSpotBoundary()

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
                retorno = self.__boundary.registration_car_spot_screen()
                acao = retorno['acao']
                if acao == CarSpotBoundary.SUBMIT:
                    valores = retorno['valores']
                    for campo in valores:
                        if valores[campo] is None or valores[campo] == '':
                            raise MissingSpotCarException

                    try:
                        qtd_vaga = int(valores['qtd_vaga'])
                    except Exception:
                        raise SpotCarValueNotValidException

                    if qtd_vaga <= 0:
                        raise SpotCarValueNotValidException

                    vagas_atuais = self.__system_controller.see_establishment_key(
                        'total_de_vagas')
                    novo_total_vagas = vagas_atuais + qtd_vaga

                    self.__system_controller.update_establishment_key(
                        'total_de_vagas', novo_total_vagas)
                    self.__boundary.show_message(
                        'Quantidade adicionada com sucesso!', 'green')
                    break
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break

            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_list_car_spot_screen(self):
        while True:
            try:
                vagas_atuais = self.__system_controller.see_establishment_key(
                    'total_de_vagas')
                retorno = self.__boundary.list_car_spot_screen(vagas_atuais)
                acao = retorno['acao']
                if acao is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_menu_delete_car_spot_screen(self):
        while True:
            try:
                vagas_atuais = self.__system_controller.see_establishment_key(
                    'total_de_vagas')
                if vagas_atuais <= 0:
                    self.__boundary.show_message(
                        'Sem vagas cadastradas! Não há vagas para excluir.')
                    break
                else:
                    retorno = self.__boundary.menu_delete_car_spot_screen(
                        vagas_atuais)
                    acao = retorno['acao']
                    if acao == CarSpotBoundary.SUBMIT:
                        valores = retorno['valores']
                        for campo in valores:
                            if valores[campo] is None or valores[campo] == '':
                                raise MissingSpotCarException

                        try:
                            qtd_vaga = int(valores['qtd_vaga'])
                        except Exception:
                            raise SpotCarValueNotValidException

                        if qtd_vaga > vagas_atuais:
                            raise ExceededSpotCarValueNotValidException

                        if qtd_vaga <= 0:
                            raise SpotCarValueNotValidException

                        novo_total_vagas = vagas_atuais - qtd_vaga

                        self.__system_controller.update_establishment_key(
                            'total_de_vagas', novo_total_vagas)
                        self.__boundary.show_message(
                            'Quantidade removida com sucesso!', 'green')
                        break
                    elif acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break

            except Exception as e:
                self.__boundary.show_message(str(e))
