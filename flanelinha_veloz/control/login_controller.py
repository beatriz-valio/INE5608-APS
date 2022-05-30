from flanelinha_veloz.control.system_controller import shutdown
from flanelinha_veloz.view.login_boundary import LoginBoundary


class LoginController:

    def __init__(self, system_controller):
        self.__login_screen = LoginBoundary()
        self.__system_controller = system_controller

    def login(self):
        # Essa função será executado quando o botão de login for clicado. Deverá ser pego os dados passados pelo
        # usuário no campos e trazer o arquivo onde estão salvos os acessos de todos os funcionários para comparar o
        # email com email e ver se a senha bate. Caso a senha bater, poderá seguir para a próxima tela (Nesse momento
        # você checará se ele é cliente ou funcionário e dependendo ele vai para a tela X ou Y). Caso a senha não
        # bata, mostrarem uma mensagem de erro para o usuário.
        pass

    def register_client(self):
        self.__system_controller.client_controller.open_screen()

    def register_employer(self):
        self.__system_controller.employees_controller.open_add_employees_screen()

    def open_screen(self):
        try:
            action_options = {
                None: shutdown,
                0: self.login,
                1: self.register_client,
                2: self.register_employer,
            }
            while True:
                option_number = self.__login_screen.open_screen()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            self.__login_screen.show_message(str(e))
