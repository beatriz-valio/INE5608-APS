class DurationValueNotValidException(Exception):
    def __init__(self):
        super().__init__('Duração não é válida! Por favor, use o formato hh:mm')
