class Jogador():

    # campos "privados"
    _pontuacao_acumulada: int
    _apelido : str
    _email : str
    _senha : str

    def __init__(self, apelido: str, email: str, senha: str):
        self._apelido = apelido
        self._email = email
        self._senha = senha
        self._pontuacao_acumulada = 0 




    
