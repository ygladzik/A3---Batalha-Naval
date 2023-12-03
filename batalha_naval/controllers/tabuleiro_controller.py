from batalha_naval.models.tabuleiro import Tabuleiro

class TabuleiroController():

    _instance = None
    _tab = Tabuleiro()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = TabuleiroController()
        return cls._instance