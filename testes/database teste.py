import sqlite3


banco = sqlite3.connect("database.db")

cursor = banco.cursor()
'''
#tabela pessoas
cursor.execute("CREATE TABLE pessoas (id_pessoa INTEGER PRIMARY KEY,"
               "nome_razao_social text,"
               "apelido_fantasia text,"
               "endereco text,"
               "numero_casa text,"
               "complemento text,"
               "bairro text,"
               "cidade text,"
               "cep text,"
               "data_nascimento text,"
               "fone1 text,"
               "fone2 text,"
               "tipo text,"
               "cpf_cnpj text,"
               "rg_inscricao_estadual text,"
               "data_cadastro text,"
               "email text,"
               "anotacoes text,"
               "familia_pai text,"
               "familia_mae text,"
               "familia_conjuge text,"
               "emprego text)")

cursor.execute("INSERT INTO pessoas (nome_razao_social,endereco,numero_casa,cpf_cnpj) VALUES ('vitor','rua osvaldo marcondes barbosa','869','09186144901')")
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())


#tabela planos
cursor.execute("CREATE TABLE planos (id_plano INTEGER PRIMARY KEY,"
               "nome_plano text,"
               "quantidade_fotos int,"
               "valor REAL,"
               "valor_foto_extra REAL,"
               "descricao text,"
               "data_criacao text)")

# OBS produto extra será um objeto produto com valor e descricao ou até mesmo fará referencia a outra tabela

cursor.execute("INSERT INTO planos (nome_plano, quantidade_fotos,valor,valor_foto_extra,descricao) VAlUES ('plano B',20,299.99,20.00,'plano Intemediario')")
cursor.execute("SELECT * FROM planos")
print(cursor.fetchall())'''
'''
#tabela pagamentos
cursor.execute("CREATE TABLE pagamentos (id_sessao INTEGER PRIMARY KEY,"
               "pessoa INTEGER,"
               "valor_pago REAL,"
               "tipo_pagamento text,"
               "descricao_extra text,"
               "data_pagamento text,"
               "FOREIGN KEY (pessoa) REFERENCES pessoas(id_pessoa))")

cursor.execute("INSERT INTO pagamentos (pessoa,valor_pago,tipo_pagamento,descricao_extra,data_pagamento) VAlUES (1,199.00,'cartao','teste','27/10/2022')")
cursor.execute("SELECT * FROM pagamentos")
print(cursor.fetchall())
'''
'''
#tabela sessoes
cursor.execute("CREATE TABLE sessoes (id_sessao INTEGER PRIMARY KEY,"
               "pessoa_sessao INTEGER,"
               "plano_contratado INTEGER,"
               "produto_extra text,"
               "pagamento text,"
               "condicao_pagamento text,"
               "FOREIGN KEY (pessoa_sessao) REFERENCES pessoas(id_pessoa),"
               "FOREIGN KEY (plano_contratado) REFERENCES planos(id_plano))")
#OBS pagamentos vai ter que mudar o jeito que está sendo construido, tem de ser uma lista de referencias a pagamentos, o sqlite não suporta isso


cursor.execute("INSERT INTO sessoes (pessoa_sessao,plano_contratado,produto_extra,pagamento,condicao_pagamento) VAlUES (1,1,'batatas','1/2','3 vezes')")
cursor.execute("SELECT * FROM sessoes")
print(cursor.fetchall())
'''

banco.commit()