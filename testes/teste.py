import sqlite3


banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

variavel = "123"
cursor.execute(f"INSERT INTO pessoas (nome_razao_social,endereco,numero_casa,cpf_cnpj) VALUES ({variavel},'rua osvaldo marcondes barbosa','869','09186144901')")
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())

banco.commit()

banco.close()