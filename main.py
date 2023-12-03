from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from batalha_naval.controllers.jogador_controller import JogadorController
from batalha_naval.models.partida import Partida
from batalha_naval.models.tabuleiro import Tabuleiro, TabuleiroParte
from batalha_naval.controllers.tabuleiro_controller import TabuleiroController

app = FastAPI()

@app.get("/")
async def lista_jogadores():
    return JogadorController.get_instance().lista_todos_os_jogadores()

@app.get("/top3")
async def ranking_top3():
    return JogadorController.get_instance().lista_ranking_top_3()

# token => https://en.wikipedia.org/wiki/JSON_Web_Token
@app.get("/criar_partida")
async def criar_partida():
    id = str(Partida.get_novo_id())
    response = RedirectResponse(url='/sua_partida/'+id)
    return response

@app.get("/sua_partida/{id}")
async def get_tabuleiro():
    return JogadorController.get_instance().lista_ranking_top_3()
# async def get_tabuleiro():
#     x = 0
#     y = 0
#     for x in range(10):
#         for y in range(10):
#             TabuleiroParte.get_quadrante_tela(x, y)

@app.get("entrar_partida/{id}")
async def get_tabuleiro():
    return JogadorController.get_instance().lista_ranking_top_3()

@app.get("/entrar_partida/{id}/colocar/{x}/{y}/{barco}/{rot}")
async def set_tabuleiro_volta(x: int, y: int, barco: int, rot: int):
    TabuleiroController.set_tabuleiro(x, y, barco, rot)
    response = RedirectResponse(url='/entrar_partida/{id}')
    return response

@app.get("/entrar_partida/{id}/atacar/{x}/{y}")
async def set_tabuleiro_atira_volta(x: int, y: int):
    TabuleiroController.jogada(x, y)
    response = RedirectResponse(url='/entrar_partida/{id}')
    return response