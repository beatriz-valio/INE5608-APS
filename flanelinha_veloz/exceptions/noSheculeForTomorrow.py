class NoScheduleForTomorrow(Exception):
    def __init__(self):
        super().__init__('Não há agendamentos para amanhã!')
