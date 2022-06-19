from datetime import datetime as dt

from flanelinha_veloz.entity.abstractUsuario import Usuario


# from flanelinha_veloz.entity.agendamento import Agendamento


class Cliente(Usuario):
    def __init__(self, cpf: int, data_nascimento: dt, email: str, genero: str,
                 nome: str, senha: str, sobrenome: str,
                 agendamentos=None):
        super().__init__(cpf, data_nascimento, email, genero, nome, senha,
                         sobrenome)
        if agendamentos is not None:
            self.__agendamentos = agendamentos
        else:
            self.__agendamentos = []

    @property
    def agendamentos(self) -> []:
        return self.__agendamentos

    # TODO: Verificar se a implementação da lista em python está correta.
    @agendamentos.setter
    def agendamentos(self, agendamentos):
        self.agendamentos.append(agendamentos)

    def incrementar_agendamento(self, schedule):
        self.__agendamentos.append(schedule)

    def limpar_agendamentos(self):
        self.__agendamentos = []
