class TimeEstablishmentOperationNotValidException(Exception):
    def __init__(self):
        super().__init__(
            'O horário de abertura não pode exceder o de fechamento. É necessário pelo menos 01 hora de funcionamento.')
