class UserAlreadyExistException(Exception):
    def __init__(self):
        super().__init__('\033[91m \nUsuário já existe!\n\033[0m')
