from flanelinha_veloz.entity.vaga import Vaga
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
                # 3: self.open_menu_update_car_spot_screen,
                4: self.open_menu_delete_car_spot_screen
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
                if all_car_spot == 0:
                    self.__boundary.show_message(
                        'Sem vagas cadastradas! Não há vagas para deletar.')
                    break
                else:
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
                        total_vagas = vagas_anteriores - qtd_vaga

                        self.__system_controller.update_establishment_key('total_de_vagas', total_vagas)
                        self.__boundary.show_message(
                            'Quantidade removida com sucesso!', 'green')
                        break
                    elif acao is None:
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
                    'Sem vagas cadastradas! Não há vagas para deletar.')
                    break
                else:
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

    # def validate_duration(self, text):
    #     try:
    #         hour, minute = [int(w) for w in text.split(':')]
    #         if hour > 23 or minute > 60:
    #             return False
    #         elif not isinstance(hour, int) or not isinstance(minute, int):
    #             return False
    #         else:
    #             return True
    #     except ValueError:
    #         return False

    def car_spot_registration(self, car_spot: Vaga):
        if car_spot is not None and \
                isinstance(car_spot, Vaga) and \
                car_spot not in self.__car_spot_dao.get_all():
            self.__car_spot_dao.add(car_spot)

    def car_spot_delete(self, car_spot: Vaga):
        if car_spot is not None and \
                isinstance(car_spot, Vaga) and \
                car_spot in self.__car_spot_dao.get_all():
            self.__car_spot_dao.remove(car_spot.codigo)

    def search_for_car_spot_by_codigo(self, codigo: int):
        try:
            return self.__car_spot_dao.get(codigo)
        except KeyError:
            self.__boundary.show_message('Nenhuma vaga cadastrada!',
                                         'red')

    # def get_x_in_table(self, qtd):
    #     data = []
    #     if qtd == 'all':
    #         for car_spot in self.__car_spot_dao.get_all():
    #             duracao = str(car_spot.duracao)[:-3]
    #             data.append([car_spot.codigo, car_spot.nome, car_spot.preco, duracao])
    #     elif qtd == 'cod_name':
    #         for car_spot in self.__car_spot_dao.get_all():
    #             data.append([car_spot.codigo, car_spot.nome])
    #     elif qtd == 'cod':
    #         for car_spot in self.__car_spot_dao.get_all():
    #             data.append(car_spot.codigo)
    #     return data
    #
    # def update_total_code(self):
    #     return_of_all = self.get_x_in_table('all')
    #     if return_of_all == []:
    #         self.__codigo = 0
    #     else:
    #         last = return_of_all[-1]
    #         code = last[0]
    #         self.__codigo = code + 1
    #     return self.__codigo
    #
    # def exemplo_adicionar(self):
    #     vaga = Vaga(data, horario_inicio, horario_fim)
    #     if self.get_spot_length() < total_Vaga_do_estabelecimento - 1:
    #         self.add(vaga, self.get_spot_length())
    #     else:
    #         raise SpotCarLimitReachedException
    #
    # def exemplo_excluir(self, key: int):
    #     list = self.get_all()
    #     if key in list and list is not None:
    #         self.remove(self.get_spot_length())
    #
    # def get_spot_length(self):
    #     return len(self.get_all())
    #
    # def generate_spot_code(self):
    #     return self.get_spot_length() + 1