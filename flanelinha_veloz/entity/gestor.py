from flanelinha_veloz.entity.abstractUsuarioEmpresa import UsuarioEmpresa
from datetime import datetime as dt, timedelta

class Gestor(UsuarioEmpresa):
    def __init__(self, cpf: str, data_nacimento: dt, email: str, genero: str, nome: str, senha: str, sobrenome: str, cargo: str, turno: list) -> None:
        super().__init__(cpf, data_nacimento, email, genero, nome, senha, sobrenome, cargo, turno)
