class EmailNotValidException(Exception):
    def __init__(self):
        super().__init__('Email não é válido!')
