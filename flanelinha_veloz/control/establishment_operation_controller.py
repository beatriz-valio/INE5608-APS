

class EstablishmentOperationController:
    def __init__(self, system_controller) -> None:
        self.__system_controller = system_controller
        # self.__boundary = EmployeesEmployeesBoundary()
        # self.__employee_dao = EmployeesEmployeesDAO()

    @property
    def establishment_operation_dao(self):
        return self.__establishment_operation_dao

    def open_add_screen(self):
        while True:
            try:
                values = self.__boundary.registration_employees_screen()
                acao = values['acao']

            except ValueError:
                self.__boundary.show_message(
                    'Existem campos em branco, confira!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    # def registration(self, code):
    #     if code is not None and \
    #             code not in self.__code_dao.get_all():
    #         self.__code_dao.add(code)

    # def search_for_code_by_cpf(self, cpf: str):
    #     try:
    #         cpf = int(cpf)
    #         return self.__code_dao.get(cpf)
    #     except KeyError:
    #         self.__boundary.show_message('Nenhum funcionário encontrado!',
    #                                      'red')
