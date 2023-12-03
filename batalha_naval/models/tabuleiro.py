class TabuleiroParte():
    _x = None
    _y = None
    _tab = [["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
        ["A","A","A","A","A","A","A","A","A","A"],
    ]

    _dict_alphanum = {
        0 : "E",
        1 : "M",
        2 : "H",
        3 : "L",
    }

    _dict_alphanam = {
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
    #_matrix = [
    #    [ 'XXXXXXXXXX' ], # 0
    #    [ 'XXXXXXXXXX' ], # 1
    #    [ 'XXXXXXXXXX' ], # ...
    #    [ 'XXXXXXXXXX' ],
    #    [ 'XXXXXXXXXX' ],
    #    [ 'XXXXXXXXXX' ],
    #    [ 'XXXXXXXXXX' ],
    #    [ 'XXXXXXXXXX' ],
    #    [ 'XXXXXXXXXX' ],
    #    [ 'XXXXXXXXXX' ]
    #]

    #_matrix2 = ["XXXXXXXXXX" for x in range(10)]


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

    def get_quadrante_jogador(self, x, y):
        xx = self._dict_alphanum[x]
        return self._matrix2[xx][y-1]
    
    def get_quadrante_tela(self, x, y):
        return self._matrix2(x, y)

class Tabuleiro():
    
    _parte_a : TabuleiroParte = None
    _parte_b : TabuleiroParte = None
    
    def __init__(self):
        _parte_a = TabuleiroParte()
        _parte_b = TabuleiroParte()