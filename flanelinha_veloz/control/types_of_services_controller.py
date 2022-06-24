from datetime import timedelta, datetime

from flanelinha_veloz.entity.servico import Servico
from flanelinha_veloz.exceptions.durationValueNotValidException import DurationValueNotValidException
from flanelinha_veloz.exceptions.missingDataException import MissingDataException
from flanelinha_veloz.exceptions.priceValueNotValidException import PriceValueNotValidException
from flanelinha_veloz.exceptions.typesOfServicesAlreadyExistsInTheSystemException import TypesOfServicesAlreadyExistsInTheSystemException
from flanelinha_veloz.persistence.typesOfServicesDAO import TypesOfServicesDAO
from flanelinha_veloz.view.types_of_services_boundary import TypesOfServicesBoundary


class TypesOfServicesController:
    def __init__(self, system_controller):
        self.__boundary = TypesOfServicesBoundary()
        self.__types_of_services_dao = TypesOfServicesDAO()
        self.__system_controller = system_controller
        self.__codigo = 0

    def open_screen(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.return_menu_manager,
                1: self.open_create_types_of_services_screen,
                2: self.open_read_types_of_services_screen,
                3: self.open_menu_update_types_of_services_screen,
                4: self.open_menu_delete_types_of_services_screen
            }
            while True:
                option_number = self.__boundary.open_options()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__boundary.show_message(str(e))

    def return_menu_manager(self):
        self.__system_controller.menu_controller.open_menu_manager()

    def open_read_types_of_services_screen(self):
        while True:
            try:
                all_types_of_services = self.get_x_in_table('all')
                if all_types_of_services == []:
                    self.__boundary.show_message(
                        'Sem tipo de serviço cadastrados, cadastre algum!')
                    break
                else:
                    values = self.__boundary.read_types_of_services_screen(all_types_of_services)
                    acao = values['acao']
                    if acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except ValueError:
                self.__boundary.show_message(
                    'Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_menu_update_types_of_services_screen(self):
        while True:
            try:
                all_types_of_services = self.get_x_in_table('cod_name')
                if all_types_of_services == []:
                    self.__boundary.show_message(
                        'Sem tipos de serviço cadastrados, cadastre algum!')
                    break
                else:
                    values = self.__boundary.menu_update_types_of_services_screen(all_types_of_services)
                    acao = values['acao']
                    if acao == TypesOfServicesBoundary.UPDATE:
                        try:
                            codigo_para_atualizacao = int(values['valores']['codigo'])
                            vehicle_type = self.search_for_types_of_services_by_codigo(codigo_para_atualizacao)
                            if vehicle_type != None:
                                self.open_update_types_of_services_screen(vehicle_type, codigo_para_atualizacao)
                            else:
                                raise Exception
                        except Exception:
                            self.__boundary.show_message(
                                'Esse código não existe na base!')
                            self.open_menu_update_types_of_services_screen()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except ValueError:
                self.__boundary.show_message(
                    'Valores incoerentes, favor conferir.', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_update_types_of_services_screen(self, vehicle_type, codigo_para_atualizacao):
        while True:
            try:
                values = self.__boundary.update_types_of_services_screen(vehicle_type)
                acoes = values['acao']
                if acoes == TypesOfServicesBoundary.SUBMIT:
                    valor_atualicao = values['valores']
                    for value in valor_atualicao:
                        if valor_atualicao[value] is None or valor_atualicao[value] == '':
                            raise MissingDataException
                    codigo = codigo_para_atualizacao
                    preco = valor_atualicao['preco']
                    duracao = valor_atualicao['duracao']
                    try:
                        preco = float(preco)
                    except Exception:
                        raise PriceValueNotValidException
                    try:
                        duracao = datetime.strptime(duracao, "%H:%M")
                    except Exception:
                        raise DurationValueNotValidException
                    duracao = timedelta(hours=duracao.hour, minutes=duracao.minute)
                    nome = valor_atualicao['nome']
                    obj = Servico(codigo, duracao, nome, preco)
                    self.types_of_services_registration(obj)
                    self.__boundary.show_message(
                        'Atualização do tipo de serviço concluído!', 'green')
                    self.open_screen()
                elif acoes is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Na atualização, existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_menu_delete_types_of_services_screen(self):
        while True:
            try:
                all_types_of_services = self.get_x_in_table('cod_name')
                if all_types_of_services == []:
                    self.__boundary.show_message(
                        'Sem tipos de serviço cadastrados, cadastre algum!')
                    break
                else:
                    values = self.__boundary.menu_delete_types_of_services_screen(all_types_of_services)
                    acao = values['acao']
                    if acao == TypesOfServicesBoundary.DELETE:
                        try:
                            codigo_para_atualizacao = int(values['valores']['codigo'])
                            vehicle_type = self.search_for_types_of_services_by_codigo(codigo_para_atualizacao)
                            if vehicle_type != None:
                                self.types_of_services_delete(vehicle_type)
                                self.__boundary.show_message(
                                    'Tipo de serviço deletado com sucesso!', 'green')
                                self.open_screen()
                            else:
                                raise Exception
                        except Exception:
                            self.__boundary.show_message(
                                'Esse código não existe na base!')
                            self.open_menu_delete_types_of_services_screen()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
            except ValueError:
                self.__boundary.show_message(
                    'Valores em branco, favor conferir.', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_create_types_of_services_screen(self):
        while True:
            try:
                values = self.__boundary.registration_types_of_services_screen()
                acao = values['acao']
                if acao == TypesOfServicesBoundary.SUBMIT:
                    valores = values['valores']
                    for value in valores:
                        if valores[value] is None or valores[value] == '':
                            raise MissingDataException
                    preco = valores['preco']
                    duracao = valores['duracao']
                    try:
                        preco = float(preco)
                    except Exception:
                        raise PriceValueNotValidException
                    try:
                        duracao = datetime.strptime(duracao, "%H:%M")
                    except Exception:
                        raise DurationValueNotValidException
                    duracao = timedelta(hours=duracao.hour, minutes=duracao.minute)
                    nome = valores['nome']
                    self.validate_name(nome)
                    codigo = self.update_total_code()
                    obj = Servico(codigo, duracao, nome, preco)
                    self.types_of_services_registration(obj)
                    self.update_total_code()
                    self.__boundary.show_message(
                        'Cadastramento do tipo de serviço concluído!', 'green')
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

    def validate_name(self, text):
        for vehicle_type in self.__types_of_services_dao.get_all():
            name = str(vehicle_type.nome)
            if name == text:
                raise TypesOfServicesAlreadyExistsInTheSystemException

    def types_of_services_registration(self, types_of_services: Servico):
        if types_of_services is not None and \
                isinstance(types_of_services, Servico) and \
                types_of_services not in self.__types_of_services_dao.get_all():
            self.__types_of_services_dao.add(types_of_services)

    def types_of_services_delete(self, types_of_services: Servico):
        if types_of_services is not None and \
                isinstance(types_of_services, Servico) and \
                types_of_services in self.__types_of_services_dao.get_all():
            self.__types_of_services_dao.remove(types_of_services.codigo)

    def search_for_types_of_services_by_codigo(self, codigo: int):
        try:
            return self.__types_of_services_dao.get(codigo)
        except KeyError:
            self.__boundary.show_message('Nenhum tipo de serviço encontrado!',
                                         'red')

    def search_for_types_of_service_by_name(self, name: str):
        try:
            vehicle_type = None
            for service_types in self.__types_of_services_dao.get_all():
                if service_types.nome == name:
                    return service_types

            if vehicle_type is None:
                raise Exception
            else:
                return vehicle_type
        except KeyError:
            self.__boundary.show_message('Nenhum tipo de serviço encontrado!',
                                         'red')

    def get_x_in_table(self, qtd):
        data = []
        if qtd == 'all':
            for vehicle_type in self.__types_of_services_dao.get_all():
                duracao = str(vehicle_type.duracao)[:-3]
                data.append([vehicle_type.codigo, vehicle_type.nome, vehicle_type.preco, duracao])
        elif qtd == 'cod_name':
            for vehicle_type in self.__types_of_services_dao.get_all():
                data.append([vehicle_type.codigo, vehicle_type.nome])
        elif qtd == 'cod':
            for vehicle_type in self.__types_of_services_dao.get_all():
                data.append(vehicle_type.codigo)
        return data

    def update_total_code(self):
        return_of_all = self.get_x_in_table('all')
        if return_of_all == []:
            self.__codigo = 0
        else:
            last = return_of_all[-1]
            code = last[0]
            self.__codigo = code + 1
        return self.__codigo
