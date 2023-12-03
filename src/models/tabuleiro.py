class TabuleiroParte():
    _x = None
    _y = None
    #o próprio tabuleiro, repleto de A(Água) que pode ser alterado
    #conforme o jogo passa
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

    #alfabeto que transforma o int dado pelo barco em caracter que
    #será colocado no tabuleiro
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
            
#get_tabuleiro envia a matrix do tabuleiro para o navegador 
# do usuário quando requerido
    @classmethod
    def get_tabuleiro(self):
        lista = "".join(str(x) for x in self._tab)
        byte = bytes(lista, 'utf-8')
        return byte
    
#traduz o INT recebido do barco, para transformá-lo no formato
#que vai ser enviado pra matix do tabuleiro
    @classmethod
    def traduz_barco(self, emb):
        Barco = self._dict_alphanum[int(emb)]
        return Barco
    
#servia pra traduzir as lanes de "A" até "J", porém não consegui
#implementar a aceitação de str na URL
    def traduz_x(self, x):
        xx = self._dict_alphanam[x]
        return xx
        
#faz a jogada, ou seja, dispara a bomba no campo, com resultados
#diferentes para alvos diferentes, como por exemplo: se acertar
#um barco, deixará um "O", mas se acertar apenas a água, ficará 
#um "X"
    @classmethod
    def jogada(self, xx, yy):
        x = xx-1
        y = yy-1
        pos = self._tab[x][y]
        if xx >=0 <=9 and yy >=0 <=9:
            match pos:
                #se for água, marca com X
                case "A":
                    self._tab[x][y] = "X"
                    return True
                #se for uma embarcação, marca com O
                case "E":
                    self._tab[x][y] = "O"
                    return True
                #não permite atirar em um lugar que já foi disparado
                case "X":
                    return False
            raise Exception("Tabuleiro com valor estranho")
        else:
            return False

#método pra colocar os barcos na água, puxando a função de traduzir barco.
    @classmethod
    def set_tabuleiro(self, xx: int, yy: int, emb: int, rot: int) -> int:

        # TabuleiroParte.traduz_x(xx)
        embi = TabuleiroParte.traduz_barco(emb)
        #ajusta os números de 1 a 10 para 0 a 9
        y = yy-1
        x = xx-1
        posrot = rot

        if xx >=0 <=9 and yy >=0 <=9:
            #analisa qual é o espaço em que quer colocar seu barco
            pos = self._tab[x][y]
            match pos:
                #permite que o barco seja colocado
                case "A":
                    self._tab[x][y] = embi
                    #ifs e elifs que dizem pra qual direção o barco será
                    if posrot == 0:
                        self._tab[x+1][y] = embi
                        self._tab[x-1][y] = embi
                        self._tab[x][y+1] = embi
                    elif posrot == 1:
                        self._tab[x][y+1] = embi
                        self._tab[x][y-1] = embi
                        self._tab[x-1][y] = embi
                    elif posrot == 2:
                        self._tab[x][y-1] = embi
                        self._tab[x-1][y] = embi
                        self._tab[x+1][y] = embi
                    elif posrot == 3:
                        self._tab[x][y-1] = embi
                        self._tab[x+1][y] = embi
                        self._tab[x][y+1] = embi
                    else:
                        return False
                #impede que coloque um barco em cima de outro
                case "E":
                    return False
                case "M":
                    return False
                case "H":
                    return False
                case "L":
                    return False
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

    #pega um quadrante específico da matrix do tabuleiro,
    #mas como não foi utilizado, não mexemos

    def get_quadrante_jogador(self, x, y):
        xx = self._dict_alphanum[x]
        return self._matrix2[xx][y-1]

class Tabuleiro():
    
    _parte_a : TabuleiroParte = None
    _parte_b : TabuleiroParte = None
    
    def __init__(self):
        _parte_a = TabuleiroParte()
        _parte_b = TabuleiroParte()