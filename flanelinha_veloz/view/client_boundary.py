from flanelinha_veloz.view.abstract_boundary import AbstractBoundary
import PySimpleGUI as sg


class ClientBoundary(AbstractBoundary):
    CANCEL = 0
    CREATE = 1
    UPDATE = 2
    GENDER_OPTIONS = ['Masculino', 'Feminino', 'Outro']

    def open_screen(self):
        layout = [
            [sg.Text('Nome: *'), sg.In(key='name')],
            [sg.Text('Sobrenome: *'), sg.In(key='last_name')],
            [sg.Text('CPF: *'), sg.In(key='cpf')],
            [sg.Text('E-mail: *'), sg.In(key='email')],
            [sg.Text('Confirmação de e-mail: *'), sg.In(key='c-email')],
            [sg.Text('Senha: *'), sg.In(password_char='*', key='password')],
            [sg.Text('Confirmação de senha: *'), sg.In(password_char='*', key='c-password')],
            [sg.Text('Gênero: *'),
             sg.Combo(ClientBoundary.GENDER_OPTIONS,
                      default_value=ClientBoundary.GENDER_OPTIONS[0], key='gender')],
            [sg.Text('Data de nascimento: *')],
            [sg.CalendarButton(target='birth_date', button_text="Calendário", format="%d/%m/%Y", ),
             sg.In(key="birth_date")],
            [sg.Cancel('Voltar', key=ClientBoundary.CANCEL), sg.Submit('Casdastrar', key=ClientBoundary.CREATE)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastramento', size=(320, 320)) \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            'action': button,
            'client': values
        }

    def open_update_screen(self):
        layout = [
            [sg.Button("Abrir gerência de Cursos", key=1)],
            [sg.Button("Abrir gerência de Disciplinas", key=2)],
            [sg.Button('Abrir gerência de Alunos', key=3)],
            [sg.Cancel('Voltar', key=ClientBoundary.CANCEL), sg.Submit('Avançar', key=ClientBoundary.UPDATE)]
        ]
        window = sg.Window('Flanelinha Veloz - Cadastramento',
                           size=(290, 290), element_justification='c') \
            .Layout(layout)
        button, value = window.Read()
        window.close()
        return button
