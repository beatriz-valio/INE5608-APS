class IncorrectLoginException(Exception):
    def __init__(self):
        super().__init__('\033[91m \nUsuário Inválido!\n\033[0m')
