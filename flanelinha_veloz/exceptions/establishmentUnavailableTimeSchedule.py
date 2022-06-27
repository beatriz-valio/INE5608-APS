class EstablishmentUnavailableTimeSchedule(Exception):
    def __init__(self):
        super().__init__('O estabelecimento não estará aberto nessa duração!')
