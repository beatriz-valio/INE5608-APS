class TimeNotValidException(Exception):
    def __init__(self):
        super().__init__('O horário não é válido!')
