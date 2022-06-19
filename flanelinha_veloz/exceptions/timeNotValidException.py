class TimeNotValidException(Exception):
    def __init__(self):
        super().__init__('É necessário ter pelo menos 01 hora de funcionamento!')
