import sqlite3


banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

#tabela pessoas, tipo será modificado e criado 2 tipos de tabelas diferentes uma para pessoa fisica e outra juridica
cursor.execute("CREATE TABLE pessoas (id INTEGER PRIMARY KEY,"
               "data_cadastro text,"
               "nome_razao_social text,"
               "status text,"
               "tipo text,"
               "cpf_cnpj text,"
               "apelido_fantasia text,"
               "rg_inscricao_estadual text,"
               "data_nascimento text,"
               "endereco text,"
               "numero_casa text,"
               "complemento text,"
               "bairro text,"
               "cidade text,"
               "cep text,"
               "uf text,"
               "fone1 text,"
               "operadora1 text,"
               "fone2 text,"
               "operadora2 text,"
               "fone3 text,"
               "operadora3 text,"
               "email text,"
               "anotacoes text,"
               "familia_pai text,"
               "familia_mae text,"
               "familia_conjuge text,"
               "emprego text)")

cursor.execute("INSERT INTO pessoas (nome_razao_social,endereco,numero_casa,cpf_cnpj,fone1) VALUES ('vitor','rua osvaldo marcondes barbosa','869','09186144901','(44)988389141')")
cursor.execute("INSERT INTO pessoas (nome_razao_social,endereco,numero_casa,cpf_cnpj,fone1) VALUES ('TESTE','Testea','869','09186144901','(44)988389141')")
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())


#tabela planos
cursor.execute("CREATE TABLE planos(id INTEGER PRIMARY KEY,"
               "nome_plano text,"
               "quantidade_fotos int,"
               "valor REAL,"
               "valor_foto_extra REAL,"
               "descricao text,"
               "data_criacao text,"
               "status text)")

# OBS produto extra será um objeto produto com valor e descricao ou até mesmo fará referencia a outra tabela

cursor.execute("INSERT INTO planos (nome_plano, quantidade_fotos,valor,valor_foto_extra,descricao) VAlUES ('plano B',20,299.99,20.00,'plano Intemediario')")
cursor.execute("SELECT * FROM planos")
print(cursor.fetchall())

cursor.execute("CREATE TABLE tipos(id INTEGER PRIMARY KEY,"
               "nome_tipo text,"
               "descricao text,"
               "data_criacao text,"
               "status text)")

cursor.execute("INSERT INTO tipos (nome_tipo, descricao) VAlUES ('Gestante','plano para gestantes')")
cursor.execute("SELECT * FROM tipos")
print(cursor.fetchall())
#tabela pagamentos
cursor.execute("CREATE TABLE pagamentos (id INTEGER PRIMARY KEY,"
               "pessoa INTEGER,"
               "valor_pago REAL,"
               "tipo_pagamento text,"
               "descricao_extra text,"
               "data_pagamento text,"
               "status text,"
               "FOREIGN KEY (pessoa) REFERENCES pessoas(id))")

cursor.execute("INSERT INTO pagamentos (pessoa,valor_pago,tipo_pagamento,descricao_extra,data_pagamento) VAlUES (1,199.00,'cartao','teste','27/10/2022')")
cursor.execute("SELECT * FROM pagamentos")
print(cursor.fetchall())

#tabela sessoes
cursor.execute("CREATE TABLE sessoes (id INTEGER PRIMARY KEY,"
               "pessoa_sessao INTEGER,"
               "nome_pessoa text,"
               "id_tipo INTEGER,"
               "tipo text,"
               "plano_contratado INTEGER,"
               "plano_nome text,"
               "data text,"
               "hora text,"
               "produto_extra text,"
               "etapa_atual text,"
               "pagamento1 text,"
               "valor_pagamento1 float,"
               "pagamento2 text,"
               "valor_pagamento2 float,"
               "pagamento3 text,"
               "valor_pagamento3 float,"
               "total_pagamentos text,"
               "observasoes text,"
               "data_cadastro text,"
               "quantidade_foto_extra text,"
               "valor_foto_extra text,"
               "status text,"
               "FOREIGN KEY (pessoa_sessao) REFERENCES pessoas(id),"
               "FOREIGN KEY (id_tipo) REFERENCES tipos(id),"
               "FOREIGN KEY (plano_contratado) REFERENCES planos(id))")
#OBS pagamentos vai ter que mudar o jeito que está sendo construido, tem de ser uma lista de referencias a pagamentos, o sqlite não suporta isso
#OBS2 Quando for aparecera a condicao de parcelamento vai aparecer como a vista dinheiro,a vista debito, 12x credito, a vista credito


cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
banco.commit()

banco.close()