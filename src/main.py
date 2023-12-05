from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.controllers.jogador_controller import JogadorController
from src.models.partida import Partida
from src.models.tabuleiro import Tabuleiro, TabuleiroParte
from src.controllers.tabuleiro_controller import TabuleiroController
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


#página inicial, que mostra apenas a lista dos jogadores
@app.get("/")
async def lista_jogadores():
    return JogadorController.get_instance().lista_todos_os_jogadores()

#página que mostra o Top 3 de jogadores com maior pontuação
@app.get("/top3")
async def ranking_top3():
    return JogadorController.get_instance().lista_ranking_top_3()

#cria a sua partida, gerando um id novo a ela e te redirecionando 
#para a mesma
@app.get("/criar_partida")
async def criar_partida():
    id = str(Partida.get_novo_id())
    response = RedirectResponse(url='/entrar_partida/'+id)
    return response

#onde a sua partida acontece, lhe mostrando o tabuleiro atual
@app.get("/entrar_partida/{id}")
async def get_tabuleiro():
    #byte = bytes(TabuleiroParte.get_tabuleiro(), 'utf-8')
    return TabuleiroParte.get_tabuleiro()

#envia informações pro tabuleiro sobre onde sua embarcação ficará
#e te leva de volta para a URL anterior, lhe entregando o tabuleiro
@app.get("/entrar_partida/{id}/colocar/{x}/{y}/{emb}/{rot}")
async def set_tabuleiro_volta(x: int, y: int, emb: str, rot: int):
    TabuleiroParte.set_tabuleiro(x, y, emb, rot)
    response = RedirectResponse(url='/entrar_partida/{id}')
    return response

#envia a informação de onde seu tiro vai, acertando um local e
#lhe enviando de volta a URL anterior, lhe entregando o tabuleiro
@app.get("/entrar_partida/{id}/atacar/{x}/{y}")
async def set_tabuleiro_atira_volta(x: int, y: int):
    TabuleiroParte.jogada(x, y)
    response = RedirectResponse(url='/entrar_partida/{id}')
    return response


# Configuração do middleware CORS para permitir solicitações da origem do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)