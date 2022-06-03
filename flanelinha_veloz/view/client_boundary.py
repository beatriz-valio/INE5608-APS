from datetime import datetime as dt

import PySimpleGUI as sg

from flanelinha_veloz.entity.cliente import Cliente
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class ClientBoundary(AbstractBoundary):
    CANCEL = 0
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    GENDER_OPTIONS = ['Masculino', 'Feminino', 'Outro']

    def open_screen(self):
        layout = [
            [sg.Text('Nome: *'), sg.In(key='name')],
            [sg.Text('Sobrenome: *'), sg.In(key='last_name')],
            [sg.Text('CPF: *'), sg.In(key='cpf')],
            [sg.Text('E-mail: *'), sg.In(key='email')],
            [sg.Text('Confirmação de e-mail: *'), sg.In(key='c-email')],
            [sg.Text('Senha: *'), sg.In(password_char='*', key='password')],
            [sg.Text('Confirmação de senha: *'),
             sg.In(password_char='*', key='c-password')],
            [sg.Text('Gênero: *'),
             sg.Combo(ClientBoundary.GENDER_OPTIONS,
                      default_value=ClientBoundary.GENDER_OPTIONS[0],
                      key='gender')],
            [sg.Text('Data de nascimento: *')],
            [sg.CalendarButton(target='birth_date', button_text="Calendário",
                               format="%d/%m/%Y", ),
             sg.In(key="birth_date")],
            [sg.Cancel('Voltar', key=ClientBoundary.CANCEL),
             sg.Submit('Cadastrar', key=ClientBoundary.CREATE)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastramento', size=(320, 320)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'action': button,
            'client': values
        }

    def open_update_screen(self, client: Cliente):
        layout = [
            [sg.Text('Nome: *'), sg.In(key='name', default_text=client.nome)],
            [sg.Text('Sobrenome: *'),
             sg.In(key='last_name', default_text=client.sobrenome)],
            [sg.Text('CPF: *'), sg.Text(text=client.cpf)],
            [sg.Text('E-mail: *'),
             sg.In(key='email', default_text=client.email)],
            [sg.Text('Confirmação de e-mail: *'),
             sg.In(key='c-email', default_text=client.email)],
            [sg.Text('Senha: *'), sg.In(password_char='*', key='password',
                                        default_text=client.senha)],
            [sg.Text('Confirmação de senha: *'),
             sg.In(password_char='*', key='c-password',
                   default_text=client.senha)],
            [sg.Text('Gênero: *'),
             sg.Combo(ClientBoundary.GENDER_OPTIONS,
                      default_value=client.genero, key='gender')],
            [sg.Text('Data de nascimento: *')],
            [sg.CalendarButton(target='birth_date', button_text="Calendário",
                               format="%d/%m/%Y", ),
             sg.In(key="birth_date", default_text=dt.strftime(client.data_nascimento, "%d/%m/%Y"))],
            [sg.Cancel('Voltar', key=ClientBoundary.CANCEL),
             sg.Submit('Atualizar', key=ClientBoundary.UPDATE)],
            [sg.Text('Deseja excluir seu cadastro?'),
             sg.Submit('Excluir', key=ClientBoundary.DELETE)]
        ]
        window = sg.Window('Flanelinha Veloz - Perfil',
                           size=(360, 360)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'action': button,
            'client': values
        }

    def profile_screen(self, client: Cliente):
        layout = [
            [sg.Text('Nome: *'), sg.Text(key='name', text=client.nome)],
            [sg.Text('Sobrenome: *'),
             sg.Text(key='last_name', text=client.sobrenome)],
            [sg.Text('CPF: *'), sg.Text(text=client.cpf)],
            [sg.Text('E-mail: *'),
             sg.Text(key='email', text=client.email)],
            [sg.Text('Senha: *'), sg.Text(key='password',
                                          text='**************')],
            [sg.Text('Gênero: *'),
             sg.Combo(ClientBoundary.GENDER_OPTIONS,
                      default_value=client.genero, key='gender',
                      disabled=True)],
            [sg.Text('Data de nascimento: *')],
            [sg.Text(dt.strftime(client.data_nascimento, "%d/%m/%Y"))],
            [sg.Cancel('Sair', key=ClientBoundary.CANCEL),
             sg.Submit('Alterar informação', key=ClientBoundary.UPDATE)],
        ]
        window = sg.Window('Flanelinha Veloz - Perfil',
                           size=(360, 360)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return button
