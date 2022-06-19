class DayNotValidException(Exception):
    def __init__(self):
        super().__init__('É necessário ter pelo menos 01 dia de funcionamento!')
