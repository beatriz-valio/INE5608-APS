import PySimpleGUI as sg
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class CarSpotBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    UPDATE = 3
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def open_options(self):
        layout = [
            [sg.Button('Adicionar', key=1, size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Button('Listar', key=2, size=CarSpotBoundary.TEXT_SIZE)],
            # [sg.Button('Alterar', key=3, size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Button('Excluir', key=4, size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL, size=CarSpotBoundary.TEXT_SIZE)]
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
            [sg.Text('Informe as vagas a serem adicionadas no estabelecimento: *', font='Arial 14', size=CarSpotBoundary.INPUT_SIZE)],
            [sg.In(key='qtd_vaga', size=(10, 20), pad=50)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL, size=CarSpotBoundary.TEXT_SIZE),
             sg.Submit('Cadastrar', key=CarSpotBoundary.SUBMIT, size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastro de Vagas',
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
    
    def list_car_spot_screen(self, car_spot):
        layout = [
            [sg.Text('Total de vagas cadastradas: ', font='Arial 14', pad=10),
             sg.Text(total_vagas, font='Arial 14', pad=10)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL, size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Quantidade de Vagas',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(50, 50)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }

    def menu_update_car_spot_screen(self, car_spot):
        column_left = [
            [sg.Table(values=car_spot,
                       headings=['Código', 'Nome'],
                       auto_size_columns=True,
                       justification='center',
                       num_rows=10,
                       vertical_scroll_only=False)]
        ]
        
        column_rigth = [
            [sg.Text('Qual o código? *')],
            [sg.In(key='codigo', justification='c', size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Submit('Atualizar', key=CarSpotBoundary.UPDATE, size=17)]
        ]

        layout = [
            [sg.Text('Qual o tipo de serviço você gostaria de alterar?', font='Arial 16', pad=10)],
            [sg.Column(column_left, element_justification='c'),
             sg.Column([[sg.Text('',size=(2,0))]]),
             sg.Column(column_rigth, element_justification='c', pad=10)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL, size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Atualização Vagas',
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
    
    def update_car_spot_screen(self, car_spot):
        duracao = str(car_spot.duracao)[:-3]
        layout = [
            [sg.Text('Nome: * ', size=CarSpotBoundary.TEXT_SIZE),
             sg.In(default_text=car_spot.nome, key='nome', size=CarSpotBoundary.INPUT_SIZE)],
            [sg.Text('Preço: * ', size=CarSpotBoundary.TEXT_SIZE),
             sg.In(default_text=car_spot.preco, key='preco', size=CarSpotBoundary.INPUT_SIZE)],
            [sg.Text('Duração: * (hh:mm) ', size=CarSpotBoundary.TEXT_SIZE),
             sg.In(default_text=duracao, key='duracao', size=CarSpotBoundary.INPUT_SIZE)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL, size=CarSpotBoundary.TEXT_SIZE),
             sg.Submit('Cadastrar', key=CarSpotBoundary.SUBMIT, size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Atualização Vagas',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(200, 200)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'acao': button,
            'valores': values
        }
    
    def menu_delete_car_spot_screen(self, car_spot):
        column_left = [
            [sg.Table(values=car_spot,
                       headings=['Código', 'Nome'],
                       auto_size_columns=True,
                       justification='center',
                       num_rows=10,
                       vertical_scroll_only=False)]
        ]
        
        column_rigth = [
            [sg.Text('Qual o código? *')],
            [sg.In(key='codigo', justification='c', size=CarSpotBoundary.TEXT_SIZE)],
            [sg.Submit('Deletar', key=CarSpotBoundary.DELETE, size=17)]
        ]

        layout = [
            [sg.Text('Qual o tipo de serviço você gostaria de deletar?', font='Arial 16', pad=10)],
            [sg.Column(column_left, element_justification='c'),
             sg.Column([[sg.Text('',size=(2,0))]]),
             sg.Column(column_rigth, element_justification='c', pad=10)],
            [sg.Cancel('Voltar', key=CarSpotBoundary.CANCEL, size=CarSpotBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Deletar Vagas',
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
