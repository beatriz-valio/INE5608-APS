class SpotCarValueNotValidException(Exception):
    def __init__(self):
        super().__init__(
            'A quantidade deve ser um inteiro positivo! Tente novamente.')
