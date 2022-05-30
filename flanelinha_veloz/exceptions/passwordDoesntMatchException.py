class PasswordDoesntMatchException(Exception):
    def __init__(self):
        super().__init__('As senhas não conferem!')
