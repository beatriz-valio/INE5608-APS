class EmailDoesntMatchException(Exception):
    def __init__(self):
        super().__init__('\033[91m \nOs e-mails não conferem!\n\033[0m')
