class CPFNotValidException(Exception):
    def __init__(self):
        super().__init__('CPF não é válido!')
