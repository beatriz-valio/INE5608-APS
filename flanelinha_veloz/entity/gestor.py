from datetime import datetime as dt

from flanelinha_veloz.entity.abstractUsuarioEmpresa import UsuarioEmpresa


class Gestor(UsuarioEmpresa):
    def __init__(self, cpf: int, data_nascimento: dt, email: str, genero: str,
                 nome: str, senha: str, sobrenome: str,
                 turno: list, dias_trabalhados: list) -> None:
        super().__init__(cpf, data_nascimento, email, genero, nome, senha,
                         sobrenome, turno, dias_trabalhados)
