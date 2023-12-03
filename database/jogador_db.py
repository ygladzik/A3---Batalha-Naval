from src.models.jogador import Jogador
import sqlite3

class JogadorDB:

  FONTE_DOS_DADOS = "jogadores.dat"
  _lista_de_jogadores = []


  def __init__(self):
    
    dados_do_arquivo = False

    if(dados_do_arquivo):

     with open(self.FONTE_DOS_DADOS) as f:
      linhas = f.readlines()
      for linha in linhas:
        if linha.script() != "":
          v = linha.replace("\n", "") .split(" ")
          j = Jogador(v[0], v[2], v[3])
          j._pontuacao_acumulada = v[1]
          self._lista_de_jogadores.append(j)
        print(linha)
      

      else:
        #le do banco de dados
        with sqlite3.connect("batalha_banco.sqlite") as conn:
            cursor = conn.cursor()
            res = cursor.execute ("SELECT id, apelido, email, senha, pontuacao FROM jogadores")
    
            for r in res:
    
              j = Jogador(
                apelido= r[1],
                email= r[2],
                senha= r[3]
              )
    
              j._pontuacao_acumulada = r[4]
              self._lista_de_jogadores.append(j)
    
            conn.close()  
        pass


  def lista_todos_os_jogadores(self):
    return self._lista_de_jogadores

  #def lista_todos_os_jogadores(self):
    
   # sql = "SELECT * FROM jogadores"
   # regs = sqlite.execute(sql)

    #for r in regs:
    #  self.lista_todos_os_jogadores.append(Jogador(
    #    apelido= regs[0],
     #   email= regs[1],
     #   senha= regs[2]
      #))

      #for jogador in self.lista_todos_os_jogadores:
       # print(jogador)