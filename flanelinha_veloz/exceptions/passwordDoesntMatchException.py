class PasswordDoesntMatchException(Exception):
    def __init__(self):
        super().__init__('\033[91m \nAs senhas não conferem!\n\033[0m')
