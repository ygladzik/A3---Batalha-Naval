import sqlite3 

arquivo_banco = "batalha_naval.db"

sql_create_table_frutas = '''
    CREATE TABLE Frutas(
        id INTEGER,
        nome TEXT,
        PRIMARY KEY(id)
    );
'''

sql_popula_table_frutas = [
    "INSERT INTO Frutas (id, nome) VALUES (1, 'Banana');",
    "INSERT INTO Frutas (id, nome) VALUES (2, 'Maçã');",
    "INSERT INTO Frutas (id, nome) VALUES (3, 'Pêra');",
    "INSERT INTO Frutas (id, nome) VALUES (4, 'Melancia');",
    "INSERT INTO Frutas (id, nome) VALUES (5, 'Abacaxi');",
    "INSERT INTO Frutas (id, nome) VALUES (6, 'Cereja');",
    "INSERT INTO Frutas (id, nome) VALUES (7, 'Romã');",
    "INSERT INTO Frutas (id, nome) VALUES (8, 'Carambola');"
]

# default 0
sql_create_table_jogador = '''
    CREATE TABLE Jogadores(
        id INTEGER,
        pontuacao INTEGER,
        nome TEXT,
        email TEXT,
        senha TEXT,
        PRIMARY KEY(id)
    );
'''

def executa_sql(codigo_sql):
    with sqlite3.connect(arquivo_banco) as conn:
        try:
            cursor = conn.cursor()
            res = cursor.execute(codigo_sql)
        except sqlite3.Error as e:
            print(e)

sql_popula_table_jogadores = [
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (0, 'Leandro Silva',200; 'll@gmail.com', '!@$%$#5%');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (1, 'Arnaldo', 3566, 'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (2, 'Arnaldo', 346,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (3, 'Arnaldo', 897,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (4, 'Arnaldo', 689,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (5, 'Arnaldo', 123,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (6, 'Arnaldo', 456,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (7, 'Arnaldo', 678,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (8, 'Arnaldo', 901,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (9, 'Arnaldo', 580,  'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (10, 'Arnaldo', 1220, 'arnaldinho@hotmail.com','!#%$¨@!');",
    "INSERT INTO Jogadores (id, nome, pontuacao, email, senha) VALUES (11, 'Arnaldo', 570,  'arnaldinho@hotmail.com','!#%$¨@!');"
]
# Cria a tabela frutas
executa_sql(sql_create_table_frutas)

# Popula a tabela Frutas
for x in sql_popula_table_frutas:
    executa_sql(x)

# cria tabela jogador
executa_sql(sql_create_table_jogador)

# Popula a tabela jogadores 
for x in sql_popula_table_jogadores:
    executa_sql(x)



