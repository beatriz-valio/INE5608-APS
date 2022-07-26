import PySimpleGUI as sg

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class NextDayReportBoundary(AbstractBoundary):
    CANCEL = 0

    def list_report_screen(self, agendamentos):
        layout = [
            [sg.Text('Relatório de Agendamentos - Amanhã', font='Arial 14', pad=10) ],
            [[sg.Text('|      Data      |    Início    |      Fim      |    Placa    |      Cliente      |    Funcionário    |     Tipo de Serviço     |   Valor Total   |', font='Arial 11', pad=5)],
             sg.Listbox(values=agendamentos,
                        select_mode='extended',
                        key="dias_de_funcionamento",
                        disabled=True,
                        size=(500, 20), pad=10)],
            [sg.Cancel('Voltar', key=NextDayReportBoundary.CANCEL,
                       size=10, pad=20)]
        ]
        window = sg.Window('Flanelinha Veloz - Relatório Agendamentos Dia Seguinte',
                           size=(900, 550),
                           resizable=True,
                           margins=(20, 20)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }
