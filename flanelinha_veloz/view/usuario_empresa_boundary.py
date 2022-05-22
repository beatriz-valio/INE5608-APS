import PySimpleGUI as sg

class UsuarioEmpresaBoundary:
    CANCELAR = 0
    SUBMETER = 1

    def tela_opcoes(self):
        layout = [
            [sg.Button("Cadastrar um novo usuário da empresa", key=1)],
            [sg.Button("Alterar dados de um usuário da empresa", key=2)],
            [sg.Button("Excluir um usuário da empresa", key=3)],
            [sg.Button("Listar todos os usuários da empresa", key=4)],
            [sg.Cancel("Voltar", key=UsuarioEmpresaBoundary.CANCELAR)]
        ]
        window = sg.Window("Flanelinha Veloz - Funcionário/Gestor",
                           size=(450, 250),
                           element_justification="c") \
            .Layout(layout)
        button, value = window.Read()
        window.close()
        return button

    def cadastrar_usuario_empresa_tela(self):
        layout = [
            [sg.Text("Nome: "),
             sg.In(key="nome")],
            [sg.Text("Sobrenome: "),
             sg.InputText(key="sobrenome")],
            [sg.Text("CPF: "),
             sg.In(key="cpf")],
            [sg.Text("Email: "),
             sg.In(key="email")],
            [sg.Text("Confirmar Email: "),
             sg.In(key="confirmar_email")],
            [sg.Text("Senha: "),
             sg.In(key="senha")],
            [sg.Text("Confirmar Senha: "),
             sg.In(key="confirmar_senha")],
            [sg.Text("Gênero: "),
             sg.In(key="genero")],
            [sg.Text("Data de Nascimento: "),
             sg.In(key="data_nascimento")],
            [sg.Text("Cargo: "),
             sg.In(key="cargo")],
            [sg.Text("Turno: "),
             sg.In(key="turno")],
            [sg.Text("Dias trabalhados: "),
             sg.In(key="dias_trabalhados")],
            [sg.Button("Voltar", key=0), sg.Button("Avançar", key=1)]
        ]
        window = sg.Window("Flanelinha Veloz - Cadastro Usuário Empresa")\
            .Layout(layout)
        button, values = window.Read()
        window.close()
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
            "turno": values["turno"],
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
                [sg.Cancel("Voltar", key=UsuarioEmpresaBoundary.CANCELAR),
                 sg.Submit("Avançar", key=UsuarioEmpresaBoundary.SUBMETER)]
            ]
            window = sg.Window("Flanelinha Veloz - Editar Usuário Empresa").Layout(layout)
            button, values = window.Read()
            window.close()
            return {
                "acao": button,
                "matricula": values["matricula"]
            }

    def excluir_usuario_empresa_tela(self, alunos):
        lista_usuario_empresa = [
            [sg.Text("\n".join(alunos))]
        ]
        layout = [
            [sg.Col(lista_usuario_empresa, scrollable=True)],
            [sg.Text("Para excluir um aluno,")],
            [sg.Text("Digite a matrícula do aluno ->"),
             sg.In(key="matricula")],
            [sg.Cancel("Voltar", key=UsuarioEmpresaBoundary.CANCELAR),
             sg.Submit("Avançar", key=UsuarioEmpresaBoundary.SUBMETER)]
        ]
        window = sg.Window("Flanelinha Veloz - Excluir um aluno").Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            "acao": button,
            "matricula": values["matricula"]
        }

    def editar_campos_usuario_empresa(self, nome: str, idade: int):
        layout = [
            [sg.Text("Digite um novo nome para o aluno:"),
             sg.Input(nome, key="nome")],
            [sg.Text("Digite uma nova idade para o aluno:"),
             sg.Input(idade, key="idade")],
            [sg.Cancel("Voltar", key=UsuarioEmpresaBoundary.CANCELAR),
             sg.Submit("Avançar", key=UsuarioEmpresaBoundary.SUBMETER)]
        ]
        window = sg.Window("Flanelinha Veloz - Novos dados").Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            "acao": button,
            "nome": values["nome"],
            "idade": values["idade"]
        }

    def listar_usuario_empresa(self, cursos):
        lista_cursos = [
            [sg.Text("\n".join(cursos))]
        ]
        layout = [
            [sg.Col(lista_cursos, scrollable=True)],
            [sg.Text("Digite o código do curso pretendido:"),
             sg.In(key="codigo_curso")],
            [sg.Cancel("Voltar", key=UsuarioEmpresaBoundary.CANCELAR),
             sg.Submit("Avançar", key=UsuarioEmpresaBoundary.SUBMETER)]
        ]
        window = sg.Window("Flanelinha Veloz - Listagem de Alunos") \
            .Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            "acao": button,
            "codigo": values["codigo_curso"]
        }

    def relatorio_usuario_empresa(self, alunos):
        lista_usuario_empresa = [
            [sg.Text("\n".join(alunos))]
        ]
        layout = [
            [sg.Col(lista_usuario_empresa, scrollable=True)],
            [sg.Cancel("Ok", key=UsuarioEmpresaBoundary.CANCELAR)]
        ]
        window = sg.Window("Flanelinha Veloz - Alunos matriculados").Layout(layout)
        button, values = window.Read()
        window.close()
        return {
            "acao": button
        }
