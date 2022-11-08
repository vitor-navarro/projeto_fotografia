import sqlite3


banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

cursor.execute("CREATE TABLE sessoes (id INTEGER PRIMARY KEY,"
               "pessoa_sessao INTEGER,"
               "pessoa_extra text,"
               "tipo text,"
               "plano_contratado INTEGER,"
               "data text,"
               "hora text"
               "lote text,"
               "produto_extra text,"
               "estapa_atual text"
               "pagamento text,"
               "condicao_pagamento text,"
               "FOREIGN KEY (pessoa_sessao) REFERENCES pessoas(id),"
               "FOREIGN KEY (plano_contratado) REFERENCES planos(id))")

banco.commit()

banco.close()