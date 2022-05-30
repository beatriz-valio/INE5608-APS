import PySimpleGUI as sg
from datetime import datetime as dt

from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.entity.gestor import Gestor
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary


class EmployeesBoundary(AbstractBoundary):
    CANCEL = 0
    SUBMIT = 1
    DELETE = 2
    GENDER_OPTIONS = ['Feminino', 'Masculino', 'Outro']
    FUNCTION_OPTIONS = ['Funcionário', 'Gestor']
    WEEKDAYS_OPTIONS = ['Domingo', 'Segunda-feira', 'Terça-feira','Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
    TEXT_SIZE = 20
    INPUT_SIZE = 70

    def registration_employees_screen(self):
        layout = [
            [sg.Text("Nome: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key="nome", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Sobrenome: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key="sobrenome", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("CPF: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key="cpf", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Email: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key="email", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Confirmar Email: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key="confirmar_email", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Senha: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key="senha", size=EmployeesBoundary.INPUT_SIZE, password_char = "*")],
            [sg.Text("Confirmar Senha: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key="confirmar_senha", size=EmployeesBoundary.INPUT_SIZE, password_char = "*")],
            [sg.Text("Gênero: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.Combo(values=EmployeesBoundary.GENDER_OPTIONS,  key="genero", size=68)],
            [sg.Text("Data de nascimento: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key='data_nascimento', size=10, justification='c'),
             sg.CalendarButton(target='data_nascimento', button_text= "Calendário", format = "%d/%m/%Y", size=(54))],
            [sg.Text("Cargo: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.Combo(values=EmployeesBoundary.FUNCTION_OPTIONS,  key="cargo", size=68)],
            [sg.Text("Primeiro Turno: * ", size=32),
             sg.Spin([i for i in range(0,24)], size=3, key="primeito_turno_entrada_hora"),
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, key="primeito_turno_entrada_minuto"),
             sg.Text("min até às"), 
             sg.Spin([i for i in range(0,24)], size=3, key="primeito_turno_saido_hora"), 
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, key="primeito_turno_saido_minuto"),
             sg.Text("min", size=15)],
            [sg.Text("Segundo Turno: * ", size=32),
             sg.Spin([i for i in range(0,24)], size=3, key="segundo_turno_entrada_hora"), 
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, key="segundo_turno_entrada_minuto"),
             sg.Text("min até às"), 
             sg.Spin([i for i in range(0,24)], size=3, key="segundo_turno_saido_hora"),
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, key="segundo_turno_saido_minuto"),
             sg.Text("min", size=15)], 
            [sg.Text("Dias trabalhados: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.Listbox(values=EmployeesBoundary.WEEKDAYS_OPTIONS, select_mode='extended', key="dias_trabalhados", size=(68, 7))],
            [sg.Cancel("Voltar", key=EmployeesBoundary.CANCEL), 
             sg.Submit("Cadastrar", key=EmployeesBoundary.SUBMIT)]
        ]
        window = sg.Window("Flanelinha Veloz - Cadastro Usuário Empresa", 
                            size=(900, 550),
                            element_justification="c",
                            resizable=True,
                            margins=(35, 35)) \
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

    def update_employees_screen(self, employee: Funcionario or Gestor):
        layout = [
            [sg.Text("Nome: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(default_text= employee.nome, key="nome", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Sobrenome: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(default_text= employee.sobrenome, key="sobrenome", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("CPF: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.Text(employee.cpf, key="cpf", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Email: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(default_text= employee.email, key="email", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Confirmar Email: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(default_text= employee.email, key="confirmar_email", size=EmployeesBoundary.INPUT_SIZE)],
            [sg.Text("Senha: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(default_text= employee.senha, key="senha", size=EmployeesBoundary.INPUT_SIZE, password_char = "*")],
            [sg.Text("Confirmar Senha: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(default_text= employee.senha, key="confirmar_senha", size=EmployeesBoundary.INPUT_SIZE, password_char = "*")],
            [sg.Text("Gênero: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.Combo(EmployeesBoundary.GENDER_OPTIONS,
                    default_value=employee.genero,
                    key="genero",
                    size=68)],
            [sg.Text("Data de nascimento: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.In(key='data_nascimento', size=10, justification='c', default_text=dt.strftime(employee.data_nascimento, "%d/%m/%Y")),
             sg.CalendarButton(target='data_nascimento', button_text= "Calendário", format = "%d/%m/%Y", size=(54))],
            [sg.Text("Cargo: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.Combo(values=EmployeesBoundary.FUNCTION_OPTIONS,
                    default_value= employee.cargo,
                    key="cargo",
                    size=68)],
            [sg.Text("Primeiro Turno: * ", size=32),
             sg.Spin([i for i in range(0,24)], size=3, initial_value= employee.turno[0] , key="primeito_turno_entrada_hora"),
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, initial_value= employee.turno[1], key="primeito_turno_entrada_minuto"),
             sg.Text("min até às"), 
             sg.Spin([i for i in range(0,24)], size=3, initial_value= employee.turno[2], key="primeito_turno_saido_hora"), 
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, initial_value= employee.turno[3], key="primeito_turno_saido_minuto"),
             sg.Text("min", size=15)],
            [sg.Text("Segundo Turno: * ", size=32),
             sg.Spin([i for i in range(0,24)], size=3, initial_value= employee.turno[4], key="segundo_turno_entrada_hora"), 
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, initial_value= employee.turno[5], key="segundo_turno_entrada_minuto"),
             sg.Text("min até às"), 
             sg.Spin([i for i in range(0,24)], size=3, initial_value= employee.turno[6], key="segundo_turno_saido_hora"),
             sg.Text("h"), 
             sg.Spin([i for i in range(0,60,15)], size=3, initial_value= employee.turno[7], key="segundo_turno_saido_minuto"),
             sg.Text("min", size=15)], 
            [sg.Text("Dias trabalhados: * ", size=EmployeesBoundary.TEXT_SIZE),
             sg.Listbox(values=EmployeesBoundary.WEEKDAYS_OPTIONS,
                    select_mode='extended',
                    default_values= employee.dias_trabalhados,
                    key="dias_trabalhados",
                    size=(68, 7))],
            [sg.Cancel("Voltar", key=EmployeesBoundary.CANCEL), 
             sg.Submit("Salvar Informações", key=EmployeesBoundary.SUBMIT)],
            [sg.Text("Gostaria de excluir seu perfil?"),
             sg.Button("Excluir perfil", key=EmployeesBoundary.DELETE)]
        ]
        window = sg.Window("Flanelinha Veloz - Cadastro Usuário Empresa", 
                            size=(900, 550),
                            element_justification="c",
                            resizable=True,
                            margins=(15, 15)) \
                        .Layout(layout)
        button, values = window.Read()
        window.close()
        turnos = [values["primeito_turno_entrada_hora"], values["primeito_turno_entrada_minuto"], values["primeito_turno_saido_hora"], values["primeito_turno_saido_minuto"], values["segundo_turno_entrada_hora"], values["segundo_turno_entrada_minuto"], values["segundo_turno_saido_hora"], values["segundo_turno_saido_minuto"]]
        return {
            "acao": button,
            "nome": values["nome"],
            "sobrenome": values["sobrenome"],
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
