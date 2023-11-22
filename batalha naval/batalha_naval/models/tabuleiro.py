class TabuleiroParte():

    _dict_alphanum = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4,
        "F" : 5,
        "G" : 6,
        "H" : 7,
        "I" : 8,
        "J" : 9
    }

    # 10x10
    # [ 'z', 'z', 'z'] === "zzz"
    _matrix = [
        [ 'XXXXXXXXXX' ], # 0
        [ 'XXXXXXXXXX' ], # 1
        [ 'XXXXXXXXXX' ], # ...
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ],
        [ 'XXXXXXXXXX' ]
    ]

    _matrix2 = ["XXXXXXXXXX" for x in range(10)]


    def set_quadrante(self, x, y, val):
        xx = self._dict_alphanum[x]
        yy = y-1
        self._matrix2[xx][yy] = val


    # get_quadrante
    # @param x: coordenada X (valores de A à J)
    # @param y: coordenada Y (valores entre 1 e 10)
    # @return : caracteres do quadrante
    #     X: água
    #     O: não descoberto ainda
    #     N: navio inimigo
    #     E: navio do jogador

    def get_quadrante(self, x, y):
        xx = self._dict_alphanum[x]
        return self._matrix2[xx][y-1]
    

class Tabuleiro():
    
    _parte_a : TabuleiroParte = None
    _parte_b : TabuleiroParte = None
    
    def __init__(self):
        _parte_a = TabuleiroParte()
        _parte_b = TabuleiroParte()