from flanelinha_veloz.entity.abstractUsuarioEmpresa import UsuarioEmpresa
from flanelinha_veloz.persistence.abstractDAO import DAO

class EmployeesDAO(DAO):
    def __init__(self):
        super().__init__('flanelinha_veloz/dados/usuarios_empresa.pkl')

    def add(self, employee: UsuarioEmpresa):
        if (isinstance(employee.cpf, int)) and \
                (employee is not None) and \
                isinstance(employee, employee):
            super().add(employee.cpf, employee)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
