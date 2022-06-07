import PySimpleGUI as sg

from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class TypesOfServicesBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    UPDATE = 3
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def open_options(self):
        layout = [
            [sg.Button('Adicionar', key=1, size=TypesOfServicesBoundary.TEXT_SIZE)],
            [sg.Button('Listar', key=2, size=TypesOfServicesBoundary.TEXT_SIZE)],
            [sg.Button('Alterar', key=3, size=TypesOfServicesBoundary.TEXT_SIZE)],
            [sg.Button('Excluir', key=4, size=TypesOfServicesBoundary.TEXT_SIZE)],
            [sg.Cancel('Voltar', key=TypesOfServicesBoundary.CANCEL, size=TypesOfServicesBoundary.TEXT_SIZE)]
        ]

        window = sg.Window('Flanelinha Veloz - Tipos de Serviços',
                           size=(900, 550),
                           element_justification='c',
                           resizable=True,
                           margins=(150, 150)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button

    def registration_types_of_services_screen(self):
        layout = [
            [sg.Text('Nome: * ', size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.In(key='nome', size=TypesOfServicesBoundary.INPUT_SIZE)],
            [sg.Text('Preço: * ', size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.In(key='preco', size=TypesOfServicesBoundary.INPUT_SIZE)],
            [sg.Text('Duração: * (hh:mm) ', size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.In(key='duracao', size=TypesOfServicesBoundary.INPUT_SIZE)],
            [sg.Cancel('Voltar', key=TypesOfServicesBoundary.CANCEL, size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.Submit('Cadastrar', key=TypesOfServicesBoundary.SUBMIT, size=TypesOfServicesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastro Tipos de Serviços',
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
    
    def read_types_of_services_screen(self, types_of_services):
        layout = [
            [sg.Table(values=types_of_services,
                       headings=['Código', 'Nome', 'Preço', 'Duração'],
                       auto_size_columns=True,
                       justification='center',
                       expand_y=True,
                       expand_x=True,
                       vertical_scroll_only=True)],
            [sg.Cancel('Voltar', key=TypesOfServicesBoundary.CANCEL, size=TypesOfServicesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Lista dos Tipos de Serviços',
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

    def menu_update_types_of_services_screen(self, types_of_services):
        column_left = [
            [sg.Table(values=types_of_services,
                       headings=['Código', 'Nome'],
                       auto_size_columns=True,
                       justification='center',
                       num_rows=10,
                       vertical_scroll_only=False)]
        ]
        
        column_rigth = [
            [sg.Text('Qual o código? *')],
            [sg.In(key='codigo', justification='c', size=TypesOfServicesBoundary.TEXT_SIZE)],
            [sg.Submit('Atualizar', key=TypesOfServicesBoundary.UPDATE, size=17)]
        ]

        layout = [
            [sg.Text('Qual o tipo de serviço você gostaria de alterar?', font='Arial 16', pad=10)],
            [sg.Column(column_left, element_justification='c'),
             sg.Column([[sg.Text('',size=(2,0))]]),
             sg.Column(column_rigth, element_justification='c', pad=10)],
            [sg.Cancel('Voltar', key=TypesOfServicesBoundary.CANCEL, size=TypesOfServicesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Atualização Tipos de Serviços',
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
    
    def update_types_of_services_screen(self, types_of_services):
        duracao = str(types_of_services.duracao)[:-3]
        layout = [
            [sg.Text('Nome: * ', size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.In(default_text=types_of_services.nome, key='nome', size=TypesOfServicesBoundary.INPUT_SIZE)],
            [sg.Text('Preço: * ', size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.In(default_text=types_of_services.preco, key='preco', size=TypesOfServicesBoundary.INPUT_SIZE)],
            [sg.Text('Duração: * (hh:mm) ', size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.In(default_text=duracao, key='duracao', size=TypesOfServicesBoundary.INPUT_SIZE)],
            [sg.Cancel('Voltar', key=TypesOfServicesBoundary.CANCEL, size=TypesOfServicesBoundary.TEXT_SIZE),
             sg.Submit('Cadastrar', key=TypesOfServicesBoundary.SUBMIT, size=TypesOfServicesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Atualização Tipos de Serviços',
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
    
    def menu_delete_types_of_services_screen(self, types_of_services):
        column_left = [
            [sg.Table(values=types_of_services,
                       headings=['Código', 'Nome'],
                       auto_size_columns=True,
                       justification='center',
                       num_rows=10,
                       vertical_scroll_only=False)]
        ]
        
        column_rigth = [
            [sg.Text('Qual o código? *')],
            [sg.In(key='codigo', justification='c', size=TypesOfServicesBoundary.TEXT_SIZE)],
            [sg.Submit('Deletar', key=TypesOfServicesBoundary.DELETE, size=17)]
        ]

        layout = [
            [sg.Text('Qual o tipo de serviço você gostaria de deletar?', font='Arial 16', pad=10)],
            [sg.Column(column_left, element_justification='c'),
             sg.Column([[sg.Text('',size=(2,0))]]),
             sg.Column(column_rigth, element_justification='c', pad=10)],
            [sg.Cancel('Voltar', key=TypesOfServicesBoundary.CANCEL, size=TypesOfServicesBoundary.TEXT_SIZE)]
        ]
        window = sg.Window('Flanelinha Veloz - Deletar Tipos de Serviços',
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
