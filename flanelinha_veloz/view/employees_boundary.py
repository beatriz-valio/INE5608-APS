import PySimpleGUI as sg
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary

class EmployeesBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    GENDER_OPTIONS = ['Feminino', 'Masculino', 'Outro']
    FUNCTION_OPTIONS = ['Funcionário', 'Gestor']
    WEEKDAYS_OPTIONS = ['Domingo', 'Segunda-feira', 'Terça-feira','Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def screen_options(self):
        layout = [
            [sg.Button("Cadastrar um novo usuário da empresa", key=1)],
            [sg.Button("Alterar dados de um usuário da empresa", key=2)],
            [sg.Cancel("Voltar", key=0)]
        ]
        window = sg.Window("Flanelinha Veloz - Funcionário/Gestor",
                           size=(900, 500),
                           element_justification="c") \
            .Layout(layout)
        button, value = window.Read()
        window.close()
        return button

    def registration_employees_screen(self):
        layout = [
            [sg.Text("Nome: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key="nome", size=(EmployeesBoundary.INPUT_SIZE))],
            [sg.Text("Sobrenome: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key="sobrenome", size=(EmployeesBoundary.INPUT_SIZE))],
            [sg.Text("CPF: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key="cpf", size=(EmployeesBoundary.INPUT_SIZE))],
            [sg.Text("Email: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key="email", size=(EmployeesBoundary.INPUT_SIZE))],
            [sg.Text("Confirmar Email: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key="confirmar_email", size=(EmployeesBoundary.INPUT_SIZE))],
            [sg.Text("Senha: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key="senha", size=(EmployeesBoundary.INPUT_SIZE), password_char = "*")],
            [sg.Text("Confirmar Senha: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key="confirmar_senha", size=(EmployeesBoundary.INPUT_SIZE), password_char = "*")],
            [sg.Text("Gênero: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.Combo(values=EmployeesBoundary.GENDER_OPTIONS,  key="genero", size=(68))],
            [sg.Text("Data de nascimento: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.In(key='data_nascimento', size=(10), justification='c'),
             sg.CalendarButton(target='data_nascimento', button_text= "Calendário", format = "%d/%m/%Y", size=(54))],
            [sg.Text("Cargo: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.Combo(values=EmployeesBoundary.FUNCTION_OPTIONS,  key="cargo", size=(68))],
            [sg.Text("Primeiro Turno: * ", size=(32)),
             sg.Spin([i for i in range(0,24)], size=(3), key="primeito_turno_entrada_hora"),
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=(3), key="primeito_turno_entrada_minuto"),
             sg.Text("min até às"), 
             sg.Spin([i for i in range(0,24)], size=(3), key="primeito_turno_saido_hora"), 
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=(3), key="primeito_turno_saido_minuto"),
             sg.Text("min", size=(15))],
            [sg.Text("Segundo Turno: * ", size=(32)),
             sg.Spin([i for i in range(0,24)], size=(3), key="segundo_turno_entrada_hora"), 
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=(3), key="segundo_turno_entrada_minuto"),
             sg.Text("min até às"), 
             sg.Spin([i for i in range(0,24)], size=(3), key="segundo_turno_saido_hora"),
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=(3), key="segundo_turno_saido_minuto"),
             sg.Text("min", size=(15))], 
            [sg.Text("Dias trabalhados: * ", size=(EmployeesBoundary.TEXT_SIZE)),
             sg.Listbox(values=EmployeesBoundary.WEEKDAYS_OPTIONS, select_mode='extended', key="dias_trabalhados", size=(68, 7))],
            [sg.Cancel("Voltar", key=EmployeesBoundary.CANCEL), sg.Submit("Avançar", key=EmployeesBoundary.SUBMIT)]
        ]
        window = sg.Window("Flanelinha Veloz - Cadastro Usuário Empresa", 
                            size=(900, 500),
                            element_justification="c") \
                        .Layout(layout)
        button, values = window.Read()
        window.close()
        turnos = [values["primeito_turno_entrada_hora"], values["primeito_turno_entrada_minuto"], values["primeito_turno_saido_hora"], values["primeito_turno_saido_minuto"], values["segundo_turno_entrada_hora"], values["segundo_turno_entrada_minuto"], values["segundo_turno_saido_hora"], values["segundo_turno_saido_minuto"]]
        return {
            "acao": button,
            "nome": values["nome"],
            "sobrenome": values["sobrenome"],
            "cpf": values["cpf"],
            "email": values["email"],
            "confirmar_email": values["confirmar_email"],
            "senha": values["senha"],
            "confirmar_senha": values["confirmar_senha"],
            "genero": values["genero"],
            "data_nascimento": values["data_nascimento"],
            "cargo": values["cargo"],
            "turno": turnos,
            "dias_trabalhados": values["dias_trabalhados"]
        }

# Fazer um para funcionário e outro para gestor
    def editar_usuario_empresa_tela(self, alunos):
        while True:
            lista_usuario_empresa = [
                [sg.Text("\n".join(alunos))]
            ]
            layout = [
                [sg.Col(lista_usuario_empresa, scrollable=True)],
                [sg.Text("Para editar um aluno,")],
                [sg.Text("Digite a matrícula do aluno ->"),
                 sg.In(key="matricula")],
                [sg.Button("Voltar", key=EmployeesBoundary.CANCEL), 
                 sg.Button("Avançar", key=EmployeesBoundary.SUBMIT),
                 sg.Button("Excluir", key=2)]
            ]
            window = sg.Window("Flanelinha Veloz - Editar Usuário Empresa").Layout(layout)
            button, values = window.Read()
            window.close()
            return {
                "acao": button,
                "matricula": values["matricula"]
            }
