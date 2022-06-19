class DayNotValidException(Exception):
    def __init__(self):
        super().__init__('É necessário ter pelo menos 1 dia de funcionamento!')
