from flanelinha_veloz.view.menu_boundary import MenuBoundary


class MenuController:

    def __init__(self, system_controller):
        self.__menu_screen = MenuBoundary()
        self.__system_controller = system_controller

    def see_client_profile(self):
        self.__system_controller.client_controller.open_update_screen()

    def see_employees_profile(self):
        self.__system_controller.employees_controller.open_profile_employees_screen()

    def open_menu_client(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.__system_controller.shutdown,
                1: self.see_client_profile
            }
            while True:
                option_number = self.__menu_screen.open_menu_client()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            # TODO: Verificar porque o show message não está sendo possível utilizar
            print(e)

    def open_menu_manager(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.__system_controller.shutdown,
                1: self.see_employees_profile,
            }
            while True:
                option_number = self.__menu_screen.open_menu_manager()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            # TODO: Verificar porque o show message não está sendo possível utilizar
            print(e)

    def open_menu_employer(self):
        try:
            action_options = {
                None: self.__system_controller.shutdown,
                0: self.__system_controller.shutdown,
                1: self.see_employees_profile,
            }
            while True:
                option_number = self.__menu_screen.open_menu_employer()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            # TODO: Verificar porque o show message não está sendo possível utilizar
            print(e)
