class EmailDoesntMatchException(Exception):
    def __init__(self):
        super().__init__('Os e-mails não conferem!')
