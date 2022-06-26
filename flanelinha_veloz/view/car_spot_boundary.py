import PySimpleGUI as sg

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class CarSpotBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    TEXT_SIZE = 20

    def open_options(self):
        layout = [
            [sg.Button('Adicionar', key=1, size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Button('Listar', key=2, size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Button('Excluir', key=3, size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL,
                       size=CarSpotBoundary.TEXT_SIZE)]
        ]

        window = sg.Window('Flanelinha Veloz - Vagas',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(150, 150)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def registration_car_spot_screen(self):
        layout = [
            [sg.Text(
                'Informe a quantidade de vagas a serem adicionadas no estabelecimento: *',
                font='Arial 14')],
            [sg.In(key='qtd_vaga', size=(10, 20), pad=40)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL,
                       size=CarSpotBoundary.TEXT_SIZE),
             sg.Submit('Adicionar', key=CarSpotBoundary.SUBMIT,
                       size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastrar Vagas',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(120, 190)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }

    def list_car_spot_screen(self, vagas_atuais):
        layout = [
            [sg.Text('Total de vagas cadastradas: ', font='Arial 14')],
            [sg.Text(vagas_atuais, font='Arial 14', pad=30)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL,
                       size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Quantidade de Vagas',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(180, 180)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }

    def menu_delete_car_spot_screen(self, vagas_atuais):
        layout = [
            [sg.Text('O Estabelecimento tem', font='Arial 10'),
             sg.Text(vagas_atuais, font='Arial 10', pad=3),
             sg.Text('vaga(s) cadastrada(s).', font='Arial 10')],
            [sg.Text(
                'Informe a quantidade de vagas a serem removidas do estabelecimento: *',
                font='Arial 14')],
            [sg.In(key='qtd_vaga', size=(10, 20), pad=30)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL,
                       size=CarSpotBoundary.TEXT_SIZE),
             sg.Submit('Excluir', key=CarSpotBoundary.SUBMIT,
                       size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Remover Vagas',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(120, 180)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }
