from calendar import month
from datetime import datetime, timedelta
from pprint import pprint
from flanelinha_veloz.persistence.scheduleDAO import ScheduleDAO
from flanelinha_veloz.persistence.sendReportDAO import SendReportDAO

class SendReportController:
    def __init__(self, system_controller):
        self.__system_controller = system_controller
        self.__send_report_dao = SendReportDAO()
        self.__schedule_dao = ScheduleDAO()

    def verify_date(self):
        x = 26
        today = datetime.today().strftime("%x")
        fisrtDay = datetime.today().replace(day=x)
        dayToSendEmail = fisrtDay.strftime("%x")
        if today == dayToSendEmail:
            if self.have_to_send_email:
                lastDayLastMonth = fisrtDay - timedelta(days=x)
                firstDayLastMonth = lastDayLastMonth.replace(day=1)
                print(firstDayLastMonth, lastDayLastMonth, dayToSendEmail)
                self.get_data_from_period(firstDayLastMonth, lastDayLastMonth)

    def have_to_send_email(self):
        # Atualizar
        return True

    def get_data_from_period(self, firstDayLastMonth, lastDayLastMonth):
        # Criar lista
        lista_agendamentos = []

        # Pegar último e primeiro dia do mês
        firstDayLastMonth = firstDayLastMonth.strftime("%x")
        lastDayLastMonth = lastDayLastMonth.strftime("%x")

        # Seleção de agendamentos dos mês anterior
        for agendamento in self.__schedule_dao.get_all():
            # pprint(vars(agendamento))
            # print(data_agendamento)
            agendamento_string = ''
            scheduling_date = agendamento.vaga.data.strftime("%x")

            if scheduling_date <= lastDayLastMonth and scheduling_date >= firstDayLastMonth:
                agendamento_string += str(agendamento.vaga.data.strftime("%x")) + '  '
                agendamento_string += str(agendamento.vaga.horario_inicio) + '  '
                agendamento_string += str(agendamento.vaga.horario_fim) + '  '
                agendamento_string += str(agendamento.placa) + ' '
                agendamento_string += str(agendamento.cliente.nome) + ' '
                agendamento_string += str(agendamento.funcionario.nome) + ' '
                agendamento_string += str(agendamento.servico.nome) + ' '
                agendamento_string += str(agendamento.valor) + ' '

                lista_agendamentos.append(agendamento_string)

        print(lista_agendamentos)