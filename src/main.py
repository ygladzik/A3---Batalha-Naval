from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.controllers.jogador_controller import JogadorController
from src.models.partida import Partida
from src.models.tabuleiro import Tabuleiro, TabuleiroParte
from src.controllers.tabuleiro_controller import TabuleiroController

app = FastAPI()

@app.get("/")
async def lista_jogadores():
    return JogadorController.get_instance().lista_todos_os_jogadores()

@app.get("/top3")
async def ranking_top3():
    return JogadorController.get_instance().lista_ranking_top_3()
    
@app.get("/criar_partida")
async def criar_partida():
    id = str(Partida.get_novo_id())
    response = RedirectResponse(url='/entrar_partida/'+id)
    return response

@app.get("/entrar_partida/{id}")
async def get_tabuleiro():
    #byte = bytes(TabuleiroParte.get_tabuleiro(), 'utf-8')
    return TabuleiroParte.get_tabuleiro()

@app.patch("/entrar_partida/{id}/colocar/{x}/{y}/{barco}/{rot}")
async def set_tabuleiro_volta(x: int, y: int, emb: str, rot: int):
    TabuleiroParte.set_tabuleiro(emb, x, y, rot)
    response = RedirectResponse(url='/entrar_partida/{id}')
    return response

@app.get("/entrar_partida/{id}/atacar/{x}/{y}")
async def set_tabuleiro_atira_volta(x: int, y: int):
    TabuleiroParte.jogada(x, y)
    response = RedirectResponse(url='/entrar_partida/{id}')
    return response
