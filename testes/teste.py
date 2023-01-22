'''import sqlite3

banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

cursor.execute(f"UPDATE planos SET status='ATIVO'")
cursor.execute(f"UPDATE tipos SET status='ATIVO'")
cursor.execute(f"UPDATE pagamentos SET status='ATIVO'")
cursor.execute(f"UPDATE sessoes SET status='ATIVO'")

banco.commit()

banco.close()
'''



