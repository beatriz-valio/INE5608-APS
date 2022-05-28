from flanelinha_veloz.entity.gestor import Gestor
from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.view.employees_boundary import EmployeesBoundary

class EmployeesController:
    def __init__(self) -> None:
        # self.__system_controller = system_controller
        self.__boundary = EmployeesBoundary()

    def add_employees(self) -> Funcionario:
        pass


    def retornar(self):
        pass

    def open_screen(self):
        try:
            options = {
                0: self.retornar,
                1: self.add_employees,
                2: self.add_manager
            }
            while True:
                # option_chosed = self.__boundary.tela_opcoes()
                option_chosed = self.__boundary.cadastrar_usuario_empresa_tela()
                function_chosed = options[option_chosed]
                function_chosed()
        except Exception as e:
            print(e)