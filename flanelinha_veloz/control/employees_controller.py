import hashlib
from flanelinha_veloz.view.employees_boundary import EmployeesBoundary
from flanelinha_veloz.entity.funcionario import Funcionario
# from flanelinha_veloz.entity.gestor import Gestor
from flanelinha_veloz.exceptions.cpfNotValidException import CPFNotValidException
from flanelinha_veloz.exceptions.emailDoesntMatchException import EmailDoesntMatchException
from flanelinha_veloz.exceptions.emailNotValidException import EmailNotValidException
from flanelinha_veloz.exceptions.employeesNotWritedException import EmployeesNotWritedException
from flanelinha_veloz.exceptions.passwordDoesntMatchException import PasswordDoesntMatchException
from flanelinha_veloz.persistence.employeesDAO import EmployeesDAO

from flanelinha_veloz.exceptions.employeesAlreadyExistsInTheSystemException import EmployeesAlreadyExistsInTheSystemException
from datetime import datetime as dt


class EmployeesController:
    def __init__(self, system_controller) -> None:
        self.__system_controller = system_controller
        self.__boundary = EmployeesBoundary()
        self.__employee_dao = EmployeesDAO()

    @property
    def employeeDAO(self):
        return self.__employee_dao

    def open_edit_employees_screen(self):
        # TODO: Atualizar o CPF
        while True:
            try:
                cpf = '41754514987'
                employees_cpf = self.search_for_employee_by_cpf(cpf)
                if employees_cpf:
                    valores = self.__boundary.update_employees_screen(employees_cpf)
                    senha_antiga = employees_cpf.senha
                    acao = valores['acao']
                    all_value_good = True
                    if acao == EmployeesBoundary.SUBMIT:
                        for value in valores:
                            if valores[value] is None or valores[value] == '': 
                                all_value_good = False
                        email = valores['email']
                        confirmar_email = valores['confirmar_email']
                        if email != confirmar_email:
                            raise EmailDoesntMatchException
                        elif not self.__system_controller.validate_email(email):
                            raise EmailNotValidException
                        else:
                            senha = valores['senha']
                            confirmar_senha = valores['confirmar_senha']
                            if senha != confirmar_senha:
                                raise PasswordDoesntMatchException
                            if senha != senha_antiga:
                                senha = senha.encode('utf-8', 'ignore')
                                senha = hashlib.md5(senha)
                                senha = senha.hexdigest()
                        if all_value_good: 
                            nome = valores['nome']
                            data_nascimento = dt.strptime(valores['data_nascimento'], "%d/%m/%Y")
                            cpf = int(cpf)
                            genero = valores['genero']
                            sobrenome = valores['sobrenome']
                            cargo = valores['cargo']
                            turno = valores['turno']
                            dias_trabalhados = valores['dias_trabalhados']
                            self.employee_delete(employees_cpf)
                            self.employee_registration(Funcionario(cpf, data_nascimento, email, genero, nome, senha, sobrenome, cargo, turno, dias_trabalhados))
                            self.__boundary.show_message('Atualização salva com sucesso!', 'green')
                            break
                        else:
                            raise ValueError
                    elif acao is None:
                        self.__system_controller.shutdown()    
                    elif acao == EmployeesBoundary.DELETE:
                        self.employee_delete(employees_cpf)
                        self.__boundary.show_message('Funcionário deletado com sucesso!', 'green')
                    else:
                        break
                else:
                    break
            except ValueError:
                self.__boundary.show_message('Nenhum funcionário cadastrado.', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

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
                    if not all_value_good:
                        raise ValueError
                    elif cpf is None or cpf == '':
                        raise EmployeesNotWritedException
                    elif not self.__system_controller.validate_cpf(cpf):
                        raise CPFNotValidException
                    elif self.search_for_employee_by_cpf(cpf):
                        raise EmployeesAlreadyExistsInTheSystemException
                    else:
                        email = valores['email']
                        confirmar_email = valores['confirmar_email']
                        if email != confirmar_email:
                            raise EmailDoesntMatchException
                        elif not self.__system_controller.validate_email(email):
                            raise EmailNotValidException
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
                        senha = senha.encode('utf-8', 'ignore')
                        senha = hashlib.md5(senha)
                        senha = senha.hexdigest()
                        self.employee_registration(Funcionario(cpf, data_nascimento, email, genero, nome, senha, sobrenome, cargo, turno, dias_trabalhados))
                        self.__boundary.show_message('Cadastramento concluído!', 'green')
                        break
                    else:
                        raise ValueError
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__boundary.show_message('Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def employee_registration(self, employee: Funcionario):
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
            self.__boundary.show_message('Nenhum funcionário encontrado!', 'red')

    def return_page(self):
        self.__system_controller.open_login_screen()

    def open_screen(self):
        try:
            options = {
                None: self.__system_controller.shutdown,
                0: self.return_page,
                1: self.open_add_employees_screen,
                2: self.open_edit_employees_screen,
            }
            while True:
                selected_option = self.__boundary.screen_options()
                selected_function = options[selected_option]
                selected_function()
        except Exception as e:
            self.__boundary.show_message(str(e))