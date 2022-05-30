from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.entity.gestor import Gestor
from flanelinha_veloz.exceptions.cpfNotValid import CPFNotValid
from flanelinha_veloz.exceptions.emailDoesntMatchException import EmailDoesntMatchException
from flanelinha_veloz.exceptions.emailNotValid import EmailNotValid
from flanelinha_veloz.exceptions.employeesNotWrited import EmployeesNotWrited
from flanelinha_veloz.exceptions.passwordDoesntMatchException import PasswordDoesntMatchException
from flanelinha_veloz.view.employees_boundary import EmployeesBoundary
from flanelinha_veloz.persistence.employeesDAO import EmployeesDAO
from flanelinha_veloz.exceptions.employeesAlreadyExistsInTheSystem import EmployeesAlreadyExistsInTheSystem
from datetime import datetime as dt
from pprint import pprint

class EmployeesController:
    def __init__(self, system_controller) -> None:
        self.__system_controller = system_controller
        self.__boundary = EmployeesBoundary()
        self.__employee_dao = EmployeesDAO()

    def open_edit_employees_screen(self):
        pass

    def open_add_employees_screen(self):
        while True:
            try:
                valores = self.__boundary.registration_employees_screen()
                acao = valores['acao']
                all_value_good = True
                if acao == EmployeesBoundary.SUBMIT:
                    for value in valores:
                        if valores[value] is None or valores[value] == '': 
                            all_value_good = False
                    cpf = valores['cpf']
                    if all_value_good == False:
                        raise ValueError
                    elif cpf is None or cpf == '':
                        raise EmployeesNotWrited
                    elif self.validate_cpf(cpf) == False:
                        raise CPFNotValid
                    elif self.search_for_employee_by_cpf(cpf):
                        raise EmployeesAlreadyExistsInTheSystem
                    else:
                        email = valores['email']
                        confirmar_email = valores['confirmar_email']
                        if email != confirmar_email:
                            raise EmailDoesntMatchException
                        elif self.validate_email(email) == False:
                            raise EmailNotValid
                        else:
                            senha = valores['senha']
                            confirmar_senha = valores['confirmar_senha']
                            if senha != confirmar_senha:
                                raise PasswordDoesntMatchException
                    if all_value_good: 
                        nome = valores['nome']
                        data_nascimento = dt.strptime(valores['data_nascimento'], "%d/%m/%Y")
                        cpf = int(cpf)
                        genero = valores['genero']
                        sobrenome = valores['sobrenome']
                        cargo = valores['cargo']
                        turno = valores['turno']
                        dias_trabalhados = valores['dias_trabalhados']
                        self.employee_resgistration(Funcionario(cpf, data_nascimento, email, genero, nome, senha, sobrenome, cargo, turno, dias_trabalhados))
                        self.__boundary.show_message('Cadastramento concluído!')
                        break
                    else:
                        raise ValueError
                elif acao == None:
                    self.exit()
                else:
                    break
            except ValueError:
                self.__boundary.show_message("Existem campos em branco, confira!")
            except Exception as e:
                self.__boundary.show_message(str(e))

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
            cpf = int(cpf)
            return self.__employee_dao.get(cpf)
        except KeyError:
            self.__boundary.show_message("Nenhum funcionário encontrado!")

    def validate_cpf(self, cpf: str) -> bool:
        numbers = [int(digit) for digit in cpf]

        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def validate_email(self, email: str) -> bool:
        has_char_neededs = False
        sum = 0
        for letter in email:
            if letter == '@' or letter == '.':
                sum += 1
            if sum == 2:
                has_char_neededs = True

        return has_char_neededs

    def exit(self):
        exit(0)
