from datetime import datetime as dt

from flanelinha_veloz.entity.abstractUsuario import Usuario


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
        if agendamentos is None:
            self.__agendamentos = []
        else:
            self.__agendamentos.append(agendamentos)
