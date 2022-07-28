from datetime import datetime
from flanelinha_veloz.persistence.scheduleDAO import ScheduleDAO
from flanelinha_veloz.view.next_day_report_boundary import NextDayReportBoundary


class NextDayReportController:
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__boundary = NextDayReportBoundary()
        self.__schedule_dao = ScheduleDAO()

    def open_screen(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.return_menu_manager
            }
            while True:
                option_number = self.open_list_report_screen()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__boundary.show_message(str(e))

    def return_menu_manager(self):
        self.__system_controller.menu_controller.open_menu_manager()

    def open_list_report_screen(self):
        while True:
            try:
                lista_agendamentos = []

                # Tratamento variavel dia seguinte
                data_hoje = datetime.now()
                data_string = data_hoje.strftime("%Y/%m/%d, %H:%M:%S")
                hoje_string = data_string.split(",")[0]
                dia = hoje_string.split("/")[2]
                dia_int = int(dia)
                amanha = dia_int + 1

                amanha_data =  hoje_string.split("/")[0] + "/" + hoje_string.split("/")[
                    1] + "/" + str(amanha)
                amanha_convertido = datetime.strptime(amanha_data,
                                                      '%Y/%m/%d').date()

                # Seleção de agendamentos dia seguinte
                for agendamento in self.__schedule_dao.get_all():
                    agendamento_string = ''

                    data_vaga = agendamento.vaga.data
                    data_vaga_string = data_vaga.strftime("%Y/%m/%d, %H:%M:%S")
                    data_padrao = data_vaga_string.split(",")[0]
                    data_convertido = datetime.strptime(data_padrao,
                                                          '%Y/%m/%d').date()

                    if data_convertido == amanha_convertido:
                        data_relatorio = amanha_convertido.strftime("%d/%m/%Y")
                        agendamento_string += '{:^16}'.format(str(data_relatorio))
                        agendamento_string += '{:14}'.format(str(agendamento.vaga.horario_inicio))
                        agendamento_string += '{:14}'.format(str(agendamento.vaga.horario_fim))
                        agendamento_string += '{:^11}'.format(str(agendamento.placa))
                        agendamento_string += '{:^20}'.format(str(agendamento.cliente.nome))
                        agendamento_string += '{:^22}'.format(str(agendamento.funcionario.nome))
                        agendamento_string += '{:^34}'.format(str(agendamento.servico.nome))
                        agendamento_string += '{:^12}'.format(str(agendamento.valor))

                        lista_agendamentos.append(agendamento_string)

                if lista_agendamentos == []:
                    lista_agendamentos.append(' SEM AGENDAMENTOS NO DIA SEGUINTE.')

                retorno = self.__boundary.list_report_screen(lista_agendamentos)
                acao = retorno['acao']
                if acao is None:
                    self.__system_controller.shutdown()
                elif acao == NextDayReportBoundary.CANCEL:
                    self.return_menu_manager()
                else:
                    break
            except Exception as e:
                self.__boundary.show_message(str(e))
