class SpotCarLimitReachedException(Exception):
    def __init__(self):
        super().__init__('Limite de vagas atingido!')
