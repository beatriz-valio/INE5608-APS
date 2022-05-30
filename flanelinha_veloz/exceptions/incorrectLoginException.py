class IncorrectLoginException(Exception):
    def __init__(self):
        super().__init__('Usuário Inválido!')
