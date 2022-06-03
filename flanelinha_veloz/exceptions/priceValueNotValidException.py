class PriceValueNotValidException(Exception):
    def __init__(self):
        super().__init__('Preço digitado não é válido!')
