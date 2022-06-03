class MissingDataException(Exception):
    def __init__(self):
        super().__init__('Dados faltantes, rever!')
