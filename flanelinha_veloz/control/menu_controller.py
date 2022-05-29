from flanelinha_veloz.view.menu_boundary import MenuBoundary

class MenuController:

    def __init__(self):
        self.__menu_screen = MenuBoundary()
        # self.__client_controller = ClientController()
        # self.__employer_controller = EmployeesController()


    def ver_perfil(self):
        # self.__employer_controller.open_menu_client();
        pass
    
    def shutdown(self):
        exit(0)

    def open_menu_client(self):
        try:
            action_options = {
                None: self.shutdown,
                0: self.sair,
                1: self.ver_perfil,
                2: self.mudar_perfil,
                3: self.agendar_lavagem
            }
            while True:
                option_number = self.__menu_screen.open_menu_client()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            print(e)