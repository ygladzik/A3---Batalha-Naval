from batalha_naval.data.jogador_db import JogadorDB

class JogadorController:

    _instance = None
    _db = None

    def __init__(self):
        self._db = JogadorDB()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = JogadorController()
        return cls._instance
    
    def lista_todos_os_jogadores(self):
        return self._db.lista_todos_os_jogadores()
    
    def lista_ranking_top_3(self):
        jogadores = self._db.lista_todos_os_jogadores()
        
        # on the fly (em tempo de execução)
        jogadores_dto = []
        for jogador in jogadores:

            # jogador_simplificado = { }
            # jogador_simplificado["apelido"] = jogador._apelido

            jogadores_dto.append({
                "apelido": jogador._apelido,
                "pontuacao": int(jogador._pontuacao_acumulada)
            })

        def criterio(jogador_dto):
            return - jogador_dto["pontuacao"]

        # ordenar o vetor, do maior ao menor, pelo score
        v_ordenado = sorted(jogadores_dto, key=criterio)

        # DTO => data transfer object
        return v_ordenado[:3]   # syntax sugar

