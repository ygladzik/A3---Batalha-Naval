from batalha_naval.models.jogador import Jogador


def test_jogador_construtor():
    apelido = "Anderson"
    email ="ddd"
    senha = "ddd"
    idade = 98

    jogador = Jogador(apelido, email, senha, idade)

    assert jogador._apelido == apelido
    assert jogador._email == email
    assert jogador._senha == senha
    assert jogador._idade == idade
    assert jogador._pontuacao_acumulada == 0


def test_jogador_construtor_nome_vazio():
    apelido = None
    email ="ddd"
    senha = "ddd"
    idade = 94

    try:
        jogador = Jogador(apelido, email, senha, idade)
        assert False == "Construtor aceitou vazio"
    except Exception as err:
        assert err.args[0] == "Não pode nome vazio"

def test_jogador_construtor_email_vazio():
    apelido = "Anderson"
    email = None
    senha = "ddd"
    idade = 94

    try:
        jogador = Jogador(apelido, email, senha, idade)
        assert False == "Construtor aceitou vazio"
    except Exception as err:
        assert err.args[0] == "Não pode email vazio"

def test_jogador_construtor_senha_vazio():
    apelido = "Andersom"
    email ="ddd"
    senha = None
    idade = 94

    try:
        jogador = Jogador(apelido, email, senha, idade)
        assert False == "Construtor aceitou vazio"
    except Exception as err:
        assert err.args[0] == "Não pode senha vazia"


def test_jogador_constructor_idade_fora_do_limite():
    apelido = "Anderson"
    email = "ddd"
    senha = "ddd"
    idades = [-20, 121]

    # testando idades erradas
    for idade in idades:
        try:
            jogador = Jogador(apelido, email, senha, idade)
            assert False == "Construtor aceitou idade negativa"
        except Exception as err:
            assert err.args[0] == "Não pode idade fora da faixa"

    idades = [120, 8, 50]
    for idade in idades:
        jogador = Jogador(apelido, email, senha, idade)
        assert jogador._idade == idade


def test_jogador_pontuar():
    jogador = Jogador("test", "test", "test", 33)

    assert jogador._pontuacao == 0
    jogador.pontuar()
    assert jogador._pontuacao == 1
    jogador.pontuar()
    assert jogador._pontuacao == 2
