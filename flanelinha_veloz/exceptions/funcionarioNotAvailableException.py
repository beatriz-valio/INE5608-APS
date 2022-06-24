class FuncionarioNotAvailableException(Exception):
    def __init__(self):
        super().__init__('Não há funcionários disponíveis para o agendamento!')
