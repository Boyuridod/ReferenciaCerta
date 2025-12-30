import sqlite3 as sqlite

def criaBanco():
    banco = sqlite.connect("referenciaCerta.db")

    banco.execute("""
        CREATE TABLE IF NOT EXISTS dados(
            id INTEGER PRIMARY KEY CHECK (id = 1),
            tela_atual TEXT,
            texto_atual TEXT,
            texto_anterior TEXT
        );
    """)

    banco.close()

def salvaEstado(tela, textoAtual):
    banco = sqlite.connect("referenciaCerta.db")

    banco.execute("""
    UPDATE dados
    SET tela_atual = ?, texto_atual = ?
    WHERE id = 1
    """, (tela, textoAtual))

    banco.close()

def apagarReferencias(referencias):
    banco = sqlite.connect("referenciaCerta.db")

    banco.execute("""
    UPDATE dados
    SET texto_atual = ?, texto_anterior = ?
    WHERE id = 1
    """, ("", referencias))

    banco.close()

def recuperar():

    banco = sqlite.connect("referenciaCerta.db")

    referencias = banco.execute("""
        SELECT texto_anterior
        FROM dados
        WHERE id = 1
    """).fetchone()

    banco.close()

    print(referencias)

    if(referencias != None):
        return referencias + "\n\n"
    else:
        return ""