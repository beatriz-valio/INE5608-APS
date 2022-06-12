# establishment_operation_controller


class Estabelecimento:
    def __init__(self, total_de_vagas:int, dias_de_funcionamento: list, horarios_de_funcionamento: list):
        if isinstance(total_de_vagas, int):
            self.__total_de_vagas = total_de_vagas
        if isinstance(dias_de_funcionamento, list):
            self.__dias_de_funcionamento = dias_de_funcionamento
        if isinstance(horarios_de_funcionamento, list):
            self.__horarios_de_funcionamento = horarios_de_funcionamento

    @property
    def total_de_vagas(self) -> int:
        return self.__total_de_vagas

    @total_de_vagas.setter
    def total_de_vagas(self, total_de_vagas: int):
        if isinstance(total_de_vagas, int):
            self.__total_de_vagas = total_de_vagas

    @property
    def dias_de_funcionamento(self) -> list:
        return self.__dias_de_funcionamento

    @dias_de_funcionamento.setter
    def dias_de_funcionamento(self, dias_de_funcionamento: list):
        if isinstance(dias_de_funcionamento, list):
            self.__dias_de_funcionamento = dias_de_funcionamento

    @property
    def horarios_de_funcionamento(self) -> list:
        return self.__horarios_de_funcionamento

    @horarios_de_funcionamento.setter
    def horarios_de_funcionamento(self, horarios_de_funcionamento: list):
        if isinstance(horarios_de_funcionamento, list):
            self.__horarios_de_funcionamento = horarios_de_funcionamento
