from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.persistence.abstractDAO import DAO

class EmployeesDAO(DAO):
    def __init__(self):
        super().__init__('/employees_list.pkl')

    def add(self, employee: Funcionario):
        if (isinstance(employee.cpf, int)) and \
                (employee is not None) and \
                isinstance(employee, Funcionario):
            super().add(employee.cpf, employee)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
