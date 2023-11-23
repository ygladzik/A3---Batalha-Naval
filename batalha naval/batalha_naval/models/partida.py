from batalha_naval.models.jogador import Jogador
from batalha_naval.models.tabuleiro import Tabuleiro


class Partida:

    _id : int

    _jogador_a : Jogador = None
    _jogador_b : Jogador = None

    _tabuleiro : Tabuleiro

    # ------ CONTADOR ESTÁTICO DE NÚMERO DE PARTIDAS ------
    __contador_id = 0

    @classmethod
    def get_novo_id(cls):
        cls.__contador_id = cls.__contador_id + 1
        return cls.__contador_id
    # -----------------------------------------------------

    def __init__(self, jogador1, jogador2):
        self._id = Partida.get_novo_id()
        self._jogador_a = jogador1
        self._jogador_b = jogador2
        self._tabuleiro = Tabuleiro()