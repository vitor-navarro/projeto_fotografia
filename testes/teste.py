'''import sqlite3

banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

cursor.execute(f"UPDATE pessoas SET status='ATIVO'")

banco.commit()

banco.close()
'''

from modulos.database import filtro_database_pessoas

filtro = "ATIV"

print(filtro_database_pessoas(filtro))






