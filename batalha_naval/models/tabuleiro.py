class TabuleiroParte():
    _x = None
    _y = None
    _tab = None

    def __init__(self):
        self._x = "ABCDEFGHIJ"
        self._y = range(10)
        self._tab = [["A" for x in range(10)] for x in self._y]

    def jogada(self, x, y):
        if x in self._x and y in self._y:
            xx = self._x.index(x)
            pos = self._tab[xx][y]

            match pos:
                case "A":
                    self._tab[xx][y] = "X"
                    return True
                case "X":
                    return False
            raise Exception("Tabuleiro com valor estranho")
        else:
            return False
            
    #_dict_alphanum = {
    #    "A" : 0,
    #    "B" : 1,
    #    "C" : 2,
    #    "D" : 3,
    #    "E" : 4,
    #    "F" : 5,
    #    "G" : 6,
    #    "H" : 7,
    #    "I" : 8,
    #    "J" : 9
    #}

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