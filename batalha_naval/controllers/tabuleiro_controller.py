from batalha_naval.models.tabuleiro import Tabuleiro

class TabuleiroController():

    _instance = None
    _tab = Tabuleiro()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TabuleiroController()
        return cls._instance

    @classmethod
    def get_tabuleiro(self):
        lista = "".join(str(x) for x in self.get_instance()._tab._parte_a._tab)
        byte = bytes(lista, 'utf-8')
        return byte
    
    def traduz_barco(self, Barco):
        Barco = self._tab._parte_a._dict_alphanum[Barco]
        return Barco
    
    def traduz_x(self, x):
        xx = self._tab._parte_a._dict_alphanam[x]
        return xx

    @classmethod
    def set_tabuleiro(self, xx: int, yy: int, Barco: int, rot: int) -> int:
            
        # TabuleiroParte.traduz_x(xx)
        Birco = TabuleiroController.traduz_barco(self, Barco)
        yy = yy-1
        xx = xx-1
        posrot = rot

        if xx >=0 <=9 and yy >=0 <=9:
            pos = self._tab._parte_a._tab[xx][yy]
            match pos:
                case "A":
                    self._tab._parte_a._tab[xx][yy] = Birco
                    if posrot == 0:
                        self._tab._parte_a._tab[xx+1][yy] = Birco
                        self._tab._parte_a._tab[xx-1][yy] = Birco
                        self._tab._parte_a._tab[xx][yy+1] = Birco
                    elif posrot == 1:
                        self._tab._parte_a._tab[xx][yy+1] = Birco
                        self._tab._parte_a._tab[xx][yy-1] = Birco
                        self._tab._parte_a._tab[xx-1][yy] = Birco
                    elif posrot == 2:
                        self._tab._parte_a._tab[xx][yy-1] = Birco
                        self._tab._parte_a._tab[xx-1][yy] = Birco
                        self._tab._parte_a._tab[xx+1][yy] = Birco
                    elif posrot == 3:
                        self._tab._parte_a._tab[xx][yy-1] = Birco
                        self._tab._parte_a._tab[xx+1][yy] = Birco
                        self._tab._parte_a._tab[xx][yy+1] = Birco
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
        
    @classmethod
    def jogada(self, xx, yy):
        pos = self._tab._parte_a._tab[xx][yy]
        if xx >=0 <=9 and yy >=0 <=9:
            match pos:
                case "A":
                    self._tab._parte_a._tab[xx][yy] = "X"
                    return True
                case "E":
                    self._tab._parte_a._tab[xx][yy] = "O"
                    return True
                case "X":
                    return False
            raise Exception("Tabuleiro com valor estranho")
        else:
            return False