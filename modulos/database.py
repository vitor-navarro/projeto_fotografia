import sqlite3


def conecta_db():
    banco = sqlite3.connect("../modulos/database.db")
    cursor = banco.cursor()

    return banco, cursor

def grava_db_pessoa(entry_codigo_valor,entry_cadastro_valor,cb_status_valor,cb_tipo_valor,entry_cpf_cnpj_valor,entry_rg_inscricao_valor,ventry_nascimento_valor,
                                       entry_nome_valor,entry_apelido_valor,entry_endereco_valor,entry_complemento_valor,entry_bairro_valor,entry_nome_cidade_valor,entry_uf_valor,
                                       entry_cep_valor,entry_fone1_valor,entry_fone2_valor,entry_fone3_valor,entry_operadora1_valor,entry_operadora2_valor,
                                       entry_operadora3_valor,entry_email_valor,entry_numero):
    codigo_valor= entry_codigo_valor()
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

    banco,cursor = conecta_db()

    cursor.execute(f"INSERT INTO pessoas (data_cadastro, nome_razao_social, status, tipo,cpf_cnpj, apelido_fantasia,rg_inscricao_estadual, data_nascimento, endereco, numero_casa, complemento,bairro, cidade, cep, uf,fone1, operador1, fone2, operador2, fone3, operador3, email) VALUES ({cadastro_valor},{nome_valor},{status_valor},{tipo_valor},{cpf_cnpj_valor},{apelido_valor},{rg_inscricao_valor},{nascimento_valor},{endereco_valor},{numero_casa_valor},{complemento_valor},{bairro_valor},{nome_cidade_valor},{cep_valor},{uf_valor},{fone1_valor},{operadora1_valor},{fone2_valor},{operadora2_valor},{fone3_valor},{operadora3_valor},{email_valor})")

    banco.commit()

    desconecta_db(banco)
    pass
def desconecta_db(banco):
    banco.close()

def adiciona_pessoa():
    pass

if __name__ == '__main__':


    banco, cursor = conecta_db()

    desconecta_db(banco)