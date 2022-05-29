from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.exceptions.employees_already_exists_in_the_system import employeesAlreadyExistsInTheSystem
# from flanelinha_veloz.control.system_controller import SystemController
from flanelinha_veloz.persistence.employeesDAO import EmployeesDAO
from flanelinha_veloz.view.abstract_boundary import AbstractBoundary
from flanelinha_veloz.view.employees_boundary import EmployeesBoundary


class EmployeesController:
    def __init__(self, system_controller) -> None:
        self.__system_controller = system_controller
        self.__abstract_boundary = AbstractBoundary
        self.__boundary = EmployeesBoundary()
        self.__employee_dao = EmployeesDAO()

    def open_add_employees_screen(self):
        while True:
            valores = self.__boundary.registration_employees_screen()
            nome = valores['nome']
            acao = valores['acao']
            if acao == EmployeesBoundary.SUBMIT:
                try:
                    cpf = valores['cpf']
                    data_nascimento = valores['data_nascimento']
                    email = valores['email']
                    genero = valores['genero']
                    nome = valores['nome']
                    senha = valores['senha']
                    sobrenome = valores['sobrenome']
                    cargo = valores['cargo']
                    turno = valores['turno']
                    dias_trabalhados = valores['dias_trabalhados']
                    if nome is not None and nome != '':
                        if self.search_for_employee_by_cpf(cpf):
                            raise employeesAlreadyExistsInTheSystem
                        else:
                            self.employee_resgistration(
                                Funcionario(cpf, data_nascimento, email, genero, nome, senha, sobrenome, cargo, turno,
                                            dias_trabalhados))
                            self.__boundary.show_message('Cadastramento concluído!')
                        break
                    else:
                        raise ValueError
                except ValueError:
                    self.__boundary.show_message("* Confira  os valores *")
            elif acao == None:
                self.exit()
            else:
                break

    def retornar(self):
        self.__system_controller.open_login_screen()

    def employee_resgistration(self, employee: Funcionario):
        if isinstance(employee, Funcionario) and employee is not None and \
                employee not in self.__employee_dao.get_all():
            self.__employee_dao.add(employee)

    def employee_delete(self, employee: Funcionario):
        if isinstance(employee, Funcionario) and employee is not None and \
                employee in self.__employee_dao.get_all():
            self.__employee_dao.remove(employee.cpf)

    def search_for_employee_by_cpf(self, cpf: str):
        try:
            return self.__employee_dao.get(cpf)
        except KeyError:
            self.__boundary.show_message("Nenhum funcionário encontrado!")

    def exit(self):
        exit(0)

    # def open_screen(self):
    #     try:
    #         options = {
    #             None: self.exit,
    #             0: self.retornar,
    #             1: self.open_add_employees_screen,
    #         }
    #         while True:
    #             option_chosed = self.__boundary.screen_options()
    #             function_chosed = options[option_chosed]
    #             function_chosed()
    #     except Exception as e:
    #         self.__boundary.show_message('oi')
