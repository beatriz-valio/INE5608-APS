
# TODO: Acertar diagrama com total_vagas

class Estabelecimento:
    def __init__(self, total_vagas:int, dias_de_funcionamento: list, horarios_de_funcionamento: list):
        if isinstance(total_vagas, int):
            self.__total_vagas = total_vagas
        if isinstance(dias_de_funcionamento, list):
            self.__dias_de_funcionamento = dias_de_funcionamento
        if isinstance(horarios_de_funcionamento, list):
            self.__horarios_de_funcionamento = horarios_de_funcionamento

    @property
    def total_vagas(self) -> int:
        return self.__total_vagas

    @total_vagas.setter
    def total_vagas(self, total_vagas: int):
        if isinstance(total_vagas, int):
            self.__total_vagas = total_vagas

    @property
    def dias_de_funcionamento(self) -> list:
        return self.__dias_de_funcionamento

    @dias_de_funcionamento.setter
    def dias(self, dias_de_funcionamento: list):
        if isinstance(dias_de_funcionamento, list):
            self.__dias_de_funcionamento = dias_de_funcionamento

    @property
    def horarios_de_funcionamento(self) -> list:
        return self.__horarios_de_funcionamento

    @horarios_de_funcionamento.setter
    def horarios(self, horarios_de_funcionamento: list):
        if isinstance(horarios_de_funcionamento, list):
            self.__horarios_de_funcionamento = horarios_de_funcionamento
