from batalha_naval.models.jogador import Jogador
from batalha_naval.data.db_config import ConfigDB
import sqlite3


class JogadorDB():

    FONTE_DOS_DADOS = "jogadores.dat"

    _lista_de_jogadores = []

def popula_do_banco(self):
         # lê do banco de dados
         with sqlite3.connect("batalha_banco.sqlite") as conn:
             cursor = conn.cursor()
             res = cursor.execute("SELECT id, apelido, email, senha, pontuacao FROM Jogadores")
             for r in res:
                 j = Jogador(
                     apelido=r[1],
                     email=r[2],
                     senha=r[3]
                 )
                 j._pontuacao_acumulada = r[4]
                 self._lista_de_jogadores.append(j)
#
    #def popula_do_arquivo(self):
    #    with open(self.FONTE_DOS_DADOS) as f:
    #            linhas = f.readlines()
    #            for linha in linhas:
    #                # trim() -> remove espaços no início e final da string
    #                # no python, trim se chama "strip"
    #                if linha.strip() != "":
    #                    print(linha)
    #                    v = linha.replace("\n","").split(";")
    #                    j = Jogador(v[0], v[2], v[3])
    #                    j._pontuacao_acumulada = v[1]
    #                    self._lista_de_jogadores.append(j)
#
def __init__(self):
           self.popula_do_banco()
#
def lista_todos_os_jogadores(self):
        return self._lista_de_jogadores