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
    def cria_tabuleiro(cls):
        tab_linhas = []
        tab_colunas = []
        y=0
        for y in range(10):
            val = cls._tab._parte_a._tab[y]
            tab_colunas.append(''.join(val))
        tab_linhas.append(''.join(tab_colunas))
        return tab_linhas

    @classmethod
    def get_tabuleiro(self):
        lista = "".join(str(x) for x in self.get_instance().cria_tabuleiro())
        byte = bytes(lista, 'utf-8')
        return byte
    
    @classmethod
    def set_tabuleiro(cls, x: int, y: int, emb: str, rot: int) -> int:
        emb = cls._tab._parte_a._tab[x][y]
        if rot == "0":
            emb = cls._tab._parte_a._tab[x+1][y]
            emb = cls._tab._parte_a._tab[x-1][y]
            emb = cls._tab._parte_a._tab[x][y+1]
        elif rot == "1":
            emb = cls._tab._parte_a._tab[x][y+1]
            emb = cls._tab._parte_a._tab[x][y-1]
            emb = cls._tab._parte_a._tab[x-1][y]
        elif rot == "2":
            emb = cls._tab._parte_a._tab[x][y-1]
            emb = cls._tab._parte_a._tab[x-1][y]
            emb = cls._tab._parte_a._tab[x+1][y]
        elif rot == "3":
            emb = cls._tab._parte_a._tab[x][y-1]
            emb = cls._tab._parte_a._tab[x+1][y]
            emb = cls._tab._parte_a._tab[x][y+1]