import sqlite3

banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

cadastro_valor ="10/11/2022"
nome_razao_social = "VITOR LUIZ DOS SANTOS NAVARRO"
id = 4

cursor.execute(f"UPDATE pessoas SET data_cadastro = ?,nome_razao_social=? WHERE id = ?",(cadastro_valor,nome_razao_social, id))
print(cursor.fetchall())
banco.commit()

banco.close()
