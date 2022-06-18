from flanelinha_veloz.persistence.establishmentOperationDAO import EstablishmentOperationDAO
from flanelinha_veloz.view.establishment_operation_boundary import EstablishmentOperationBoundary


class EstablishmentOperationController:
    def __init__(self, system_controller):
        self.__boundary = EstablishmentOperationBoundary()
        self.__establishment_operation_dao = EstablishmentOperationDAO()
        self.__system_controller = system_controller

    @property
    def establishment_operation_dao(self) -> EstablishmentOperationDAO:
        return self.__establishment_operation_dao
    
    def return_menu_manager(self):
        self.__system_controller.menu_controller.open_menu_manager()

    def open_screen(self):
        while True:
            try:
                dias_funcionando = self.__system_controller.see_establishment_key('dias_de_funcionamento')
                horarios_funcionando = self.__system_controller.see_establishment_key('horarios_de_funcionamento')


                horario_abertura = horarios_funcionando[0].split(":")[0]
                minuto_abertura = horarios_funcionando[0].split(":")[1]
                horario_fechamento = horarios_funcionando[-1].split(":")[0]
                minuto_fechamento = horarios_funcionando[-1].split(":")[1]
                horario_estabelecimento = [horario_abertura, minuto_abertura, horario_fechamento, minuto_fechamento]


                values = self.__boundary.list_establishment_screen(dias_funcionando, horario_estabelecimento)
                acao = values['acao']
                if acao == EstablishmentOperationBoundary.UPDATE:
                    self.open_edit_establishment_screen()
                elif acao == EstablishmentOperationBoundary.CANCEL:
                    self.return_menu_manager()
                elif acao is None:
                    self.__system_controller.shutdown()
                else:
                    break

            except ValueError:
                self.__boundary.show_message('Não foi possível fazer essa ação!', 'red')
            except Exception as e:
                self.__boundary.show_message(str(e))

    def open_edit_establishment_screen(self):
        while True:
            try:
                dias_funcionando = self.__system_controller.see_establishment_key('dias_de_funcionamento')
                horarios_funcionando = self.__system_controller.see_establishment_key('horarios_de_funcionamento')

                horario_abertura = horarios_funcionando[0].split(":")[0]
                minuto_abertura =  horarios_funcionando[0].split(":")[1]
                horario_fechamento = horarios_funcionando[-1].split(":")[0]
                minuto_fechamento =  horarios_funcionando[-1].split(":")[1]
                horario_estabelecimento = [horario_abertura, minuto_abertura, horario_fechamento, minuto_fechamento]
                print(horario_estabelecimento)

                values = self.__boundary.menu_update_establishment_screen(dias_funcionando, horario_estabelecimento)
                acao = values['acao']
                if acao is None:
                    self.__system_controller.shutdown()
                else:
                    break

            except Exception as e:
                self.__boundary.show_message(str(e))