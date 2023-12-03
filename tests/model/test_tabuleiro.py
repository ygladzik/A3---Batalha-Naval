#from batalha_naval.models.tabuleiro import TabuleiroParte

#__x = ["A" for x in range(10)]
#__y = range(10)


#def test_parte_tabuleiro_construtor():
    #tabuleiro_parte = TabuleiroParte()
    #assert tabuleiro_parte._x == "ABCDEFGHIJ"
    #assert tabuleiro_parte._y == __y

    #tab_esperado = [__x for x in __y]

    #assert tabuleiro_parte._tab == tab_esperado


#def test_tabuleiro_jogada():
    #tabuleiro = TabuleiroParte()

    #for x in "ABCDEFGHIJ":
        #for y in __y:
        #    assert tabuleiro.jogada(x, y)


#def test_tabuleiro_jogadas_erradas():
#    tabuleiro_parte = TabuleiroParte()

#    assert tabuleiro_parte.jogada("K", 1) == False
#    assert tabuleiro_parte.jogada("L", 1) == False
#    assert tabuleiro_parte.jogada("A", -1) == False
#    assert tabuleiro_parte.jogada("A", 10) == False


# este teste ....
# caso aconteça de...
# então...
#def test_tabuleiro_parte_jogadas_consecutivas():
#    tabuleiro_parte = TabuleiroParte()
#
#    assert tabuleiro_parte._tab[1][8] == "A"
#    assert tabuleiro_parte.jogada("B", 8) == True
#    assert tabuleiro_parte._tab[1][8] == "X"
#    assert tabuleiro_parte.jogada("B", 8) == False
#    assert tabuleiro_parte._tab[1][8] == "X"
#    assert tabuleiro_parte.jogada("B", 8) == False
#  assert tabuleiro_parte._tab[1][8] == "X"
