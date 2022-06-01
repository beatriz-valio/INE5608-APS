import hashlib
from datetime import datetime as dt

from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.entity.gestor import Gestor
from flanelinha_veloz.exceptions.cpfNotValidException import \
    CPFNotValidException
from flanelinha_veloz.exceptions.emailDoesntMatchException import \
    EmailDoesntMatchException
from flanelinha_veloz.exceptions.emailNotValidException import \
    EmailNotValidException
from flanelinha_veloz.exceptions.employeesAlreadyExistsInTheSystemException import \
    EmployeesAlreadyExistsInTheSystemException
from flanelinha_veloz.exceptions.employeesNotWritedException import \
    EmployeesNotWritedException
from flanelinha_veloz.exceptions.passwordDoesntMatchException import \
    PasswordDoesntMatchException
from flanelinha_veloz.persistence.employeesDAO import EmployeesDAO
from flanelinha_veloz.view.employees_boundary import EmployeesBoundary


class EmployeesController:
    def __init__(self, system_controller) -> None:
        self.__system_controller = system_controller
        self.__boundary = EmployeesBoundary()
        self.__employee_dao = EmployeesDAO()

    @property
    def employee_dao(self):
        return self.__employee_dao

    def open_edit_employees_screen(self):
        while True:
            try:
                cpf = self.__system_controller.logged_user.cpf
                employees_cpf = self.search_for_employee_by_cpf(cpf)
                if employees_cpf:
                    values = self.__boundary.update_employees_screen(
                        employees_cpf)
                    senha_antiga = employees_cpf.senha
                    acao = values['acao']
                    all_value_good = True
                    if acao == EmployeesBoundary.SUBMIT:
                        valores = values['valores']
                        del (valores['Calendário'])
                        for value in valores:
                            if valores[value] is None or valores[value] == '':
                                all_value_good = False
                        email = valores['email']
                        confirmar_email = valores['confirmar_email']
                        if email != confirmar_email:
                            raise EmailDoesntMatchException
                        elif not self.__system_controller.validate_email(
                                email):
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
                            data_nascimento = dt.strptime(
                                valores['data_nascimento'], "%d/%m/%Y")
                            cpf = int(cpf)
                            genero = valores['genero']
                            sobrenome = valores['sobrenome']
                            cargo = valores['cargo']
                            turno = [valores['primeiro_turno_entrada_hora'],
                                     valores['primeiro_turno_entrada_minuto'],
                                     valores['primeiro_turno_saido_hora'],
                                     valores['primeiro_turno_saido_minuto'],
                                     valores['segundo_turno_entrada_hora'],
                                     valores['segundo_turno_entrada_minuto'],
                                     valores['segundo_turno_saido_hora'],
                                     valores['segundo_turno_saido_minuto']]
                            dias_trabalhados = valores['dias_trabalhados']
                            self.employee_delete(employees_cpf)
                            if cargo == 'Gestor':
                                obj = Gestor(cpf, data_nascimento, email,
                                             genero, nome, senha, sobrenome,
                                             cargo, turno, dias_trabalhados)
                                self.employee_registration(obj)
                                self.__boundary.show_message(
                                    'Atualização salva com sucesso!', 'green')
                                self.__system_controller.menu_controller.open_menu_manager()
                            else:
                                obj = Funcionario(cpf, data_nascimento, email,
                                                  genero, nome, senha,
                                                  sobrenome, cargo, turno,
                                                  dias_trabalhados)
                                self.employee_registration(obj)
                                self.__boundary.show_message(
                                    'Atualização salva com sucesso!', 'green')
                                self.__system_controller.menu_controller.open_menu_employer()
                        else:
                            raise ValueError
                    elif acao == EmployeesBoundary.CANCEL:
                        if employees_cpf.cargo == 'Gestor':
                            self.__system_controller.menu_controller.open_menu_manager()
                        elif employees_cpf.cargo == 'Funcionário':
                            self.__system_controller.menu_controller.open_menu_employer()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    elif acao == EmployeesBoundary.DELETE:
                        self.employee_delete(employees_cpf)
                        self.__boundary.show_message(
                            'Funcionário deletado com sucesso!', 'green')
                        self.__system_controller.open_login_screen()
                    else:
                        break
                else:
                    break
            except ValueError:
                self.__boundary.show_message('Nenhum funcionário cadastrado.',
                                             'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_profile_employees_screen(self):
        while True:
            try:
                cpf = self.__system_controller.logged_user.cpf
                employees_cpf = self.search_for_employee_by_cpf(cpf)
                if employees_cpf:
                    values = self.__boundary.profile_employees_screen(
                        employees_cpf)
                    acao = values['acao']
                    if acao == EmployeesBoundary.UPDATE:
                        self.open_edit_employees_screen()
                    elif acao is None:
                        self.__system_controller.shutdown()
                    else:
                        break
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Não foi possível fazer essa ação!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_add_employees_screen(self):
        while True:
            try:
                values = self.__boundary.registration_employees_screen()
                acao = values['acao']
                all_value_good = True
                if acao == EmployeesBoundary.SUBMIT:
                    valores = values['valores']
                    del (valores['Calendário'])
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
                        elif not self.__system_controller.validate_email(
                                email):
                            raise EmailNotValidException
                        else:
                            senha = valores['senha']
                            confirmar_senha = valores['confirmar_senha']
                            if senha != confirmar_senha:
                                raise PasswordDoesntMatchException
                    if all_value_good:
                        nome = valores['nome']
                        data_nascimento = dt.strptime(
                            valores['data_nascimento'], "%d/%m/%Y")
                        cpf = int(cpf)
                        genero = valores['genero']
                        sobrenome = valores['sobrenome']
                        cargo = valores['cargo']
                        turno = [valores['primeiro_turno_entrada_hora'],
                                 valores['primeiro_turno_entrada_minuto'],
                                 valores['primeiro_turno_saido_hora'],
                                 valores['primeiro_turno_saido_minuto'],
                                 valores['segundo_turno_entrada_hora'],
                                 valores['segundo_turno_entrada_minuto'],
                                 valores['segundo_turno_saido_hora'],
                                 valores['segundo_turno_saido_minuto']]
                        dias_trabalhados = valores['dias_trabalhados']
                        senha = senha.encode('utf-8', 'ignore')
                        senha = hashlib.md5(senha)
                        senha = senha.hexdigest()
                        if cargo == 'Gestor':
                            obj = Gestor(cpf, data_nascimento, email, genero,
                                         nome, senha, sobrenome, cargo, turno,
                                         dias_trabalhados)
                        else:
                            obj = Funcionario(cpf, data_nascimento, email,
                                              genero, nome, senha, sobrenome,
                                              cargo, turno, dias_trabalhados)
                        self.employee_registration(obj)
                        self.__boundary.show_message(
                            'Cadastramento concluído!', 'green')
                        break
                    else:
                        raise ValueError
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break
            except ValueError:
                self.__boundary.show_message(
                    'Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def employee_registration(self, employee):
        if employee is not None and \
                employee not in self.__employee_dao.get_all():
            self.__employee_dao.add(employee)

    def employee_delete(self, employee):
        if employee is not None and \
                employee in self.__employee_dao.get_all():
            self.__employee_dao.remove(employee.cpf)
            self.__system_controller.set_logged_user(None)

    def search_for_employee_by_cpf(self, cpf: str):
        try:
            cpf = int(cpf)
            return self.__employee_dao.get(cpf)
        except KeyError:
            self.__boundary.show_message('Nenhum funcionário encontrado!',
                                         'red')
