import sqlite3

def conecta_db():
    banco = sqlite3.connect("../modulos/database.db")
    cursor = banco.cursor()

    return banco, cursor

def pega_ultimo_id(nome_banco):
    banco,cursor = conecta_db()

    cursor.execute(f"SELECT id FROM {nome_banco}")
    lista = cursor.fetchall()
    if len(lista) != 0:
        ultimo = str(lista[len(lista)-1])
        ultimo_replace = ultimo.replace("(","")
        ultimo_replace = ultimo_replace.replace(")","")
        ultimo_replace = ultimo_replace.replace(",","")
        ultimo_replace = str(int(ultimo_replace)+1)
        desconecta_db(banco)
        return ultimo_replace
    else:
        desconecta_db(banco)
        return "0"


def grava_db_pessoa(entry_codigo_valor,entry_cadastro_valor,cb_status_valor,cb_tipo_valor,entry_cpf_cnpj_valor,entry_rg_inscricao_valor,ventry_nascimento_valor,
                                       entry_nome_valor,entry_apelido_valor,entry_endereco_valor,entry_complemento_valor,entry_bairro_valor,entry_nome_cidade_valor,entry_uf_valor,
                                       entry_cep_valor,entry_fone1_valor,entry_fone2_valor,entry_fone3_valor,entry_operadora1_valor,entry_operadora2_valor,
                                       entry_operadora3_valor,entry_email_valor,entry_numero):

    cadastro_valor = entry_cadastro_valor()
    status_valor = cb_status_valor()
    tipo_valor = cb_tipo_valor()
    cpf_cnpj_valor = entry_cpf_cnpj_valor()
    rg_inscricao_valor = entry_rg_inscricao_valor()
    nascimento_valor = ventry_nascimento_valor()
    nome_valor = entry_nome_valor()
    apelido_valor = entry_apelido_valor()
    endereco_valor = entry_endereco_valor()
    complemento_valor = entry_complemento_valor()
    bairro_valor = entry_bairro_valor()
    nome_cidade_valor = entry_nome_cidade_valor()
    uf_valor = entry_uf_valor()
    cep_valor = entry_cep_valor()
    fone1_valor = entry_fone1_valor()
    fone2_valor = entry_fone2_valor()
    fone3_valor = entry_fone3_valor()
    operadora1_valor = entry_operadora1_valor()
    operadora2_valor = entry_operadora2_valor()
    operadora3_valor = entry_operadora3_valor()
    email_valor = entry_email_valor()
    numero_casa_valor = entry_numero()

    banco, cursor = conecta_db()

    cursor.execute(f"INSERT INTO pessoas (data_cadastro, nome_razao_social, status, tipo,cpf_cnpj, apelido_fantasia,rg_inscricao_estadual, data_nascimento, endereco, numero_casa, complemento,bairro, cidade, cep, uf,fone1, operadora1, fone2, operadora2, fone3, operadora3, email) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(cadastro_valor,nome_valor,status_valor,tipo_valor,cpf_cnpj_valor,apelido_valor,rg_inscricao_valor,nascimento_valor,endereco_valor,numero_casa_valor,complemento_valor,bairro_valor,nome_cidade_valor,cep_valor,uf_valor,fone1_valor,operadora1_valor,fone2_valor,operadora2_valor,fone3_valor,operadora3_valor,email_valor))
    cursor.execute("select * from pessoas")
    print(cursor.fetchall())
    banco.commit()

    desconecta_db(banco)

def altera_db_pessoa(entry_codigo_valor,entry_cadastro_valor,cb_status_valor,cb_tipo_valor,entry_cpf_cnpj_valor,entry_rg_inscricao_valor,ventry_nascimento_valor,
                                       entry_nome_valor,entry_apelido_valor,entry_endereco_valor,entry_complemento_valor,entry_bairro_valor,entry_nome_cidade_valor,entry_uf_valor,
                                       entry_cep_valor,entry_fone1_valor,entry_fone2_valor,entry_fone3_valor,entry_operadora1_valor,entry_operadora2_valor,
                                       entry_operadora3_valor,entry_email_valor,entry_numero):

    id = entry_codigo_valor()
    cadastro_valor = entry_cadastro_valor()
    status_valor = cb_status_valor()
    tipo_valor = cb_tipo_valor()
    cpf_cnpj_valor = entry_cpf_cnpj_valor()
    rg_inscricao_valor = entry_rg_inscricao_valor()
    nascimento_valor = ventry_nascimento_valor()
    nome_valor = entry_nome_valor()
    apelido_valor = entry_apelido_valor()
    endereco_valor = entry_endereco_valor()
    complemento_valor = entry_complemento_valor()
    bairro_valor = entry_bairro_valor()
    nome_cidade_valor = entry_nome_cidade_valor()
    uf_valor = entry_uf_valor()
    cep_valor = entry_cep_valor()
    fone1_valor = entry_fone1_valor()
    fone2_valor = entry_fone2_valor()
    fone3_valor = entry_fone3_valor()
    operadora1_valor = entry_operadora1_valor()
    operadora2_valor = entry_operadora2_valor()
    operadora3_valor = entry_operadora3_valor()
    email_valor = entry_email_valor()
    numero_casa_valor = entry_numero()

    banco, cursor = conecta_db()

    cursor.execute(f"UPDATE pessoas SET data_cadastro = ?, nome_razao_social=?, status = ?, tipo=?,cpf_cnpj=?, apelido_fantasia=?,rg_inscricao_estadual=?, data_nascimento=?, endereco=?, numero_casa=?, complemento=?,bairro=?, cidade=?, cep=?, uf=?,fone1=?, operadora1=?, fone2=?, operadora2=?, fone3=?, operadora3=?, email=? WHERE id = ?",(cadastro_valor,nome_valor,status_valor,tipo_valor,cpf_cnpj_valor,apelido_valor,rg_inscricao_valor,nascimento_valor,endereco_valor,numero_casa_valor,complemento_valor,bairro_valor,nome_cidade_valor,cep_valor,uf_valor,fone1_valor,operadora1_valor,fone2_valor,operadora2_valor,fone3_valor,operadora3_valor,email_valor,id))
    cursor.execute("select * from pessoas")
    print(cursor.fetchall())
    banco.commit()

    desconecta_db(banco)

def deleta_db_pessoa(id):
    banco, cursor = conecta_db()
    cursor.execute(f"DELETE FROM pessoas WHERE id = ?", (str(id),))

    banco.commit()

    desconecta_db(banco)
def pega_todas_pessoas_lista():

    banco, cursor = conecta_db()
    #retorna em ordem alfabética, modificar isso com as filtragens
    lista_db = cursor.execute("SELECT id, nome_razao_social,cpf_cnpj,cidade FROM pessoas ORDER BY nome_razao_social DESC")
    lista = []
    for i in lista_db:
        lista.append(i)

    desconecta_db(banco)

    return lista

def filtro_database_pessoas(search_data, filtro_status, filtro_opcoes, filtro_tipo_pesquisa):
    banco, cursor = conecta_db()
    filtro_status = filtro_status.get()
    filtro_opcoes = filtro_opcoes.get()
    filtro_tipo_pesquisa = filtro_tipo_pesquisa.get()
    #para segurança, adicionar um lista de colunas validas para a clausula, codigo, nome, fantasia etc

    if filtro_tipo_pesquisa == "aproximacao":
        search_data = f'%{search_data.replace(" ","%")}%'

    elif filtro_tipo_pesquisa == "inicio":
        search_data = f'{search_data.replace(" ","%")}%'

    if filtro_status == "TODOS":
        lista_db = cursor.execute("SELECT id, nome_razao_social,cpf_cnpj,cidade FROM pessoas WHERE nome_razao_social LIKE ? ORDER BY ?", (search_data, filtro_opcoes,))
        lista = []
        for i in lista_db:
            lista.append(i)
    else:
        lista_db = cursor.execute("SELECT id, nome_razao_social,cpf_cnpj,cidade FROM pessoas WHERE status = ? AND nome_razao_social LIKE ? ORDER BY ?", (filtro_status, search_data, filtro_opcoes,))
        lista = []
        for i in lista_db:
            lista.append(i)

    desconecta_db(banco)

    return lista

def pega_um_item_pessoa(item):
    banco, cursor = conecta_db()

    pessoa = cursor.execute('SELECT * FROM pessoas WHERE id = ?', (str(item),))

    pessoa = pessoa.fetchall()
    desconecta_db(banco)
    return pessoa

def pega_todas_trabalhos_lista():

    banco, cursor = conecta_db()
    #retorna em ordem alfabética, modificar isso com as filtragens
    lista_db = cursor.execute("SELECT id, data,hora,nome_pessoa,tipo,plano_nome,etapa_atual FROM sessoes ORDER BY pessoa_sessao DESC")
    lista = []
    for i in lista_db:
        lista.append(i)

    desconecta_db(banco)

    return lista
def pega_todos_planos_sessoes_lista():
    banco, cursor = conecta_db()
    #retorna em ordem alfabética, modificar isso com as filtragens
    lista_db = cursor.execute("SELECT id, nome_plano FROM planos ORDER BY id")
    lista = []
    for i in lista_db:
        lista.append(i)

    desconecta_db(banco)

    return lista

def grava_db_trabalhos(entry_codigo,entry_cadastro,entry_data_sessao,entry_horario_sessao,codigo_pessoa_trabalho,entry_nome,cb_tipo_sessao,codigo_tipo_trabalho,cb_plano,codigo_plano_trabalho,pagamento1,entry_valor1,pagamento2,entry_valor2,pagamento3,entry_valor3,entry_total,textarea_observacoes,entry_quantidade_foto_extra,entry_valor_foto_extra):
    entry_codigo = int(entry_codigo())
    entry_cadastro = entry_cadastro()
    entry_data_sessao = entry_data_sessao()
    entry_horario_sessao = entry_horario_sessao()
    codigo_pessoa_trabalho = int(codigo_pessoa_trabalho)
    entry_nome = entry_nome()
    cb_tipo_sessao = cb_tipo_sessao()
    codigo_tipo_trabalho = int(codigo_tipo_trabalho)
    cb_plano = cb_plano()
    codigo_plano_trabalho = int(codigo_plano_trabalho)
    pagamento1 = pagamento1()
    entry_valor1 = float(entry_valor1)
    pagamento2 = pagamento2()
    entry_valor2 = float(entry_valor2)
    pagamento3 = pagamento3()
    entry_valor3 = float(entry_valor3)
    entry_total = float(entry_total())
    textarea_observacoes = textarea_observacoes("1.0","end-1c")
    quantidade_foto_extra = entry_quantidade_foto_extra()
    valor_foto_extra = entry_valor_foto_extra()


    banco, cursor = conecta_db()
#obs ao dar o return, mandar a informação self.argumentos = None
    cursor.execute(f"INSERT INTO sessoes (pessoa_sessao,nome_pessoa,id_tipo,tipo,plano_contratado,plano_nome,data,hora,pagamento1,valor_pagamento1,pagamento2,valor_pagamento2,pagamento3,valor_pagamento3,total_pagamentos,observasoes,data_cadastro,quantidade_foto_extra,valor_foto_extra) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(codigo_pessoa_trabalho,entry_nome,codigo_tipo_trabalho,cb_tipo_sessao,codigo_plano_trabalho,cb_plano,entry_data_sessao,entry_horario_sessao,pagamento1,entry_valor1,pagamento2,entry_valor2,pagamento3,entry_valor3,entry_total,textarea_observacoes,entry_cadastro,quantidade_foto_extra,valor_foto_extra))
    cursor.execute("select * from sessoes")
    print(cursor.fetchall())
    banco.commit()

    desconecta_db(banco)

def altera_db_trabalhos(entry_codigo,entry_cadastro,entry_data_sessao,entry_horario_sessao,codigo_pessoa_trabalho,entry_nome,cb_tipo_sessao,codigo_tipo_trabalho,cb_plano,codigo_plano_trabalho,pagamento1,entry_valor1,pagamento2,entry_valor2,pagamento3,entry_valor3,entry_total,textarea_observacoes,entry_quantidade_foto_extra,entry_valor_foto_extra):
    id = int(entry_codigo())
    entry_cadastro = entry_cadastro()
    entry_data_sessao = entry_data_sessao()
    entry_horario_sessao = entry_horario_sessao()
    codigo_pessoa_trabalho = int(codigo_pessoa_trabalho)
    entry_nome = entry_nome()
    cb_tipo_sessao = cb_tipo_sessao()
    codigo_tipo_trabalho = int(codigo_tipo_trabalho)
    cb_plano = cb_plano()
    codigo_plano_trabalho = int(codigo_plano_trabalho)
    pagamento1 = pagamento1()
    entry_valor1 = float(entry_valor1)
    pagamento2 = pagamento2()
    entry_valor2 = float(entry_valor2)
    pagamento3 = pagamento3()
    entry_valor3 = float(entry_valor3)
    entry_total = float(entry_total())
    textarea_observacoes = textarea_observacoes("1.0","end-1c")
    quantidade_foto_extra = entry_quantidade_foto_extra()
    valor_foto_extra = entry_valor_foto_extra()


    banco, cursor = conecta_db()
    cursor.execute(f"UPDATE sessoes SET pessoa_sessao = ?,nome_pessoa = ?, id_tipo=?, tipo = ?, plano_contratado=?,plano_nome=?, data=?,hora=?, pagamento1=?, valor_pagamento1=?, pagamento2=?, valor_pagamento2=?,pagamento3=?, valor_pagamento3=?, total_pagamentos=?, observasoes=?,data_cadastro=?,quantidade_foto_extra = ?, valor_foto_extra = ?  WHERE id = ?",(codigo_pessoa_trabalho,entry_nome,codigo_tipo_trabalho,cb_tipo_sessao,codigo_plano_trabalho,cb_plano,entry_data_sessao,entry_horario_sessao,pagamento1,entry_valor1,pagamento2,entry_valor2,pagamento3,entry_valor3,entry_total,textarea_observacoes,entry_cadastro,quantidade_foto_extra, valor_foto_extra, id))
    cursor.execute("select * from sessoes")
    banco.commit()

    desconecta_db(banco)

def deleta_db_trabalho(id):
    banco, cursor = conecta_db()
    cursor.execute(f"DELETE FROM sessoes WHERE id = ?", (str(id),))

    banco.commit()

    desconecta_db(banco)
def pega_um_item_trabalho(item):
    banco, cursor = conecta_db()

    trabalho = cursor.execute('SELECT * FROM sessoes WHERE id = ?', (str(item),))
    trabalho = trabalho.fetchall()

    desconecta_db(banco)
    return trabalho
def pega_um_item_plano(item):
    banco, cursor = conecta_db()

    pessoa = cursor.execute('SELECT * FROM planos WHERE id = ?', (str(item),))
    pessoa = pessoa.fetchall()
    print(pessoa)
    desconecta_db(banco)
    return pessoa

def grava_db_planos(entry_codigo,entry_cadastro,entry_nome,entry_descricao,entry_valor_base,entry_quantidade_fotos,entry_valor_foto_extra):
    entry_codigo = entry_codigo()
    entry_cadastro= entry_cadastro()
    entry_nome= entry_nome()
    entry_descricao= entry_descricao()
    entry_valor_base= float(entry_valor_base)
    entry_quantidade_fotos= int(entry_quantidade_fotos)
    entry_valor_foto_extra= float(entry_valor_foto_extra)

    print(entry_codigo,entry_cadastro,entry_nome,entry_descricao,entry_valor_base,entry_quantidade_fotos,entry_valor_foto_extra)

    banco, cursor = conecta_db()

    cursor.execute(f"INSERT INTO planos (nome_plano, quantidade_fotos, valor, valor_foto_extra,descricao, data_criacao) VALUES (?,?,?,?,?,?)",(entry_nome,entry_quantidade_fotos,entry_valor_base,entry_valor_foto_extra,entry_descricao,entry_cadastro))
    cursor.execute("select * from planos")
    banco.commit()

    desconecta_db(banco)

def altera_db_planos(entry_codigo,entry_cadastro,entry_nome,entry_descricao,entry_valor_base,entry_quantidade_fotos,entry_valor_foto_extra):
    id = entry_codigo()
    entry_cadastro= entry_cadastro()
    entry_nome= entry_nome()
    entry_descricao= entry_descricao()
    entry_valor_base= float(entry_valor_base)
    entry_quantidade_fotos= int(entry_quantidade_fotos)
    entry_valor_foto_extra= float(entry_valor_foto_extra)

    banco, cursor = conecta_db()

    cursor.execute(f"UPDATE planos SET nome_plano = ?, quantidade_fotos = ?, valor = ?, valor_foto_extra = ?,descricao = ?, data_criacao = ? WHERE id = ?",(entry_nome,entry_quantidade_fotos,entry_valor_base,entry_valor_foto_extra,entry_descricao,entry_cadastro, id))
    cursor.execute("select * from planos")
    banco.commit()

    desconecta_db(banco)

def deleta_db_plano(id):
    banco, cursor = conecta_db()
    cursor.execute(f"DELETE FROM planos WHERE id = ?", (str(id),))

    banco.commit()

    desconecta_db(banco)
def grava_db_tipos(entry_codigo,entry_cadastro,entry_nome,entry_descricao):
    entry_codigo= entry_codigo()
    entry_cadastro = entry_cadastro()
    entry_nome= entry_nome()
    entry_descricao= entry_descricao()

    banco, cursor = conecta_db()

    cursor.execute(f"INSERT INTO tipos (nome_tipo,descricao,data_criacao) VALUES (?,?,?)",(entry_nome,entry_descricao,entry_cadastro))
    cursor.execute("select * from tipos")
    banco.commit()

    desconecta_db(banco)

def altera_db_tipos(entry_codigo,entry_cadastro,entry_nome,entry_descricao):
    id = entry_codigo()
    entry_cadastro = entry_cadastro()
    entry_nome= entry_nome()
    entry_descricao= entry_descricao()

    banco, cursor = conecta_db()

    cursor.execute(f"UPDATE tipos SET nome_tipo = ?, descricao = ?, data_criacao = ? WHERE id = ?",(entry_nome,entry_descricao,entry_cadastro, id))
    cursor.execute("select * from tipos")
    banco.commit()

    desconecta_db(banco)

def deleta_db_tipo(id):
    banco, cursor = conecta_db()
    cursor.execute(f"DELETE FROM tipos WHERE id = ?", (str(id),))

    banco.commit()

    desconecta_db(banco)

def pega_um_item_tipo(item):
    banco, cursor = conecta_db()
    item = str(item)
    tipo = cursor.execute('SELECT * FROM tipos WHERE id = ?', (str(item),))
    tipo = tipo.fetchall()
    desconecta_db(banco)
    return tipo
def pega_todos_tipos_sessoes_lista():
    banco, cursor = conecta_db()
    #retorna em ordem alfabética, modificar isso com as filtragens
    lista_db = cursor.execute("SELECT id, nome_tipo FROM tipos ORDER BY id")
    lista = []
    for i in lista_db:
        lista.append(i)

    desconecta_db(banco)

    return lista


def desconecta_db(banco):
    banco.close()

def adiciona_pessoa():
    pass

if __name__ == '__main__':


    banco, cursor = conecta_db()

    desconecta_db(banco)