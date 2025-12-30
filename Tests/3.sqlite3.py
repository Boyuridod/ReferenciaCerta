import sqlite3 as banco

bancoApp = banco.connect("geradorDeReferencias.db")

bancoApp.execute("""
    CREATE TABLE IF NOT EXISTS tema(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    );
""")

bancoApp.execute("""
    INSERT INTO tema (nome)
    VALUES ('dark'),
    ('light')
    ON CONFLICT (nome) DO NOTHING;
""")

bancoApp.execute("""
    CREATE TABLE IF NOT EXISTS configuracao(
        temaId INTEGER,
        ultimaTela text,
        FOREIGN KEY (temaId) REFERENCES tema(id)
    );
""")

bancoApp.execute("""
    INSERT INTO configuracao(temaID, ultimatela) VALUES (1, 'Inicial');
""")

config = bancoApp.execute("""
    SELECT * FROM tema;
""")

select = bancoApp.execute("""
    SELECT tema.nome, configuracao.ultimaTela FROM configuracao
    LEFT JOIN tema ON configuracao.temaId = tema.id;
""")

for row in select:
    print(row)

banco.close()