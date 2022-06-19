class carSpotNotValidException(Exception):
    def __init__(self):
        super().__init__('Não é possível excluir essa quantidade de vaga! Você não possui essa quantidade de vaga livre.')
