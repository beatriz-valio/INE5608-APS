import venv
import PySimpleGUI as sg
from flanelinha_veloz.entity.veiculo import Veiculo

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class VehicleTypesBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    UPDATE = 3
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def open_options(self):
        layout = [
            [sg.Button('Adicionar', key=1, size=VehicleTypesBoundary.TEXT_SIZE)],
            [sg.Button('Listar', key=2, size=VehicleTypesBoundary.TEXT_SIZE)],
            [sg.Button('Alterar', key=3, size=VehicleTypesBoundary.TEXT_SIZE)],
            [sg.Button('Excluir', key=4, size=VehicleTypesBoundary.TEXT_SIZE)],
            [sg.Cancel('Voltar', key=VehicleTypesBoundary.CANCEL, size=VehicleTypesBoundary.TEXT_SIZE)]
        ]

        window = sg.Window('Flanelinha Veloz - Tipos de Veículos',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(150, 150)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def registration_vehicle_types_screen(self):
        layout = [
            [sg.Text('Nome: * ', size=VehicleTypesBoundary.TEXT_SIZE),
             sg.In(key='nome', size=VehicleTypesBoundary.INPUT_SIZE)],
            [sg.Text('Preço: * ', size=VehicleTypesBoundary.TEXT_SIZE),
             sg.In(key='preco', size=VehicleTypesBoundary.INPUT_SIZE)],
            [sg.Text('Duração: * (hh:mm) ', size=VehicleTypesBoundary.TEXT_SIZE),
             sg.In(key='duracao', size=VehicleTypesBoundary.INPUT_SIZE)],
            [sg.Cancel('Voltar', key=VehicleTypesBoundary.CANCEL, size=VehicleTypesBoundary.TEXT_SIZE),
             sg.Submit('Cadastrar', key=VehicleTypesBoundary.SUBMIT, size=VehicleTypesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastro Tipos de Veículo',
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
    
    def read_vehicle_types_screen(self, vehicle_type):
        layout = [
            [sg.Table(values=vehicle_type,
                       headings=['Código', 'Nome', 'Preço', 'Duração'],
                       auto_size_columns=True,
                       justification='center',
                       expand_y=True,
                       expand_x=True,
                       vertical_scroll_only=True)],
            [sg.Cancel('Voltar', key=VehicleTypesBoundary.CANCEL, size=VehicleTypesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Lista dos Tipos de Veículo',
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

    def menu_update_vehicle_types_screen(self, vehicle_type):
        column_left = [
            [sg.Table(values=vehicle_type,
                       headings=['Código', 'Nome'],
                       auto_size_columns=True,
                       # TODO Ajustar o tamanho da coluna/tipo de scroll
                       justification='center',
                       num_rows=10,
                       vertical_scroll_only=False)]
        ]
        
        column_rigth = [
            [sg.Text('Qual o código? *')],
            [sg.In(key='codigo', justification='c', size=VehicleTypesBoundary.TEXT_SIZE)],
            [sg.Submit('Atualizar', key=VehicleTypesBoundary.UPDATE, size=17)]
        ]

        layout = [
            [sg.Text('Qual o tipo de veículo você gostaria de alterar?', font='Arial 16', pad=10)],
            [sg.Column(column_left, element_justification='c'),
             sg.Column([[sg.Text('',size=(2,0))]]),
             sg.Column(column_rigth, element_justification='c', pad=10)],
            [sg.Cancel('Voltar', key=VehicleTypesBoundary.CANCEL, size=VehicleTypesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Atualização Tipos de Veículo',
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
    
    def update_vehicle_types_screen(self, vehicle_type):
        layout = [
            [sg.Text('Nome: * ', size=VehicleTypesBoundary.TEXT_SIZE),
             sg.In(default_text=vehicle_type.nome, key='nome', size=VehicleTypesBoundary.INPUT_SIZE)],
            [sg.Text('Preço: * ', size=VehicleTypesBoundary.TEXT_SIZE),
             sg.In(default_text=vehicle_type.preco, key='preco', size=VehicleTypesBoundary.INPUT_SIZE)],
            [sg.Text('Duração: * (hh:mm) ', size=VehicleTypesBoundary.TEXT_SIZE),
             sg.In(default_text=vehicle_type.duracao, key='duracao', size=VehicleTypesBoundary.INPUT_SIZE)],
            # TODO Mudar a formatação da exibição do dado
            [sg.Cancel('Voltar', key=VehicleTypesBoundary.CANCEL, size=VehicleTypesBoundary.TEXT_SIZE),
             sg.Submit('Cadastrar', key=VehicleTypesBoundary.SUBMIT, size=VehicleTypesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Atualização Tipos de Veículo',
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
    
    def menu_delete_vehicle_types_screen(self, vehicle_type):
        column_left = [
            [sg.Table(values=vehicle_type,
                       headings=['Código', 'Nome'],
                       auto_size_columns=True,
                       justification='center',
                       num_rows=10,
                       vertical_scroll_only=False)]
        ]
        
        column_rigth = [
            [sg.Text('Qual o código? *')],
            [sg.In(key='codigo', justification='c', size=VehicleTypesBoundary.TEXT_SIZE)],
            [sg.Submit('Deletar', key=VehicleTypesBoundary.DELETE, size=17)]
        ]

        layout = [
            [sg.Text('Qual o tipo de veículo você gostaria de deletar?', font='Arial 16', pad=10)],
            [sg.Column(column_left, element_justification='c'),
             sg.Column([[sg.Text('',size=(2,0))]]),
             sg.Column(column_rigth, element_justification='c', pad=10)],
            [sg.Cancel('Voltar', key=VehicleTypesBoundary.CANCEL, size=VehicleTypesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Deletar Tipos de Veículo',
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
