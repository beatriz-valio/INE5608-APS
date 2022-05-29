from flanelinha_veloz.view.client_boundary import ClientBoundary


def shutdown():
    exit(0)


class ClientController:
    def __init__(self, system_controller):
        self.__client_screen = ClientBoundary()
        self.__system_controller = system_controller

    def return_page(self):
        self.__system_controller.open_login_screen()

    def create_client(self):
        # TODO: Realizar uma função que ao clicar no botão de cadastrar registre o cliente localmente.
        pass

    def update_client(self):
        # TODO: Pegar o cliente localmente e atualizar ele com valores novos.
        pass

    def open_screen(self):
        try:
            options = {
                None: shutdown,
                0: self.return_page,
                1: self.create_client,
                2: self.update_client
            }

            while True:
                selected_option = self.__client_screen.open_screen()
                selected_function = options[selected_option]
                selected_function()
        except Exception as e:
            self.__client_screen.show_message(str(e))
