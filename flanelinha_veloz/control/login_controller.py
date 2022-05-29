from flanelinha_veloz.view.login_boundary import LoginBoundary
from flanelinha_veloz.view.menu_boundary import MenuBoundary

class LoginController:

    def __init__(self):
        self.__login_screen = LoginBoundary()
        # self.__client_controller = ClientController()
        # self.__employer_controller = EmployeesController()
        self.__menu_controller = MenuBoundary()


    def login(self):
        # Essa função será executado quando o botão de login for clicado. Deverá ser pego os dados passados pelo usuário no campos e trazer o arquivo onde estão salvos os acessos de todos os funcionários para comparar o email com email e ver se a senha bate.
        # Caso a senha bater, poderá seguir para a próxima tela (Nesse momento você checará se ele é cliente ou funcionário e dependendo ele vai para a tela X ou Y).
        # Caso a senha não bata, mostrarem uma mensagem de erro para o usuário.
        self.__menu_controller.open_menu_client();

    def register_client(self):
        # TODO: Aqui voce deverá chamar o controlador de cliente e chamar a função que abre a tela de cliente.
        # self.__client_controller.open_screen();
        pass

    def register_employer(self):
        # TODO: Aqui voce deverá chamar o controlador de funcionário e chamar a função que abre a tela de funcionário.
        # self.__employer_controller.open_screen();
        pass
    
    def shutdown(self):
        exit(0)

    def open_screen(self):
        try:
            action_options = {
                None: self.shutdown,
                1: self.login,
                2: self.register_client,
                3: self.register_employer,
            }
            while True:
                option_number = self.__login_screen.open_screen()
                selected_function = action_options[option_number]
                selected_function()
        except Exception as e:
            print(e)