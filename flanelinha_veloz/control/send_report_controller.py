from calendar import month
from datetime import datetime, timedelta
from flanelinha_veloz.persistence.scheduleDAO import ScheduleDAO
from flanelinha_veloz.persistence.sendReportDAO import SendReportDAO
import pandas as pd


class SendReportController:
    def __init__(self, system_controller):
        self.__send_report_dao = SendReportDAO()
        self.__schedule_dao = ScheduleDAO()

    def verify_date(self):
        x = 1
        today = datetime.today().strftime("%x")
        fisrtDay = datetime.today().replace(day=x)
        dayToSendEmail = fisrtDay.strftime("%x")
        if today == dayToSendEmail:
            if self.need_to_send_email(today):
                lastDayLastMonth = fisrtDay - timedelta(days=x)
                firstDayLastMonth = lastDayLastMonth.replace(day=1)
                self.get_data_from_period(firstDayLastMonth, lastDayLastMonth, today)
                self.send_email()
                self.need_to_send_email(today)
                # self.remove_send_from_today() # Para retirar envio de hoje na hora de validação com a professor

    def need_to_send_email(self, today):
        result = False
        last_send = self.__send_report_dao.get()
        if last_send == today:
            result = True
        return result
    
    def remove_send_from_today(self):
        # Para retirar envio de hoje na hora de validação com a professor
        self.__send_report_dao.remove()

    def send_email(self):
        print('Email enviado para os gestores!')

    def get_data_from_period(self, firstDayLastMonth, lastDayLastMonth, today):
        data = []

        month = str(lastDayLastMonth.strftime("%B"))+'_'+str(lastDayLastMonth.strftime("%Y"))
        firstDayLastMonth = firstDayLastMonth.strftime("%x")
        lastDayLastMonth = lastDayLastMonth.strftime("%x")

        for agendamento in self.__schedule_dao.get_all():
            scheduling_date = agendamento.vaga.data.strftime("%x")

            if scheduling_date <= lastDayLastMonth and scheduling_date >= firstDayLastMonth:
                agendamento_info = []
                agendamento_info.append(agendamento.vaga.data.strftime("%x"))
                agendamento_info.append(str(agendamento.vaga.horario_inicio))
                agendamento_info.append(str(agendamento.vaga.horario_fim))
                agendamento_info.append(agendamento.placa)
                agendamento_info.append(agendamento.cliente.nome)
                agendamento_info.append(agendamento.funcionario.nome)
                agendamento_info.append(agendamento.servico.nome)
                agendamento_info.append(agendamento.valor)

                data.append(agendamento_info)

        dataframe_infos = pd.DataFrame(data, columns=['Data', 'Horário de início', 'Horário de término', 'Placa', 'Nome do cliente', 'Nome do funcionário', 'Tipo de serviço', 'Valor'])
        dataframe_infos.to_csv(f'flanelinha_veloz/files/report_{month}.csv')

        self.__send_report_dao.add(today)
