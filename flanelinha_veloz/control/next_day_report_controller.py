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
                data_string = data_hoje.strftime("%d/%m/%Y, %H:%M:%S")
                hoje_string = data_string.split(",")[0]
                dia = hoje_string.split("/")[0]
                dia_int = int(dia)
                amanha = dia_int + 1

                amanha_data = str(amanha) + "/" + hoje_string.split("/")[
                    1] + "/" + hoje_string.split("/")[2]
                amanha_convertido = datetime.strptime(amanha_data,
                                                      '%d/%m/%Y').date()

                # Seleção de agendamentos dia seguinte
                for agendamento in self.__schedule_dao.get_all():
                    agendamento_string = ''

                    if agendamento.vaga.data == amanha_convertido:
                        agendamento_string += agendamento.vaga
                        lista_agendamentos.append(agendamento_string)

                if lista_agendamentos == []:
                    lista_agendamentos.append(' SEM AGENDAMENTOS NO DIA SEGUINTE.')

                retorno = self.__boundary.list_report_screen(lista_agendamentos)
                acao = retorno['acao']
                if acao is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except Exception as e:
                self.__boundary.show_message(str(e))
