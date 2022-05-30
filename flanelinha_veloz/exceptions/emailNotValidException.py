class EmailNotValidException(Exception):
    def __init__(self):
        super().__init__('\033[91m \nEmail não é válido!\n\033[0m')
