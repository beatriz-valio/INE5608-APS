import PySimpleGUI as sg

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class NextDayReportBoundary(AbstractBoundary):
    CANCEL = 0
    TEXT_SIZE = 20

    def list_report_screen(self, agendamentos):
        layout = [
            [sg.Text('Relatório de agendamentos do próximo dia: ', font='Arial 14')],
            [sg.Listbox(values=agendamentos,
                        select_mode='extended',
                        key="dias_de_funcionamento",
                        disabled=True,
                        size=(500, 20), pad=10)],
            [sg.Cancel('Voltar', key=NextDayReportBoundary.CANCEL,
                       size=NextDayReportBoundary.TEXT_SIZE, pad=10)]
        ]
        window = sg.Window('Flanelinha Veloz - Quantidade de Vagas',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(100, 100)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }
