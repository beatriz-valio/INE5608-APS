class ExceededSpotCarValueNotValidException(Exception):
    def __init__(self):
        super().__init__(
            'Quantidade maior que a total de vagas! Tente novamente.')
