from src.models.jogador import Jogador
from src.data.db_config import ConfigDB
import sqlite3


class JogadorDB():

    FONTE_DOS_DADOS = "jogadores.dat"

    _lista_de_jogadores = []

    #cria uma lista com todas os jogadores presentes no banco de dados
    def popula_do_banco(self):
            # lê do banco de dados
            with sqlite3.connect("batalha_banco.sqlite") as conn:
                cursor = conn.cursor()
                res = cursor.execute("SELECT id, apelido, email, senha, pontuacao, idade FROM Jogadores")
                for r in res:
                    j = Jogador(
                        apelido=r[1],
                        email=r[2],
                        senha=r[3],
                        idade=r[5]
                    )
                    j._pontuacao_acumulada = r[4]
                    self._lista_de_jogadores.append(j)

    #puxa a função que popula automaticamente
    def __init__(self):
            self.popula_do_banco()

    #função que retorna a lista já populada
    def lista_todos_os_jogadores(self):
            return self._lista_de_jogadores
    
    #função que adiciona jogadores ao banco    
    def inserir_jogador_no_banco(self, jogador: Jogador):
        sqlite_insert = """INSERT INTO Jogadores (apelido, email, pontuacao, senha, idade) VALUES (?, ?, ?, ?, ?);"""
        val =  (jogador._apelido, jogador._email, jogador._pontuacao_acumulada, jogador._senha, jogador._idade)
        ConfigDB(sqlite_insert, val)