import sqlite3


def conecta_db():
    banco = sqlite3.connect("../modulos/database.db")
    cursor = banco.cursor()

    return banco, cursor

def pega_ultimo_id(nome_banco):
    banco,cursor = conecta_db()

    cursor.execute(f"SELECT id FROM {nome_banco}")
    lista = cursor.fetchall()
    print(lista)
    if len(lista) != 0:
        ultimo = str(lista[len(lista)-1])
        ultimo_replace = ultimo.replace("(","")
        ultimo_replace = ultimo_replace.replace(")","")
        ultimo_replace = ultimo_replace.replace(",","")
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
    id = str(id)
    cursor.execute(f"DELETE FROM pessoas WHERE id = ?", (id))

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

def pega_um_item_pessoa(item):
    banco, cursor = conecta_db()

    item = str(item)
    pessoa = cursor.execute('SELECT * FROM pessoas WHERE id = ?', (item))
    pessoa = pessoa.fetchall()
    desconecta_db(banco)
    return pessoa
def pega_todas_trabalhos_lista():

    banco, cursor = conecta_db()
    #retorna em ordem alfabética, modificar isso com as filtragens
    lista_db = cursor.execute("SELECT id, data,pessoa_sessao,pessoa_extra,tipo,estapa_atual FROM sessoes ORDER BY nome_razao_social DESC")
    lista = []
    for i in lista_db:
        lista.append(i)

    desconecta_db(banco)

    return lista
def pega_todos_tipos_sessoes_lista():
    banco, cursor = conecta_db()
    #retorna em ordem alfabética, modificar isso com as filtragens
    lista_db = cursor.execute("SELECT id, nome_plano FROM planos ORDER BY id")
    lista = []
    for i in lista_db:
        lista.append(i)

    desconecta_db(banco)

    return lista

def grava_db_trabalhos(entry_codigo,entry_cadastro,entry_data_sessao,entry_horario_sessao,codigo_pessoa_trabalho,entry_nome,cb_tipo_sessao,cb_plano,entry_valor1,entry_valor2,entry_valor3,entry_total,textarea_observacoes):
    entry_codigo = entry_codigo()
    entry_cadastro = entry_cadastro()
    entry_data_sessao = entry_data_sessao()
    entry_horario_sessao = entry_horario_sessao()
    codigo_pessoa_trabalho = codigo_pessoa_trabalho
    entry_nome = entry_nome()
    cb_tipo_sessao = cb_tipo_sessao()
    cb_plano = cb_plano()
    entry_valor1 = entry_valor1()
    entry_valor2 = entry_valor2()
    entry_valor3 = entry_valor3()
    entry_total = entry_total()
    textarea_observacoes = textarea_observacoes("1.0","end-1c")

    banco, cursor = conecta_db()
#obs ao dar o return, mandar a informação self.argumentos = None
    print(entry_codigo,entry_cadastro,entry_data_sessao,entry_horario_sessao,codigo_pessoa_trabalho,entry_nome,cb_tipo_sessao,cb_plano,entry_valor1,entry_valor2,entry_valor3,entry_total,textarea_observacoes)
    cursor.execute(f"INSERT INTO sessoes () VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",())
    cursor.execute("select * from sessoes")
    print(cursor.fetchall())
    banco.commit()

    desconecta_db(banco)
def pega_um_item_trabalho(item):
    banco, cursor = conecta_db()

    item = str(item)
    trabalho = cursor.execute('SELECT * FROM sessoes WHERE id = ?', (item))
    trabalho = trabalho.fetchall()
    desconecta_db(banco)
    return trabalho

def grava_db_planos(entry_codigo,entry_cadastro,entry_nome,entry_descricao,entry_valor_base,entry_quantidade_fotos,entry_valor_foto_extra):
    entry_codigo= entry_codigo()
    entry_cadastro= entry_cadastro()
    entry_nome= entry_nome()
    entry_descricao= entry_descricao()
    entry_valor_base= float(entry_valor_base())
    entry_quantidade_fotos= int(entry_quantidade_fotos())
    entry_valor_foto_extra= float(entry_valor_foto_extra())

    banco, cursor = conecta_db()

    cursor.execute(f"INSERT INTO planos (nome_plano, quantidade_fotos, valor, valor_foto_extra,descricao, data_criacao) VALUES (?,?,?,?,?,?)",(entry_nome,entry_quantidade_fotos,entry_valor_base,entry_valor_foto_extra,entry_descricao,entry_cadastro))
    cursor.execute("select * from planos")
    print(cursor.fetchall())
    banco.commit()

    desconecta_db(banco)
def desconecta_db(banco):
    banco.close()

def adiciona_pessoa():
    pass

if __name__ == '__main__':


    banco, cursor = conecta_db()

    desconecta_db(banco)