from fastapi import FastAPI
from batalha_naval.controllers.jogador_controller import JogadorController

app = FastAPI()

# token => https://en.wikipedia.org/wiki/JSON_Web_Token
@app.get("/partida/{id_partida}/tabuleiro")
async def get_tabuleiro(token, id_partida):
    pass

@app.get("/")
async def lista_jogadores():
    return JogadorController.get_instance().lista_todos_os_jogadores()

@app.get("/top3")
async def ranking_top3():
    return JogadorController.get_instance().lista_ranking_top_3()