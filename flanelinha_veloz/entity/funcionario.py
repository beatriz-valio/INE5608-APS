from datetime import datetime as dt

from flanelinha_veloz.entity.abstractUsuarioEmpresa import UsuarioEmpresa


class Funcionario(UsuarioEmpresa):
    def __init__(self, cpf: int, data_nascimento: dt, email: str, genero: str,
                 nome: str, senha: str, sobrenome: str, cargo: str,
                 turno: list, dias_trabalhados: list, 
                 agendamentos: [] = None) -> None:
        super().__init__(cpf, data_nascimento, email, genero, nome, senha,
                         sobrenome, cargo, turno, dias_trabalhados)
        if agendamentos is not None:
            self.__agendamentos = agendamentos
        else:
            self.__agendamentos = []

    @property
    def agendamentos(self) -> []:
        return self.__agendamentos

    @agendamentos.setter
    def agendamentos(self, agendamentos):
        if agendamentos is None:
            self.__agendamentos = []
        else:
            self.__agendamentos.append(agendamentos)
