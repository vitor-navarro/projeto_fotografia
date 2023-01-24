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

#tabela planos
cursor.execute("CREATE TABLE planos(id INTEGER PRIMARY KEY,"
               "nome_plano text,"
               "quantidade_fotos int,"
               "valor REAL,"
               "valor_foto_extra REAL,"
               "descricao text,"
               "data_criacao text,"
               "status text)")

cursor.execute("CREATE TABLE tipos(id INTEGER PRIMARY KEY,"
               "nome_tipo text,"
               "descricao text,"
               "data_criacao text,"
               "status text)")

#tabela pagamentos
cursor.execute("CREATE TABLE pagamentos (id INTEGER PRIMARY KEY,"
               "pessoa INTEGER,"
               "valor_pago REAL,"
               "tipo_pagamento text,"
               "descricao_extra text,"
               "data_pagamento text,"
               "status text,"
               "FOREIGN KEY (pessoa) REFERENCES pessoas(id))")

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

banco.commit()

banco.close()