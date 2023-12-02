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

    @classmethod
    def jogada(self, xx, yy):
        pos = self._tab[xx][yy]
        if xx >=0 <=9 and yy >=0 <=9:
            match pos:
                case "A":
                    self._tab[xx][yy] = "X"
                    return True
                case "E":
                    self._tab[xx][yy] = "O"
                    return True
                case "X":
                    return False
            raise Exception("Tabuleiro com valor estranho")
        else:
            return False
            
    def traduz_barco(self, Barco):
        Barco = self._dict_alphanum[Barco]
        return Barco
    
    def traduz_x(self, x):
        xx = self._dict_alphanam[x]
        return xx

    @classmethod
    def set_tabuleiro(self, xx: int, yy: int, Barco: int, rot: int) -> int:
            
        # TabuleiroParte.traduz_x(xx)
        Birco = TabuleiroParte.traduz_barco(self, Barco)
        yy = yy-1
        xx = xx-1
        posrot = rot

        if xx >=0 <=9 and yy >=0 <=9:
            pos = self._tab[xx][yy]
            match pos:
                case "A":
                    self._tab[xx][yy] = Birco
                    if posrot == 0:
                        self._tab[xx+1][yy] = Birco
                        self._tab[xx-1][yy] = Birco
                        self._tab[xx][yy+1] = Birco
                    elif posrot == 1:
                        self._tab[xx][yy+1] = Birco
                        self._tab[xx][yy-1] = Birco
                        self._tab[xx-1][yy] = Birco
                    elif posrot == 2:
                        self._tab[xx][yy-1] = Birco
                        self._tab[xx-1][yy] = Birco
                        self._tab[xx+1][yy] = Birco
                    elif posrot == 3:
                        self._tab[xx][yy-1] = Birco
                        self._tab[xx+1][yy] = Birco
                        self._tab[xx][yy+1] = Birco
                    else:
                        return False
                case "E":
                    return False
                case "M":
                    return False
                case "H":
                    return False
                case "L":
                    return False
            raise Exception("Tabuleiro com valor estranho")
        else:
            raise Exception("Coordenadas inválidas")

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