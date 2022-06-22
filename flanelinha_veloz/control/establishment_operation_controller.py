from flanelinha_veloz.exceptions.dayNotValidException import DayNotValidException
from flanelinha_veloz.exceptions.establishmentOperationNotValidException import EstablishmentOperationNotValidException
from flanelinha_veloz.exceptions.timeEstablishmentOperationNotValidException import TimeEstablishmentOperationNotValidException
from flanelinha_veloz.persistence.establishmentOperationDAO import EstablishmentOperationDAO
from flanelinha_veloz.view.establishment_operation_boundary import EstablishmentOperationBoundary
from datetime import datetime, time


class EstablishmentOperationController:
    def __init__(self, system_controller):
        self.__boundary = EstablishmentOperationBoundary()
        self.__establishment_operation_dao = EstablishmentOperationDAO()
        self.__system_controller = system_controller

    @property
    def establishment_operation_dao(self) -> EstablishmentOperationDAO:
        return self.__establishment_operation_dao

    def return_menu_manager(self):
        self.__system_controller.menu_controller.open_menu_manager()

    def open_screen(self):
        while True:
            try:
                dias_estabelecimento = self.__system_controller.see_establishment_key('dias_de_funcionamento')
                lista_horarios_funcionando = self.__system_controller.see_establishment_key('horarios_de_funcionamento')
                horario_estabelecimento = self.return_times(lista_horarios_funcionando)

                retorno = self.__boundary.list_establishment_screen(dias_estabelecimento, horario_estabelecimento)
                acao = retorno['acao']
                if acao == EstablishmentOperationBoundary.UPDATE:
                    self.open_edit_establishment_screen()
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break

            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_edit_establishment_screen(self):
        while True:
            try:
                dias_estabelecimento = self.__system_controller.see_establishment_key('dias_de_funcionamento')
                lista_horarios_funcionando = self.__system_controller.see_establishment_key('horarios_de_funcionamento')
                horario_estabelecimento = self.return_times(lista_horarios_funcionando)

                retorno = self.__boundary.menu_update_establishment_screen(dias_estabelecimento, horario_estabelecimento)
                acao = retorno['acao']
                if acao == EstablishmentOperationBoundary.SUBMIT:
                    valores = retorno['valores']
                    novos_dias = valores['dias_de_funcionamento']
                    lista_novos_horarios = self.return_time_list(valores['abertura_estabelecimento_hora'], valores['abertura_estabelecimento_minuto'], valores['fechamento_estabelecimento_hora'], valores['fechamento_estabelecimento_minuto'])

                    if dias_estabelecimento != novos_dias or lista_horarios_funcionando != lista_novos_horarios:
                        if len(novos_dias) > 0:
                            self.__system_controller.update_establishment_key('dias_de_funcionamento', novos_dias)
                        else:
                            raise DayNotValidException
                        if valores['abertura_estabelecimento_hora'] < valores['fechamento_estabelecimento_hora']:
                            self.__system_controller.update_establishment_key('horarios_de_funcionamento', lista_novos_horarios)
                        else:
                            raise TimeEstablishmentOperationNotValidException
                    else:
                        raise EstablishmentOperationNotValidException
                    self.__boundary.show_message('Funcionamento do estabelecimento atualizado!', 'green')
                    break
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break

            except Exception as e:
                self.__boundary.show_message(str(e))

    def return_times(self, lista_horarios):
        horario_abertura = lista_horarios[0].split(":")[0]
        minuto_abertura = lista_horarios[0].split(":")[1]
        horario_fechamento = lista_horarios[-1].split(":")[0]
        minuto_fechamento = lista_horarios[-1].split(":")[1]
        horario_estabelecimento = [int(horario_abertura), int(minuto_abertura), int(horario_fechamento), int(minuto_fechamento)]

        return horario_estabelecimento

    def return_time_list(self, hora_inicial, minuto_inicial, hora_final, minuto_final):
        # Corrige hora menor que 10
        if hora_inicial < 10:
            horario_abertura = '0' + str(hora_inicial) + ':' + str(minuto_inicial)
        else:
            horario_abertura = str(hora_inicial) + ':' + str(minuto_inicial)
        if hora_final < 10:
            horario_fechamento = '0' + str(hora_final) + ':' + str(minuto_final)
        else:
            horario_fechamento = str(hora_final) + ':' + str(minuto_final)

        horario_trabalho = [horario_abertura, horario_fechamento]
        horario_trabalho_convertido = sorted(datetime.strptime(x, '%H:%M').time() for x in horario_trabalho)
        lista_horarios = [time(t,m,0,0).strftime("%H:%M") for t in range(min(horario_trabalho_convertido).hour, (max(horario_trabalho_convertido).hour)+1) for m in [0, 30]]

        # Garante valores iniciais e finais da lista de horários coerentes
        if minuto_inicial != 0 and min(lista_horarios) > horario_abertura:
            lista_horarios.append(horario_abertura)
        elif min(lista_horarios) < horario_abertura:
            lista_horarios.remove(min(lista_horarios))
        if max(lista_horarios) > horario_fechamento:
            lista_horarios.remove(max(lista_horarios))
        elif max(lista_horarios) < horario_fechamento:
            lista_horarios.append(horario_fechamento)
        lista_horarios_estabelecimento = sorted(lista_horarios)

        return lista_horarios_estabelecimento
