class CPFNotValidException(Exception):
    def __init__(self):
        super().__init__('\033[91m \nCPF não é válido!\n\033[0m')
