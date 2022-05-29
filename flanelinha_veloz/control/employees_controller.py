from flanelinha_veloz.entity.abstractUsuarioEmpresa import UsuarioEmpresa
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary
from flanelinha_veloz.view.employees_boundary import EmployeesBoundary
# from flanelinha_veloz.control.system_controller import SystemController
from flanelinha_veloz.persistence.employeesDAO import EmployeesDAO
from flanelinha_veloz.exceptions.employees_already_exists_in_the_system import employeesAlreadyExistsInTheSystem
from datetime import datetime as dt

class EmployeesController:
    def __init__(self) -> None:
        # self.__system_controller = SystemController()
        self.__abstract_boundary = AbstractBoundary
        self.__boundary = EmployeesBoundary()
        self.__employee_dao = EmployeesDAO()

    def open_add_employees_screen(self):
        while True:
            valores = self.__boundary.registration_employees_screen()
            nome = valores['nome']
            acao = valores['acao']
            if acao == EmployeesBoundary.SUBMETER:
                try:
                    cpf = valores['cpf']
                    data_nascimento = dt(valores['data_nascimento'])
                    email = valores['email']
                    genero = valores['genero']
                    nome = valores['nome']
                    senha = valores['senha']
                    sobrenome = valores['sobrenome']
                    cargo = valores['cargo']
                    turno = valores['turno']
                    dias_trabalhados = valores['dias_trabalhados']
                    print(cpf, data_nascimento, email, genero, nome, senha, sobrenome, cargo, turno, dias_trabalhados)
                    if nome is not None and nome != '':
                        if self.search_for_employee_by_cpf(cpf):
                            raise employeesAlreadyExistsInTheSystem
                        else:
                            self.employee_resgistration(UsuarioEmpresa(cpf, data_nascimento, email, genero, nome, senha, sobrenome, cargo, turno, dias_trabalhados))
                            self.__boundary.show_message('Cadastramento concluído!')
                        break
                    else:
                        raise ValueError
                except ValueError:
                    self.__boundary.show_message("* Confira  os valores *")
            else:
                break

    def retornar(self):
        # TO DO: Remove comments
        # self.__system_controller.open_screen()
        pass

    def employee_resgistration(self, employee: UsuarioEmpresa):
        if isinstance(employee, UsuarioEmpresa) and employee is not None and \
                employee not in self.__employee_dao.get_all():
            self.__employee_dao.add(employee)
    
    def employee_delete(self, employee: UsuarioEmpresa):
        if isinstance(employee, UsuarioEmpresa) and employee is not None and \
                employee in self.__employee_dao.get_all():
            self.__employee_dao.remove(employee.cpf)
    
    def search_for_employee_by_cpf(self, cpf: int):
        try:
            return self.__funcionario_dao.get(cpf)
        except KeyError:
            self.__boundary.show_message("Nenhum funcionário encontrado!")

    def open_screen(self):
        try:
            options = {
                0: self.retornar,
                1: self.open_add_employees_screen,
            }
            while True:
                option_chosed = self.__boundary.screen_options()
                function_chosed = options[option_chosed]
                function_chosed()
        except Exception as e:
            self.__boundary.show_message(str(e))
