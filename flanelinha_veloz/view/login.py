import PySimpleGUI as sg
# sg.theme('')

layout = [
    # [sg.Image(logo)],
    [sg.Text('E-mail')],
    [sg.Input(key='email')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Entrar', key='entrar')],
    [sg.Text('', key='mensagem')],
    [sg.Text('Não possui cadastro?')],
    [sg.Button('Cadastro de Cliente', key='cadastrar_cliente')],
    [sg.Button('Cadastro de Funcionário', key='cadastrar_funcionario')],
]

window = sg.Window('Flanelinha Veloz', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    # elif event == 'entrar':
        # usuario_correto = ....
        # senha_correta = ....
        # usuario = values['usuario']
        # senha = values['senha']
        # if usuario == usuario_correto and senha == senha_correta:
        #     window[] ...... abrir tela
        # else:
        #     window['mensagem'].update('Usuário ou Senha incorreto.')
    # elif event == 'cadastrar_cliente':
    # elif event == 'cadastrar_funcionario':

