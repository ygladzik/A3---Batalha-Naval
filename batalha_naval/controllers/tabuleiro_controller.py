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