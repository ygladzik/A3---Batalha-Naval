class Jogador():

    # campos "privados"
    _apelido: str = None
    _email: str = None
    _senha: str = None
    _idade: int = None
    _pontuacao_acumulada: int = 0

    def __init__(self, apelido: str, email: str, senha: str, idade: int):
        if apelido != None:
                self._apelido = apelido
        else:
            raise Exception("Não pode nome vazio")
  
        if email != None:
                self._email = email
        else:
            raise Exception("Não pode email vazio")
        
        if senha != None:
                self._senha = senha
        else:
            raise Exception("Não pode senha vazia")

        if idade >= 8 and idade <= 120:
            self._idade = idade
        else:
            raise Exception("Não pode idade fora da faixa")
        self._pontuacao = 0

    
    def pontuar(self):
        self._pontuacao += 1



    
