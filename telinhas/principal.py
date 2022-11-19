
from tkinter import *
from tkinter import ttk
from datetime import date
from modulos.database import grava_db_pessoa, grava_db_trabalhos, pega_ultimo_id, pega_todas_pessoas_lista, \
    pega_um_item_pessoa, altera_db_pessoa, deleta_db_pessoa, pega_um_item_trabalho, pega_todos_tipos_sessoes_lista, \
    grava_db_planos, pega_um_item_plano, pega_um_item_tipo, pega_todos_planos_sessoes_lista, grava_db_tipos
from functools import partial
class Funcs():
    def __init__(self):
        self.lb_style = ("monospace", 12)
        self.paddingx = 10
        self.paddingy = 7
        self.entry_style = ("monospace", 14)
        self.data_sistema = date.today().strftime('%d/%m/%Y')
        self.lista_de_pessoas = None
        self.lista_de_trabalhos = None
        self.lista_planos = None
        self.argumentos = None
        self.nome_pessoa_trabalho = None
        self.codigo_pessoa_trabalho = None
        self.codigo_tipo_trabalho = None
        self.nome_tipo_trabalho = None
        self.codigo_plano_trabalho = None
        self.nome_plano_trabalho = None
        self.valores_pagamento = []

    def sem_comando(self):
        print("Tela ainda não cadastrada")

    def configurar_janela_auxiliar(self,janela):
        janela.update_idletasks()

        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()

        x = int((screen_width / 2) - (964 / 2) - 50)
        y = int((screen_height / 2) - (580 / 2) - 50)

        janela.geometry("+%d+%d" % (x, y))

        janela.geometry("1024x624")
        janela.resizable(False,False)

    def configurar_janela_auxiliar2(self,janela):
        janela.update_idletasks()

        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        #modificar para ficar no meio da tela.

        x = int(screen_width/4)
        y = int(screen_height/4)

        janela.geometry("+%d+%d" % (x, y))

        janela.geometry("512x312")
        janela.resizable(False,False)

    def configurar_janela_auxiliar3(self,janela):
        janela.update_idletasks()

        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        #modificar para ficar no meio da tela.

        x = int(screen_width/6)
        y = int(screen_height/6)

        janela.geometry("+%d+%d" % (x, y))

        janela.geometry("768x468")
        janela.resizable(False,False)

    def insert_entry_desabilitado(self, entry, valor,posicao = 0):
        if valor == None:
            valor = ""
        entry.config(state="normal")
        entry.delete(0, END)
        entry.insert(posicao, valor)
        entry.config(state="disabled")
    def novo_cadastro_tipo(self):
        janela = Toplevel()
        self.configurar_janela_auxiliar3(janela)
        janela.title("Cadastro Tipos")

        codigo = pega_ultimo_id("tipos")

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")
        self.insert_entry_desabilitado(entry_codigo, codigo)

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
        entry_cadastro.insert(END, self.data_sistema)
        entry_cadastro.grid(column=1, row=1, padx=self.paddingx)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador2, text="Nome*", font=self.lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style,width=89)
        entry_nome.grid(column=0, row=1, padx=self.paddingx)

        separador3 = ttk.Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_descricao = Label(separador3, text="Descrição", font=self.lb_style)
        lb_descricao.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_descricao = Entry(separador3, font=self.entry_style,width=89)
        entry_descricao.grid(column=0, row=1, padx=self.paddingx)

        separador5 = ttk.Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy,side=BOTTOM)

        grava_db_pessoa_args = partial(grava_db_tipos,entry_codigo.get,entry_cadastro.get,entry_nome.get,entry_descricao.get)
        grava = Button(separador5, text="GRAVA", font=self.lb_style, command=grava_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador5, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")
    def altera_cadastro_tipo(self):
        pass
    def exclui_cadastro_tipo(self):
        pass
    def novo_cadastro_plano(self):
        janela = Toplevel()
        self.configurar_janela_auxiliar3(janela)
        janela.title("Cadastro Planos")

        codigo = pega_ultimo_id("planos")

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")
        self.insert_entry_desabilitado(entry_codigo, codigo)

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
        entry_cadastro.insert(END, self.data_sistema)
        entry_cadastro.grid(column=1, row=1, padx=self.paddingx)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador2, text="Nome*", font=self.lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style,width=89)
        entry_nome.grid(column=0, row=1, padx=self.paddingx)

        separador3 = ttk.Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_descricao = Label(separador3, text="Descrição", font=self.lb_style)
        lb_descricao.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_descricao = Entry(separador3, font=self.entry_style,width=89)
        entry_descricao.grid(column=0, row=1, padx=self.paddingx)

        separador4 = ttk.Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_valor_base = Label(separador4, text="Valor do Plano", font=self.lb_style)
        lb_valor_base.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_valor_base = Entry(separador4, font=self.entry_style)
        entry_valor_base.grid(column=0, row=1, padx=self.paddingx)

        separador5 = ttk.Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_quantidade_fotos = Label(separador5, text="Quantidade de fotos", font=self.lb_style)
        lb_quantidade_fotos.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_quantidade_fotos = Entry(separador5, font=self.entry_style)
        entry_quantidade_fotos.grid(column=1, row=1, padx=self.paddingx)

        lb_valor_foto_extra = Label(separador5, text="Valor Fotos extra", font=self.lb_style)
        lb_valor_foto_extra.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_valor_foto_extra = Entry(separador5, font=self.entry_style)
        entry_valor_foto_extra.grid(column=2, row=1, padx=self.paddingx)

        separador5 = ttk.Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy,side=BOTTOM)

        grava_db_pessoa_args = partial(grava_db_planos,entry_codigo.get,entry_cadastro.get,entry_nome.get,entry_descricao.get,entry_valor_base.get,entry_quantidade_fotos.get,entry_valor_foto_extra.get)
        grava = Button(separador5, text="GRAVA", font=self.lb_style, command=grava_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador5, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")
    def altera_cadastro_plano(self):
        pass
    def exclui_cadastro_plano(self):
        pass


    def novo_cadastro_pessoa(self):
        janela = Toplevel()

        variavel_upercase = StringVar()

        janela.title("Cadastro Pessoas")

        self.configurar_janela_auxiliar(janela)

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        codigo = pega_ultimo_id("pessoas")

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")
        self.insert_entry_desabilitado(entry_codigo, codigo)

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
        entry_cadastro.insert(END, self.data_sistema)
        entry_cadastro.grid(column=1, row=1, padx=self.paddingx)

        status_possiveis = ["Ativo", "Inativo"]
        tipos_possiveis_pessoas = ["Física", "Jurídica"]

        # mudar para opções
        lb_status = Label(separador1, text="Status", font=self.lb_style)
        lb_status.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        cb_status = ttk.Combobox(separador1, font=self.entry_style, width=15, values=status_possiveis, state="readonly")
        cb_status.set("Ativo")
        cb_status.grid(column=2, row=1, padx=self.paddingx)

        # mudar para opções
        lb_tipo = Label(separador1, text="Tipo", font=self.lb_style)
        lb_tipo.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        cb_tipo = ttk.Combobox(separador1, font=self.entry_style, width=15, values=tipos_possiveis_pessoas, state="readonly")
        cb_tipo.set("Física")
        cb_tipo.grid(column=3, row=1, padx=self.paddingx)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        # condicao para mudar quando for tipo juridica
        lb_cpf_cnpj = Label(separador2, text="CPF", font=self.lb_style)
        lb_cpf_cnpj.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_cpf_cnpj = Entry(separador2, font=self.entry_style, width=20)
        entry_cpf_cnpj.grid(column=0, row=1, padx=self.paddingx)

        # condicao para mudar quando for tipo juridica
        lb_rg_inscricao = Label(separador2, text="RG", font=self.lb_style)
        lb_rg_inscricao.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_rg_inscricao = Entry(separador2, font=self.entry_style, width=20)
        entry_rg_inscricao.grid(column=1, row=1, padx=self.paddingx)

        lb_nascimento = Label(separador2, text="Nascimento", font=self.lb_style)
        lb_nascimento.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_nascimento = Entry(separador2, font=self.entry_style, width=10)
        entry_nascimento.grid(column=2, row=1, padx=self.paddingx)

        separador3 = ttk.Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador3, text="Nome*", font=self.lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador3, font=self.entry_style, width=89)
        entry_nome.grid(column=0, row=1, padx=self.paddingx)

        lb_apelido = Label(separador3, text="Apelido", font=self.lb_style)
        lb_apelido.grid(column=0, row=2, sticky="W", padx=self.paddingx)
        entry_apelido = Entry(separador3, font=self.entry_style, width=89)
        entry_apelido.grid(column=0, row=3, padx=self.paddingx)

        separador4 = ttk.Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_endereco = Label(separador4, text="Endereço", font=self.lb_style)
        lb_endereco.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_endereco = Entry(separador4, font=self.entry_style, width=82)
        entry_endereco.grid(column=0, row=1, padx=self.paddingx)

        lb_numero = Label(separador4, text="Numero", font=self.lb_style)
        lb_numero.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_numero = Entry(separador4, font=self.entry_style, width=5)
        entry_numero.grid(column=1, row=1, padx=self.paddingx)

        separador5 = ttk.Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_complemento = Label(separador5, text="Complemento", font=self.lb_style)
        lb_complemento.grid(column=0, row=2, sticky="W", padx=self.paddingx)
        entry_complemento = Entry(separador5, font=self.entry_style, width=44)
        entry_complemento.grid(column=0, row=3, padx=self.paddingx)

        lb_bairro = Label(separador5, text="Bairro", font=self.lb_style)
        lb_bairro.grid(column=1, row=2, sticky="W", padx=self.paddingx)
        entry_bairro = Entry(separador5, font=self.entry_style, width=43)
        entry_bairro.grid(column=1, row=3, padx=self.paddingx)

        separador6 = ttk.Separator(janela, orient="horizontal")
        separador6.pack(fill="x", padx=self.paddingx, pady=self.paddingy)
        '''
        lb_cidade = Label(separador6, text="Cidade", font=self.lb_style, state=DISABLED)
        lb_cidade.grid(column=0, row=4, sticky="W", padx=self.paddingx)
        entry_cidade = Entry(separador6, font=self.entry_style,width=5)
        entry_cidade.grid(column=0, row=5, padx=self.paddingx)
        '''

        lb_nome_cidade = Label(separador6, text="Cidade", font=self.lb_style)
        lb_nome_cidade.grid(column=1, row=4, sticky="W", padx=self.paddingx)
        entry_nome_cidade = Entry(separador6, font=self.entry_style, width=40)
        entry_nome_cidade.grid(column=1, row=5, padx=self.paddingx)

        lb_uf = Label(separador6, text="UF", font=self.lb_style)
        lb_uf.grid(column=2, row=4, sticky="W", padx=self.paddingx)
        entry_uf = Entry(separador6, font=self.entry_style, width=3)
        entry_uf.grid(column=2, row=5, padx=self.paddingx)

        lb_cep = Label(separador6, text="CEP", font=self.lb_style)
        lb_cep.grid(column=3, row=4, sticky="W", padx=self.paddingx)
        entry_cep = Entry(separador6, font=self.entry_style, width=10)
        entry_cep.grid(column=3, row=5, padx=self.paddingx)

        separador7 = ttk.Separator(janela, orient="horizontal")
        separador7.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        width_fone = 17
        width_operadora = 8
        lb_fone1 = Label(separador7, text="Fone 1", font=self.lb_style)
        lb_fone1.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_fone1 = Entry(separador7, font=self.entry_style, width=width_fone)
        entry_fone1.grid(column=0, row=1, padx=self.paddingx)

        lb_operadora1 = Label(separador7, text="Operadora", font=self.lb_style)
        lb_operadora1.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_operadora1 = Entry(separador7, font=self.entry_style, width=width_operadora)
        entry_operadora1.grid(column=1, row=1, padx=self.paddingx)

        lb_fone2 = Label(separador7, text="Fone 2", font=self.lb_style)
        lb_fone2.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_fone2 = Entry(separador7, font=self.entry_style, width=width_fone)
        entry_fone2.grid(column=2, row=1, padx=self.paddingx)

        lb_operadora2 = Label(separador7, text="Operadora", font=self.lb_style)
        lb_operadora2.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        entry_operadora2 = Entry(separador7, font=self.entry_style, width=width_operadora)
        entry_operadora2.grid(column=3, row=1, padx=self.paddingx)

        lb_fone3 = Label(separador7, text="Fone 3", font=self.lb_style)
        lb_fone3.grid(column=4, row=0, sticky="W", padx=self.paddingx)
        entry_fone3 = Entry(separador7, font=self.entry_style, width=width_fone)
        entry_fone3.grid(column=4, row=1, padx=self.paddingx)

        lb_operadora3 = Label(separador7, text="Operadora", font=self.lb_style)
        lb_operadora3.grid(column=5, row=0, sticky="W", padx=self.paddingx)
        entry_operadora3 = Entry(separador7, font=self.entry_style, width=width_operadora)
        entry_operadora3.grid(column=5, row=1, padx=self.paddingx)

        separador8 = ttk.Separator(janela, orient="horizontal")
        separador8.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_email = Label(separador8, text="Email", font=self.lb_style)
        lb_email.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_email = Entry(separador8, font=self.entry_style, width=89)
        entry_email.grid(column=0, row=1, padx=self.paddingx)

        lb_campos_obrigatorios = Label(janela, text="(*) Campos Obrigatórios")
        lb_campos_obrigatorios.pack(fill="x", side=RIGHT, anchor=NW)

        separador9 = ttk.Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)



        grava_db_pessoa_args = partial(grava_db_pessoa,entry_codigo.get,entry_cadastro.get,cb_status.get,cb_tipo.get,entry_cpf_cnpj.get,entry_rg_inscricao.get,entry_nascimento.get,
                                       entry_nome.get,entry_apelido.get,entry_endereco.get,entry_complemento.get,entry_bairro.get,entry_nome_cidade.get,entry_uf.get,
                                       entry_cep.get,entry_fone1.get,entry_fone2.get,entry_fone3.get,entry_operadora1.get,entry_operadora2.get,
                                       entry_operadora3.get,entry_email.get,entry_numero.get)
        grava = Button(separador9, text="GRAVA", font=self.lb_style, command=grava_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador9, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")
    def seleciona_item_pessoas(self):

        for selected_item in self.lista_de_pessoas.selection():
            item = self.lista_de_pessoas.item(selected_item)
            record = item['values']
            pessoa = pega_um_item_pessoa(record[0])
            return pessoa

    def seleciona_item_trabalhos(self):

        for selected_item in self.lista_de_trabalhos.selection():
            item = self.lista_de_trabalhos.item(selected_item)
            record = item['values']
            pessoa = pega_um_item_trabalho(record[0])
            return pessoa

    def novo_financeiro(self):
        janela = Toplevel()

        janela.title("Cadastro Financeiro")

        self.configurar_janela_auxiliar2(janela)

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_data = Label(separador1, text="Data", font=self.lb_style)
        lb_data.grid(column=2, row=1, sticky="W", padx=self.paddingx)
        entry_data = Entry(separador1, font=self.entry_style, width=10)
        entry_data.grid(column=2, row=2, padx=self.paddingx)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_codigo_sessao = Label(separador2, text="Sessão", font=self.lb_style)
        lb_codigo_sessao.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo_sessao = Entry(separador2, font=self.entry_style, width=8)
        entry_codigo_sessao.grid(column=0, row=1, padx=self.paddingx, sticky="NW")

        lb_nome = Label(separador2, text="Nome", font=self.lb_style)
        lb_nome.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=30, state=DISABLED)
        entry_nome.grid(column=1, row=1, padx=self.paddingx)

        separador3 = ttk.Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_valor = Label(separador3, text="Valor", font=self.lb_style)
        lb_valor.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_valor = Entry(separador3, font=self.entry_style, width=10)
        entry_valor.grid(column=0, row=1, padx=self.paddingx)

        pagamentos_possiveis = ["Dinheiro", "Pix", "Cartão"]

        # mudar para opções
        lb_tipo = Label(separador3, text="Status", font=self.lb_style)
        lb_tipo.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        cb_tipo = ttk.Combobox(separador3, font=self.entry_style, width=15, values=pagamentos_possiveis, state="readonly")
        cb_tipo.set("Dinheiro")
        cb_tipo.grid(column=1, row=1, padx=self.paddingx)

        lb_parcelas= Label(separador3, text="Nº Parcelas", font=self.lb_style)
        lb_parcelas.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_parcelas = Entry(separador3, font=self.entry_style, width=10)
        entry_parcelas.grid(column=2, row=1, padx=self.paddingx)

        separador4 = ttk.Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy,side=BOTTOM)

        grava = Button(separador4, text="GRAVA", font=self.lb_style)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador4, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")

    def altera_cadastro_pessoa(self):
        pessoa = self.seleciona_item_pessoas()

        print(pessoa)
        janela = Toplevel()
        variavel_upercase = StringVar()

        janela.title("Cadastro Pessoas")

        self.configurar_janela_auxiliar(janela)

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        codigo = pega_ultimo_id("pessoas")

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")
        self.insert_entry_desabilitado(entry_codigo, pessoa[0][0])

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
        entry_cadastro.insert(END, self.data_sistema)
        entry_cadastro.grid(column=1, row=1, padx=self.paddingx)
        entry_cadastro.delete(0, END)
        entry_cadastro.insert(END,pessoa[0][1])

        status_possiveis = ["Ativo", "Inativo"]
        tipos_possiveis_pessoas = ["Física", "Jurídica"]

        # mudar para opções
        lb_status = Label(separador1, text="Status", font=self.lb_style)
        lb_status.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        cb_status = ttk.Combobox(separador1, font=self.entry_style, width=15, values=status_possiveis, state="readonly")
        cb_status.set(pessoa[0][3])
        cb_status.grid(column=2, row=1, padx=self.paddingx)

        # mudar para opções
        lb_tipo = Label(separador1, text="Tipo", font=self.lb_style)
        lb_tipo.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        cb_tipo = ttk.Combobox(separador1, font=self.entry_style, width=15, values=tipos_possiveis_pessoas,
                               state="readonly")
        cb_tipo.set(pessoa[0][4])
        cb_tipo.grid(column=3, row=1, padx=self.paddingx)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        # condicao para mudar quando for tipo juridica
        lb_cpf_cnpj = Label(separador2, text="CPF", font=self.lb_style)
        lb_cpf_cnpj.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_cpf_cnpj = Entry(separador2, font=self.entry_style, width=20)
        entry_cpf_cnpj.grid(column=0, row=1, padx=self.paddingx)
        entry_cpf_cnpj.insert(END,pessoa[0][5])

        # condicao para mudar quando for tipo juridica
        lb_rg_inscricao = Label(separador2, text="RG", font=self.lb_style)
        lb_rg_inscricao.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_rg_inscricao = Entry(separador2, font=self.entry_style, width=20)
        entry_rg_inscricao.grid(column=1, row=1, padx=self.paddingx)
        entry_rg_inscricao.insert(END,pessoa[0][7])

        lb_nascimento = Label(separador2, text="Nascimento", font=self.lb_style)
        lb_nascimento.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_nascimento = Entry(separador2, font=self.entry_style, width=10)
        entry_nascimento.grid(column=2, row=1, padx=self.paddingx)
        entry_nascimento.insert(END,pessoa[0][8])

        separador3 = ttk.Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador3, text="Nome*", font=self.lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador3, font=self.entry_style, width=89)
        entry_nome.grid(column=0, row=1, padx=self.paddingx)
        entry_nome.insert(END,pessoa[0][2])

        lb_apelido = Label(separador3, text="Apelido", font=self.lb_style)
        lb_apelido.grid(column=0, row=2, sticky="W", padx=self.paddingx)
        entry_apelido = Entry(separador3, font=self.entry_style, width=89)
        entry_apelido.grid(column=0, row=3, padx=self.paddingx)
        entry_apelido.insert(END,pessoa[0][6])

        separador4 = ttk.Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_endereco = Label(separador4, text="Endereço", font=self.lb_style)
        lb_endereco.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_endereco = Entry(separador4, font=self.entry_style, width=82)
        entry_endereco.grid(column=0, row=1, padx=self.paddingx)
        entry_endereco.insert(END,pessoa[0][9])

        lb_numero = Label(separador4, text="Numero", font=self.lb_style)
        lb_numero.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_numero = Entry(separador4, font=self.entry_style, width=5)
        entry_numero.grid(column=1, row=1, padx=self.paddingx)
        entry_numero.insert(END,pessoa[0][10])

        separador5 = ttk.Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_complemento = Label(separador5, text="Complemento", font=self.lb_style)
        lb_complemento.grid(column=0, row=2, sticky="W", padx=self.paddingx)
        entry_complemento = Entry(separador5, font=self.entry_style, width=44)
        entry_complemento.grid(column=0, row=3, padx=self.paddingx)
        entry_complemento.insert(END,pessoa[0][11])

        lb_bairro = Label(separador5, text="Bairro", font=self.lb_style)
        lb_bairro.grid(column=1, row=2, sticky="W", padx=self.paddingx)
        entry_bairro = Entry(separador5, font=self.entry_style, width=43)
        entry_bairro.grid(column=1, row=3, padx=self.paddingx)
        entry_bairro.insert(END,pessoa[0][12])

        separador6 = ttk.Separator(janela, orient="horizontal")
        separador6.pack(fill="x", padx=self.paddingx, pady=self.paddingy)
        '''
        lb_cidade = Label(separador6, text="Cidade", font=self.lb_style, state=DISABLED)
        lb_cidade.grid(column=0, row=4, sticky="W", padx=self.paddingx)
        entry_cidade = Entry(separador6, font=self.entry_style,width=5)
        entry_cidade.grid(column=0, row=5, padx=self.paddingx)
        '''

        lb_nome_cidade = Label(separador6, text="Cidade", font=self.lb_style)
        lb_nome_cidade.grid(column=1, row=4, sticky="W", padx=self.paddingx)
        entry_nome_cidade = Entry(separador6, font=self.entry_style, width=40)
        entry_nome_cidade.grid(column=1, row=5, padx=self.paddingx)
        entry_nome_cidade.insert(END,pessoa[0][13])

        lb_uf = Label(separador6, text="UF", font=self.lb_style)
        lb_uf.grid(column=2, row=4, sticky="W", padx=self.paddingx)
        entry_uf = Entry(separador6, font=self.entry_style, width=3)
        entry_uf.grid(column=2, row=5, padx=self.paddingx)
        entry_uf.insert(END,pessoa[0][15])

        lb_cep = Label(separador6, text="CEP", font=self.lb_style)
        lb_cep.grid(column=3, row=4, sticky="W", padx=self.paddingx)
        entry_cep = Entry(separador6, font=self.entry_style, width=10)
        entry_cep.grid(column=3, row=5, padx=self.paddingx)
        entry_cep.insert(END,pessoa[0][14])

        separador7 = ttk.Separator(janela, orient="horizontal")
        separador7.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        width_fone = 17
        width_operadora = 8
        lb_fone1 = Label(separador7, text="Fone 1", font=self.lb_style)
        lb_fone1.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_fone1 = Entry(separador7, font=self.entry_style, width=width_fone)
        entry_fone1.grid(column=0, row=1, padx=self.paddingx)
        entry_fone1.insert(END,pessoa[0][16])

        lb_operadora1 = Label(separador7, text="Operadora", font=self.lb_style)
        lb_operadora1.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_operadora1 = Entry(separador7, font=self.entry_style, width=width_operadora)
        entry_operadora1.grid(column=1, row=1, padx=self.paddingx)
        entry_operadora1.insert(END,pessoa[0][17])

        lb_fone2 = Label(separador7, text="Fone 2", font=self.lb_style)
        lb_fone2.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_fone2 = Entry(separador7, font=self.entry_style, width=width_fone)
        entry_fone2.grid(column=2, row=1, padx=self.paddingx)
        entry_fone2.insert(END,pessoa[0][18])

        lb_operadora2 = Label(separador7, text="Operadora", font=self.lb_style)
        lb_operadora2.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        entry_operadora2 = Entry(separador7, font=self.entry_style, width=width_operadora)
        entry_operadora2.grid(column=3, row=1, padx=self.paddingx)
        entry_operadora2.insert(END,pessoa[0][19])

        lb_fone3 = Label(separador7, text="Fone 3", font=self.lb_style)
        lb_fone3.grid(column=4, row=0, sticky="W", padx=self.paddingx)
        entry_fone3 = Entry(separador7, font=self.entry_style, width=width_fone)
        entry_fone3.grid(column=4, row=1, padx=self.paddingx)
        entry_fone3.insert(END, pessoa[0][20])

        lb_operadora3 = Label(separador7, text="Operadora", font=self.lb_style)
        lb_operadora3.grid(column=5, row=0, sticky="W", padx=self.paddingx)
        entry_operadora3 = Entry(separador7, font=self.entry_style, width=width_operadora)
        entry_operadora3.grid(column=5, row=1, padx=self.paddingx)
        entry_operadora3.insert(END, pessoa[0][21])

        separador8 = ttk.Separator(janela, orient="horizontal")
        separador8.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_email = Label(separador8, text="Email", font=self.lb_style)
        lb_email.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_email = Entry(separador8, font=self.entry_style, width=89)
        entry_email.grid(column=0, row=1, padx=self.paddingx)
        entry_email.insert(END, pessoa[0][22])

        lb_campos_obrigatorios = Label(janela, text="(*) Campos Obrigatórios")
        lb_campos_obrigatorios.pack(fill="x", side=RIGHT, anchor=NW)

        separador9 = ttk.Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)

        altera_db_pessoa_args = partial(altera_db_pessoa, entry_codigo.get, entry_cadastro.get, cb_status.get,
                                       cb_tipo.get, entry_cpf_cnpj.get, entry_rg_inscricao.get, entry_nascimento.get,
                                       entry_nome.get, entry_apelido.get, entry_endereco.get, entry_complemento.get,
                                       entry_bairro.get, entry_nome_cidade.get, entry_uf.get,
                                       entry_cep.get, entry_fone1.get, entry_fone2.get, entry_fone3.get,
                                       entry_operadora1.get, entry_operadora2.get,
                                       entry_operadora3.get, entry_email.get, entry_numero.get)
        grava = Button(separador9, text="GRAVA", font=self.lb_style, command=altera_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador9, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")
        pass

    def altera_cadastro_trabalho(self):
        print("Tela ainda não cadastrada")
        pass
    def altera_financeiro(self):
        print("Tela ainda não cadastrada")
        pass
    def exclui_cadastro_pessoa(self):
        pessoa = self.seleciona_item_pessoas()
        id = pessoa[0][0]
        deleta_db_pessoa(id)
    def exclui_cadastro_trabalho(self):
        print("Tela ainda não cadastrada")
        pass
    def exclui_financeiro(self):
        print("Tela ainda não cadastrada")
        pass

class Aplicacao(Funcs):
    def __init__(self):

        super().__init__()
        self.lb_style = ("monospace", 12)
        self.paddingx = 10
        self.paddingy = 7
        self.entry_style = ("monospace", 14)
        self.btn_style = ("monospace", 12)
        self.data = date.today().strftime('%d/%m/%Y')
        self.lista_de_pessoas = None

        janela = Tk()
        # pre config

        janela.title("Projeto fotografia")
        janela.state("zoomed")

        barra_menu = ttk.Separator(janela, orient="horizontal")
        barra_menu.pack(fill="x")

        pessoas = Button(barra_menu, text="PESSOAS", font=("monospace", 12), command=self.janela_pessoas, padx=10, pady=30)
        pessoas.pack(side=LEFT)

        trabalhos = Button(barra_menu, text="TRABALHOS", font=("monospace", 12), command=self.janela_trabalhos, padx=10,
                           pady=30)
        trabalhos.pack(side=LEFT)

        financeiro = Button(barra_menu, text="FINANCEIRO", font=("monospace", 12), command=self.janela_financeiro, padx=10,
                            pady=30)
        financeiro.pack(side=LEFT)

        separador_corpo = ttk.Separator(janela, orient="horizontal")
        separador_corpo.pack(fill="x")

        barra_proximos_trabalhos = Label(separador_corpo, text="Próximos Trabalhos",font=self.lb_style, pady=self.paddingy,padx=self.paddingx)
        barra_proximos_trabalhos.pack(side=LEFT)

        janela.mainloop()

    def barra_alteracoes(self,janela, funcoes):
        barra_alteracoes = ttk.Separator(janela, orient="horizontal")
        barra_alteracoes.pack(fill="x")

        novo = Button(barra_alteracoes, text="Novo", font=("monospace", 10), command=funcoes[0], padx=5,
                      pady=10)
        novo.pack(side=LEFT)

        alterar = Button(barra_alteracoes, text="Alterar", font=("monospace", 10), command=funcoes[1], padx=5,
                         pady=10)
        alterar.pack(side=LEFT)

        excluir = Button(barra_alteracoes, text="Excluir", font=("monospace", 10), command=funcoes[2], padx=5,
                         pady=10)
        excluir.pack(side=LEFT)

        return barra_alteracoes

    def barra_filtros_opcoes_pessoas(self,barra_filtros):
        # opções 1
        barra_filtro_opcoes = ttk.Separator(barra_filtros, orient="vertical")
        barra_filtro_opcoes.grid(column=0, row=0, sticky="W")

        varaivel_opcoes = StringVar(barra_filtro_opcoes)

        label_opcoes = Label(barra_filtro_opcoes, text="Filtros")
        label_opcoes.grid(column=0, row=0, columnspan=2, sticky="W")

        rb_codigo = Radiobutton(barra_filtro_opcoes, text="Código", value="codigo", variable=varaivel_opcoes)
        rb_codigo.grid(column=0, row=1, sticky="W")

        rb_nome_fantasia = Radiobutton(barra_filtro_opcoes, text="nome/fantasia", value="nome_fantasia",
                                       variable=varaivel_opcoes)
        rb_nome_fantasia.grid(column=0, row=2, sticky="W")

        rb_nome = Radiobutton(barra_filtro_opcoes, text="nome", value="nome", variable=varaivel_opcoes)
        rb_nome.grid(column=0, row=3, sticky="W")

        rb_fantasia = Radiobutton(barra_filtro_opcoes, text="fantasia", value="fantasia", variable=varaivel_opcoes)
        rb_fantasia.grid(column=0, row=4, sticky="W")

        rb_cidade = Radiobutton(barra_filtro_opcoes, text="cidade", value="cidade", variable=varaivel_opcoes)
        rb_cidade.grid(column=1, row=1, sticky="W")

        rb_endereco = Radiobutton(barra_filtro_opcoes, text="endereco", value="endereco", variable=varaivel_opcoes)
        rb_endereco.grid(column=1, row=2, sticky="W")

        rb_cpf_cnpj = Radiobutton(barra_filtro_opcoes, text="cpf/cnpj", value="cpf_cnpj", variable=varaivel_opcoes)
        rb_cpf_cnpj.grid(column=1, row=3, sticky="W")

        rb_bairro = Radiobutton(barra_filtro_opcoes, text="bairro", value="bairro", variable=varaivel_opcoes)
        rb_bairro.grid(column=1, row=4, sticky="W")

        rb_nome_fantasia.select()

    def barra_filtros_opcoes_trabalho(self,barra_filtros):
        # opções 1
        barra_filtro_opcoes = ttk.Separator(barra_filtros, orient="vertical")
        barra_filtro_opcoes.grid(column=0, row=0, sticky="W")

        varaivel_opcoes = StringVar(barra_filtro_opcoes)

        label_opcoes = Label(barra_filtro_opcoes, text="Filtros")
        label_opcoes.grid(column=0, row=0, columnspan=2, sticky="W")

        rb_codigo = Radiobutton(barra_filtro_opcoes, text="Código", value="codigo", variable=varaivel_opcoes)
        rb_codigo.grid(column=0, row=1, sticky="W")

        rb_nome_pessoa_extra = Radiobutton(barra_filtro_opcoes, text="Nome/Pessoa extra", value="nome_pessoa_extra",
                                       variable=varaivel_opcoes)
        rb_nome_pessoa_extra.grid(column=0, row=2, sticky="W")

        rb_nome = Radiobutton(barra_filtro_opcoes, text="Nome", value="nome", variable=varaivel_opcoes)
        rb_nome.grid(column=0, row=3, sticky="W")

        rb_pessoa_extra = Radiobutton(barra_filtro_opcoes, text="Pessoa extra", value="pessoa_extra", variable=varaivel_opcoes)
        rb_pessoa_extra.grid(column=0, row=4, sticky="W")

        rb_cidade = Radiobutton(barra_filtro_opcoes, text="cidade", value="cidade", variable=varaivel_opcoes)
        rb_cidade.grid(column=1, row=1, sticky="W")

        rb_endereco = Radiobutton(barra_filtro_opcoes, text="endereco", value="endereco", variable=varaivel_opcoes)
        rb_endereco.grid(column=1, row=2, sticky="W")

        rb_cpf_cnpj = Radiobutton(barra_filtro_opcoes, text="cpf/cnpj", value="cpf_cnpj", variable=varaivel_opcoes)
        rb_cpf_cnpj.grid(column=1, row=3, sticky="W")

        rb_lote = Radiobutton(barra_filtro_opcoes, text="Lote", value="lote", variable=varaivel_opcoes)
        rb_lote.grid(column=1, row=4, sticky="W")

        rb_nome_pessoa_extra.select()

    def barra_filtros_status_pessoas(self, barra_filtros):
        barra_filtro_opcoes2 = ttk.Separator(barra_filtros, orient="vertical")
        barra_filtro_opcoes2.grid(column=1, row=0, sticky="W")

        varaivel_opcoes2 = StringVar(barra_filtro_opcoes2, value="nome_fantasia")

        label_opcoes2 = Label(barra_filtro_opcoes2, text="Status")
        label_opcoes2.grid(column=0, row=0, columnspan=2, sticky="W")

        rb_ativo = Radiobutton(barra_filtro_opcoes2, text="ativos", value="ativo", variable=varaivel_opcoes2)
        rb_ativo.grid(column=0, row=1, sticky="W")

        rb_terminado = Radiobutton(barra_filtro_opcoes2, text="Terminados", value="terminado",
                                   variable=varaivel_opcoes2)
        rb_terminado.grid(column=0, row=2, sticky="W")

        rb_todos = Radiobutton(barra_filtro_opcoes2, text="Todos", value="todos", variable=varaivel_opcoes2)
        rb_todos.grid(column=0, row=3, sticky="W")

        label_vazio = Label(barra_filtro_opcoes2, text="")
        label_vazio.grid(column=0, row=4, sticky="W")

        rb_ativo.select()

    def barra_filtros_status_trabalho(self, barra_filtros):
        barra_filtro_opcoes2 = ttk.Separator(barra_filtros, orient="vertical")
        barra_filtro_opcoes2.grid(column=1, row=0, sticky="W")

        varaivel_opcoes2 = StringVar(barra_filtro_opcoes2, value="nome_fantasia")

        label_opcoes2 = Label(barra_filtro_opcoes2, text="Status")
        label_opcoes2.grid(column=0, row=0, columnspan=2, sticky="W")

        rb_ativo = Radiobutton(barra_filtro_opcoes2, text="ativos", value="ativo", variable=varaivel_opcoes2)
        rb_ativo.grid(column=0, row=1, sticky="W")

        rb_terminado = Radiobutton(barra_filtro_opcoes2, text="Terminados", value="terminado",
                                   variable=varaivel_opcoes2)
        rb_terminado.grid(column=0, row=2, sticky="W")

        rb_todos = Radiobutton(barra_filtro_opcoes2, text="Todos", value="todos", variable=varaivel_opcoes2)
        rb_todos.grid(column=0, row=3, sticky="W")

        label_vazio = Label(barra_filtro_opcoes2, text="")
        label_vazio.grid(column=0, row=4, sticky="W")

        rb_ativo.select()

    def barra_filtros_pesquisa(self, barra_filtros):
        barra_filtro_opcoes3 = ttk.Separator(barra_filtros, orient="horizontal")
        barra_filtro_opcoes3.grid(column=2, row=0, sticky="NE")

        varaivel_opcoes3 = StringVar(barra_filtro_opcoes3)

        label_opcoes3 = Label(barra_filtro_opcoes3, text="Pesquisa")
        label_opcoes3.grid(column=0, row=0, sticky="N")

        rb_inicio = Radiobutton(barra_filtro_opcoes3, text="Inicio", value="inicio", variable=varaivel_opcoes3)
        rb_inicio.grid(column=0, row=1, sticky="E")

        rb_aproximacao = Radiobutton(barra_filtro_opcoes3, text="Aproximação", value="aproximacao",
                                     variable=varaivel_opcoes3)
        rb_aproximacao.grid(column=1, row=1, sticky="E")

        rb_qualquer_parte = Radiobutton(barra_filtro_opcoes3, text="Qualquer parte", value="qualquer_parte",
                                        variable=varaivel_opcoes3)
        rb_qualquer_parte.grid(column=2, row=1, sticky="E")

        rb_exato = Radiobutton(barra_filtro_opcoes3, text="Exato", value="exato", variable=varaivel_opcoes3)
        rb_exato.grid(column=3, row=1, sticky="E")

        rb_aproximacao.select()
    def buscar_pessoa_trabalho(self,janela_trabalhos):
        self.janela_pessoas(btn_grava_escolhe = "escolhe",janela_trabalhos = janela_trabalhos)

    def set_codigo_nome_trabalho(self,codigo,nome,janela_trabalhos):
        janela_trabalhos.destroy()
        self.codigo_pessoa_trabalho = codigo
        self.nome_pessoa_trabalho = nome
        self.novo_cadastro_trabalho()

    def novo_cadastro_trabalho(self):
        janela = Toplevel()
        janela.focus_force()

        janela.title("Cadastro Trabalho")

        self.configurar_janela_auxiliar(janela)

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        codigo = pega_ultimo_id("sessoes")

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")

        self.insert_entry_desabilitado(entry_codigo,codigo)

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
        entry_cadastro.insert(END,self.data_sistema)
        entry_cadastro.grid(column=1, row=1, padx=self.paddingx)

        lb_data_sessao = Label(separador1, text="Data da Sessão", font=self.lb_style)
        lb_data_sessao.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_data_sessao = Entry(separador1, font=self.entry_style, width=10)
        entry_data_sessao.insert(END,self.data_sistema)
        entry_data_sessao.grid(column=2, row=1, padx=self.paddingx)

        lb_horario_sessao = Label(separador1, text="Horário da Sessão", font=self.lb_style)
        lb_horario_sessao.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        entry_horario_sessao = Entry(separador1, font=self.entry_style, width=10)
        entry_horario_sessao.grid(column=3, row=1, padx=self.paddingx)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador2, text="Nome", font=self.lb_style)
        lb_nome.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=89)
        entry_nome.grid(column=1, row=1, padx=self.paddingx)

        separador3 = ttk.Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        # mudar para opções
        lb_tipo_sessao = Label(separador3, text="tipo da Sessão", font=self.lb_style)
        lb_tipo_sessao.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        cb_tipo_sessao = Entry(separador3, font=self.entry_style, width=20, state=DISABLED)
        #cb_tipo_sessao = ttk.Combobox(separador1, font=self.entry_style, width=15, values=tipos_possiveis, state="readonly")
        #cb_tipo_sessao.set("Ativo")
        cb_tipo_sessao.grid(column=1, row=1, padx=self.paddingx,sticky="W")

        lb_plano = Label(separador3, text="Plano", font=self.lb_style)
        lb_plano.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        cb_plano = Entry(separador3, font=self.entry_style, width=20, state=DISABLED)
        #cb_plano = ttk.Combobox(separador1, font=self.entry_style, width=15, values=planos_possiveis, state="readonly")
        #cb_plano.set("Ativo")
        cb_plano.grid(column=3, row=1, padx=self.paddingx,sticky="W")

        separador4 = ttk.Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        opcoes_pagamento = ['DINHEIRO','PIX', 'CARTÃO DÉBITO', 'CARTÃO CRÉDITO', 'OUTRO']

        lb_condicao_pagamento1 = Label(separador4, text="Condicao Pagamento", font=self.lb_style)
        lb_condicao_pagamento1.grid(column=0, row=0, sticky="W", padx=self.paddingx, columnspan=2)

        lb_valor = Label(separador4, text="Valor", font=self.lb_style)
        lb_valor.grid(column=3, row=0, sticky="W", padx=self.paddingx, columnspan=2)

        lb_total = Label(separador4, text="Total", font=self.lb_style)
        lb_total.grid(column=5, row=0, sticky="W", padx=self.paddingx)

        entry_total = Entry(separador4, font=self.entry_style, width=10,state=DISABLED)
        lb_aviso_valores = Label(separador4, text="", font=self.lb_style)
        lb_aviso_valores.grid(column=6, row=0, sticky="W", padx=self.paddingx)

        lb_condicao_pagamento_numero1 = Label(separador4, text="1º", font=self.lb_style)
        lb_condicao_pagamento_numero1.grid(column=0, row=1, padx=self.paddingx,pady=self.paddingy)
        cb_condicao_pagamento1 = ttk.Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento, state="readonly")
        cb_condicao_pagamento1.set("DINHEIRO")
        cb_condicao_pagamento1.grid(column=1, row=1, padx=self.paddingx,pady=self.paddingy)
        entry_valor1 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor1.grid(column=3, row=1, padx=self.paddingx,pady=self.paddingy)

        lb_condicao_pagamento_numero2 = Label(separador4, text="2º", font=self.lb_style)
        lb_condicao_pagamento_numero2.grid(column=0, row=2, padx=self.paddingx,pady=self.paddingy)
        cb_condicao_pagamento2 = ttk.Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento, state="readonly")
        cb_condicao_pagamento2.set("DINHEIRO")
        cb_condicao_pagamento2.grid(column=1, row=2, padx=self.paddingx,pady=self.paddingy)
        entry_valor2 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor2.grid(column=3, row=2, padx=self.paddingx,pady=self.paddingy)


        lb_condicao_pagamento_numero3 = Label(separador4, text="3º", font=self.lb_style)
        lb_condicao_pagamento_numero3.grid(column=0, row=3, padx=self.paddingx,pady=self.paddingy)
        cb_condicao_pagamento3 = ttk.Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento, state="readonly")
        cb_condicao_pagamento3.set("DINHEIRO")
        cb_condicao_pagamento3.grid(column=1, row=3, padx=self.paddingx,pady= self.paddingy)
        entry_valor3 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor3.grid(column=3, row=3, padx=self.paddingx,pady=self.paddingy)

        def soma_condicao_pagamento(event):
            try:
                valor1 = entry_valor1.get().replace(",",".")
                valor2 = entry_valor2.get().replace(",",".")
                valor3 = entry_valor3.get().replace(",",".")
                lb_aviso_valores['text'] = "."
                self.valores_pagamento = []
                if valor1 == '':
                    valor1 = "0"
                    valor1=float(valor1)
                else:
                    valor1=float(valor1)

                if valor2 == '':
                    valor2 = "0"
                    valor2=float(valor2)
                else:
                    valor2=float(valor2)

                if valor3 == '':
                    valor3 = "0"
                    valor3=float(valor3)
                else:
                    valor3=float(valor3)

                total = str(valor1+valor2+valor3)
                self.valores_pagamento.append(valor1)
                self.valores_pagamento.append(valor2)
                self.valores_pagamento.append(valor3)
                self.insert_entry_desabilitado(entry_total, total, 0)
                return
            except ValueError:
                lb_aviso_valores['text'] = "VERIFIQUE OS VALORES DO PAGAMENTO"

        entry_valor1.bind("<FocusOut>",soma_condicao_pagamento)
        entry_valor2.bind("<FocusOut>",soma_condicao_pagamento)
        entry_valor3.bind("<FocusOut>",soma_condicao_pagamento)

        entry_total.grid(column=5, row=3, padx=self.paddingx,pady=self.paddingy)

        separador5 = ttk.Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_observacoes = Label(separador5, text="Observações", font=self.lb_style)
        lb_observacoes.grid(column=0, row=0, padx=self.paddingx,pady=self.paddingy,sticky="W")
        textarea_observacoes = Text(separador5, font=self.entry_style, height=6)
        textarea_observacoes.grid(column=0, row=1, padx=self.paddingx,pady= self.paddingy,sticky="W")

        def coleta_argumentos():
            argumentos = []
            argumentos.append(entry_codigo.get())
            argumentos.append(entry_cadastro.get())
            argumentos.append(entry_data_sessao.get())
            argumentos.append(entry_horario_sessao.get())
            argumentos.append(entry_nome.get())
            argumentos.append(self.codigo_pessoa_trabalho)
            argumentos.append(cb_tipo_sessao.get())
            argumentos.append(cb_plano.get())
            argumentos.append(entry_valor1.get())
            argumentos.append(entry_valor2.get())
            argumentos.append(entry_valor3.get())
            argumentos.append(entry_total.get())
            argumentos.append(textarea_observacoes.get("1.0","end-1c"))
            self.argumentos = argumentos
        def buscar_pessoa_trabalho_args():
            coleta_argumentos()
            self.buscar_pessoa_trabalho(janela)

        bt_busca_pessoa = Button(separador2, text="busca", font=self.btn_style, command=buscar_pessoa_trabalho_args)
        bt_busca_pessoa.grid(column=0, row=1)

        def buscar_tipos_sessao_trabalho_args():
            coleta_argumentos()
            self.buscar_tipos_sessao_trabalho(tipo = "escolha",janela_trabalhos=janela)


        bt_busca_sessao = Button(separador3, text="busca", font=self.btn_style, command=buscar_tipos_sessao_trabalho_args)
        bt_busca_sessao.grid(column=0, row=1)
        def buscar_plano_sessao_trabalho_args():
            coleta_argumentos()
            self.buscar_plano_trabalho(tipo = "escolha",janela_trabalhos=janela)

        bt_busca_plano = Button(separador3, text="busca", font=self.btn_style, command=buscar_plano_sessao_trabalho_args)
        bt_busca_plano.grid(column=2, row=1)

        separador9 = ttk.Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)
        if self.argumentos is not None:
            self.insert_entry_desabilitado(entry_codigo,self.argumentos[0])
            self.set_text_entry(entry_cadastro,self.argumentos[1])
            self.set_text_entry(entry_data_sessao,self.argumentos[2])
            self.set_text_entry(entry_horario_sessao,self.argumentos[3])
            self.set_text_entry(entry_nome,self.nome_pessoa_trabalho)
            self.insert_entry_desabilitado(cb_tipo_sessao,self.nome_tipo_trabalho)
            self.insert_entry_desabilitado(cb_plano,self.nome_plano_trabalho)
            self.set_text_entry(entry_valor1,self.argumentos[8])
            self.set_text_entry(entry_valor2,self.argumentos[9])
            self.set_text_entry(entry_valor3,self.argumentos[10])
            self.insert_entry_desabilitado(entry_total,self.argumentos[11])
            self.set_textarea(textarea_observacoes,self.argumentos[12])
        def grava_db_trabalho_args():
            self.argumentos = None
            grava_db_trabalhos(entry_codigo.get,entry_cadastro.get,entry_data_sessao.get,entry_horario_sessao.get,self.codigo_pessoa_trabalho,entry_nome.get,cb_tipo_sessao.get,self.codigo_tipo_trabalho,cb_plano.get,self.codigo_plano_trabalho,cb_condicao_pagamento1.get,self.valores_pagamento[0],cb_condicao_pagamento2.get,self.valores_pagamento[1],cb_condicao_pagamento3.get,self.valores_pagamento[2],entry_total.get,textarea_observacoes.get)
            janela.destroy()

        grava = Button(separador9, text="GRAVA", font=self.lb_style, command=grava_db_trabalho_args)
        grava.grid(column=0, row=0, sticky="WS")

        def cancelar():
            self.argumentos = None
            janela.destroy()


        cancela = Button(separador9, text="CANCELA", font=self.lb_style, command=cancelar)
        cancela.grid(column=1, row=0, sticky="WS")

    def cria_lista_de_pessoas(self,janela):
        lista = pega_todas_pessoas_lista()

        lista_pessoas = ttk.Treeview(janela, columns=("col0","col1", "col2", "col3"))
        lista_pessoas.heading("#0", text="")
        lista_pessoas.heading("#1", text="Cod")
        lista_pessoas.heading("#2", text="Nome")
        lista_pessoas.heading("#3", text="CPF/CNPJ")
        lista_pessoas.heading("#4", text="Cidade")

        lista_pessoas.column("#0", width=0)
        lista_pessoas.column("#1", width=50)
        lista_pessoas.column("#2", width=450)
        lista_pessoas.column("#3", width=204)
        lista_pessoas.column("#4", width=300)

        for i in lista:
            lista_pessoas.insert("",END,values=i)


        lista_pessoas.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(janela, orient="vertical")
        lista_pessoas.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")

        self.lista_de_pessoas = lista_pessoas
    def lista_de_trabalho(self,janela):

        lista_pessoas = ttk.Treeview(janela, columns=("col1", "col2", "col3","col4","col5","col6"))
        lista_pessoas.heading("#0", text="Cod")
        lista_pessoas.heading("#1", text="Data")
        lista_pessoas.heading("#2", text="hora")
        lista_pessoas.heading("#3", text="Nome")
        lista_pessoas.heading("#4", text="Pessoas")
        lista_pessoas.heading("#5", text="Tipo sessão")
        lista_pessoas.heading("#6", text="Etapa")

        lista_pessoas.column("#0", width=50)
        lista_pessoas.column("#1", width=100)
        lista_pessoas.column("#2", width=100)
        lista_pessoas.column("#3", width=300)
        lista_pessoas.column("#4", width=200)
        lista_pessoas.column("#5", width=127)
        lista_pessoas.column("#6", width=128)

        lista_pessoas.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(janela, orient="vertical")
        lista_pessoas.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")
    def lista_de_trabalho_financeiro(self,janela):
        trabalho = [1, "vitor", "091.861.449-01", "são jorge do ivai"]
        #codigo, lote + sessao, pessoa,condicao, valor, pago

        lista_pessoas = ttk.Treeview(janela, columns=("col1", "col2", "col3", "col4", "col5"))
        lista_pessoas.heading("#0", text="Cod")
        lista_pessoas.heading("#1", text="Lote + Sessao")
        lista_pessoas.heading("#2", text="Pessoa")
        lista_pessoas.heading("#3", text="Condicao")
        lista_pessoas.heading("#4", text="Valor")
        lista_pessoas.heading("#5", text="Pago")

        lista_pessoas.column("#0", width=50)
        lista_pessoas.column("#1", width=90)
        lista_pessoas.column("#2", width=300)
        lista_pessoas.column("#3", width=200)
        lista_pessoas.column("#4", width=100)
        lista_pessoas.column("#5", width=100)

        lista_pessoas.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(janela, orient="vertical")
        lista_pessoas.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")

    def informacoes_adicionais_pessoas(self,janela, pessoa = None):
        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", side=BOTTOM, padx=self.paddingx, pady=self.paddingy+10)

        lb_nome_razao = Label(separador1, text="Nome/Razão Social", font=self.lb_style)
        lb_nome_razao.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_nome_razao = Entry(separador1, font=self.entry_style, width=50, state=DISABLED)
        entry_nome_razao.grid(column=1, row=0, padx=self.paddingx)

        lb_fantasia_apelido = Label(separador1, text="Fantasia/Apelido", font=self.lb_style)
        lb_fantasia_apelido.grid(column=0, row=1, sticky="NW", padx=self.paddingx)
        entry_fantasia_apelido = Entry(separador1, font=self.entry_style, width=50, state=DISABLED)
        entry_fantasia_apelido.grid(column=1, row=1, padx=self.paddingx)

        lb_fone1 = Label(separador1, text="Fone 1", font=self.lb_style)
        lb_fone1.grid(column=2, row=0, sticky="NW", padx=self.paddingx)
        entry_fone1 = Entry(separador1, font=self.entry_style, width=20, state=DISABLED)
        entry_fone1.grid(column=3, row=0, padx=self.paddingx)

        lb_fone2 = Label(separador1, text="Fone 2", font=self.lb_style)
        lb_fone2.grid(column=2, row=1, sticky="NW", padx=self.paddingx)
        entry_fone2 = Entry(separador1, font=self.entry_style, width=20, state=DISABLED)
        entry_fone2.grid(column=3, row=1, padx=self.paddingx)

        lb_fone3 = Label(separador1, text="Fone 3", font=self.lb_style)
        lb_fone3.grid(column=2, row=2, sticky="NW", padx=self.paddingx)
        entry_fone3 = Entry(separador1, font=self.entry_style, width=20, state=DISABLED)
        entry_fone3.grid(column=3, row=2, padx=self.paddingx)

        separador_endereco = ttk.Separator(separador1, orient="horizontal")
        separador_endereco.grid(column=0, row=2, padx=self.paddingx, sticky="ew",columnspan=2)

        lb_endereco = Label(separador_endereco, text="Endereço", font=self.lb_style)
        lb_endereco.pack(side=LEFT)
        #lb_endereco.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_endereco = Entry(separador_endereco, font=self.entry_style, width=41, state=DISABLED)

        #entry_endereco.grid(column=1, row=0, padx=self.paddingx, sticky="ew")

        lb_numero = Label(separador_endereco, text="N.", font=self.lb_style)
        #lb_numero.grid(column=2, row=0, sticky="EW", padx=self.paddingx)

        entry_numero = Entry(separador_endereco, font=self.entry_style, width=6, state=DISABLED)
        entry_numero.pack(side=RIGHT,padx=1)
        lb_numero.pack(side=RIGHT,padx=3)
        entry_endereco.pack(side=RIGHT)
        #entry_numero.grid(column=3, row=0, padx=self.paddingx, sticky="ew")

        return entry_nome_razao, entry_fantasia_apelido, entry_fone1, entry_fone2, entry_fone3,entry_endereco,entry_numero

    #modificar assim que tiver as informações do que colocar
    def informacoes_adicionais_trabalho(self,janela, trabalho = None):
        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", side=BOTTOM, padx=self.paddingx, pady=self.paddingy+10)

        separador2 = ttk.Separator(separador1, orient="horizontal")
        separador2.grid(column=0,row=0,rowspan=3)

        lb_observacoes = Label(separador2, text="Observações", font=self.lb_style)
        lb_observacoes.grid(column=0, row=0, sticky="NW", padx=self.paddingx, rowspan=3)
        entry_observacoes = Text(separador2, font=self.entry_style, width=78,height=3, state=DISABLED,pady=self.paddingy)
        entry_observacoes.grid(column=1, row=0, padx=self.paddingx,sticky="NW")

        separador3 = ttk.Separator(separador2, orient="horizontal")
        separador3.grid(column=1, row = 0,rowspan=3,sticky="E")

        lb_valor = Label(separador3, text="Valor", font=self.lb_style)
        lb_valor.grid(column=0, row=0, sticky="NE", padx=self.paddingx)
        entry_valor = Entry(separador3, font=self.entry_style, width=10, state=DISABLED)
        entry_valor.grid(column=1, row=0, padx=self.paddingx)

        lb_pago = Label(separador3, text="Pago", font=self.lb_style)
        lb_pago.grid(column=0, row=1, sticky="NE", padx=self.paddingx)
        entry_pago = Entry(separador3, font=self.entry_style, width=10, state=DISABLED)
        entry_pago.grid(column=1, row=1, padx=self.paddingx)

        lb_devendo = Label(separador3, text="Devendo", font=self.lb_style)
        lb_devendo.grid(column=0, row=2, sticky="NE", padx=self.paddingx)
        entry_devendo = Entry(separador3, font=self.entry_style, width=10, state=DISABLED)
        entry_devendo.grid(column=1, row=2, padx=self.paddingx)


        # entry_numero.grid(column=3, row=0, padx=self.paddingx, sticky="ew")
    def buscar_plano_trabalho(self,tipo = "escolha",janela_trabalhos=None):

        janela = Toplevel()
        self.configurar_janela_auxiliar2(janela)
        janela.title("Planos")

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", pady=self.paddingy)

        funcoes = [self.novo_cadastro_plano, self.altera_cadastro_plano, self.exclui_cadastro_plano]

        barra_alteracoes = self.barra_alteracoes(separador1, funcoes)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x")

        lista_planos = ttk.Treeview(separador2, columns=("col1", "col2"), padding=(0,0,0,25))
        lista_planos.heading("#0", text="")
        lista_planos.heading("#1", text="Cod")
        lista_planos.heading("#2", text="Nome")

        lista_planos.column("#0", width=0)
        lista_planos.column("#1", width=50)
        lista_planos.column("#2", width=442)

        lista = pega_todos_planos_sessoes_lista()

        for i in lista:
            lista_planos.insert("",END,values=i)

        lista_planos.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(separador2, orient="vertical")
        lista_planos.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")

        self.lista_planos = lista_planos

        if tipo == "escolha":
            def funcao(event):
                plano = None
                for selected_item in self.lista_planos.selection():
                    item = self.lista_planos.item(selected_item, 'values')
                    plano = pega_um_item_plano(item[0])
                    self.codigo_plano_trabalho = plano[0][0]
                    self.nome_plano_trabalho = plano[0][1]
                    janela.destroy()
                    janela_trabalhos.destroy()
                    self.novo_cadastro_trabalho()
                    return False

            self.lista_planos.bind("<Double-1>", funcao)
    def buscar_tipos_sessao_trabalho(self, tipo = None,janela_trabalhos = None):

        janela = Toplevel()
        self.configurar_janela_auxiliar2(janela)
        janela.title("Tipos")

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", pady=self.paddingy)

        funcoes = [self.novo_cadastro_tipo, self.altera_cadastro_tipo, self.exclui_cadastro_tipo]

        barra_alteracoes = self.barra_alteracoes(separador1, funcoes)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x")

        lista_tipos = ttk.Treeview(separador2, columns=("col1", "col2","col3"), padding=(0,0,0,25))
        lista_tipos.heading("#0", text="")
        lista_tipos.heading("#1", text="Cod")
        lista_tipos.heading("#2", text="Nome")
        lista_tipos.heading("#3", text="Descrição")

        lista_tipos.column("#0", width=0)
        lista_tipos.column("#1", width=50)
        lista_tipos.column("#2", width=100)
        lista_tipos.column("#3", width=342)

        lista = pega_todos_tipos_sessoes_lista()

        for i in lista:
            lista_tipos.insert("",END,values=i)

        lista_tipos.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(separador2, orient="vertical")
        lista_tipos.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")

        self.lista_tipos = lista_tipos

        if tipo == "escolha":
            def funcao(event):
                tipo = None
                for selected_item in self.lista_tipos.selection():
                    item = self.lista_tipos.item(selected_item, 'values')
                    tipo = pega_um_item_tipo(item[0])
                    self.codigo_tipo_trabalho = tipo[0][0]
                    self.nome_tipo_trabalho = tipo[0][1]
                    janela.destroy()
                    janela_trabalhos.destroy()
                    self.novo_cadastro_trabalho()
                    return False

            self.lista_tipos.bind("<Double-1>", funcao)

    def janela_pessoas(self,btn_grava_escolhe = None, janela_trabalhos = None):
        janela_pessoas = Toplevel()

        self.configurar_janela_auxiliar(janela_pessoas)
        funcoes = [self.novo_cadastro_pessoa,self.altera_cadastro_pessoa, self.exclui_cadastro_pessoa]

        barra_alteracoes = self.barra_alteracoes(janela_pessoas, funcoes)

        barra_filtros = ttk.Separator(janela_pessoas, orient="horizontal")
        barra_filtros.pack(fill="x")

        listagem_pessoas = ttk.Separator(janela_pessoas, orient="horizontal")
        listagem_pessoas.pack(fill="x")

        self.barra_filtros_opcoes_pessoas(barra_filtros)
        self.barra_filtros_status_pessoas(barra_filtros)
        self.barra_filtros_pesquisa(barra_filtros)
        self.cria_lista_de_pessoas(listagem_pessoas)
        entry_nome_razao, entry_fantasia_apelido, entry_fone1, entry_fone2, entry_fone3,entry_endereco,entry_numero = self.informacoes_adicionais_pessoas(janela_pessoas)
        def adiciona_informacoes_adicionais(event):

            for selected_item in self.lista_de_pessoas.selection():
                item = self.lista_de_pessoas.item(selected_item,'values')
                pessoa = pega_um_item_pessoa(item[0])

                self.insert_entry_desabilitado(entry_nome_razao,pessoa[0][2])
                self.insert_entry_desabilitado(entry_fantasia_apelido, pessoa[0][6])
                self.insert_entry_desabilitado(entry_fone1, pessoa[0][16])
                self.insert_entry_desabilitado(entry_fone2, pessoa[0][18])
                self.insert_entry_desabilitado(entry_fone3, pessoa[0][20])
                self.insert_entry_desabilitado(entry_endereco, pessoa[0][9])
                self.insert_entry_desabilitado(entry_numero, pessoa[0][10])

        if btn_grava_escolhe == "escolhe":
            def funcao(event):
                pessoa = None
                for selected_item in self.lista_de_pessoas.selection():
                    item = self.lista_de_pessoas.item(selected_item, 'values')
                    pessoa = pega_um_item_pessoa(item[0])
                    self.codigo_pessoa_trabalho = pessoa[0][0]
                    self.set_codigo_nome_trabalho(pessoa[0][0],pessoa[0][2],janela_trabalhos)
                    janela_pessoas.destroy()
                    return False

            self.lista_de_pessoas.bind("<Double-1>", funcao)

        self.lista_de_pessoas.bind("<Button-1>", adiciona_informacoes_adicionais)

        janela_pessoas.title("Pesquisa de Pessoas")

    def janela_trabalhos(self):
        janela_trabalhos = Toplevel()
        self.configurar_janela_auxiliar(janela_trabalhos)

        data_hoje = date.today().strftime("%d/%m/%Y")

        funcoes = [self.novo_cadastro_trabalho, self.altera_cadastro_trabalho, self.exclui_cadastro_trabalho]

        barra_alteracoes = self.barra_alteracoes(janela_trabalhos,funcoes)

        bt_planos = Button(barra_alteracoes, text="Planos",padx=5,pady=10,font=("monospace", 10), command=self.buscar_tipos_sessao_trabalho)
        bt_planos.pack(side = LEFT, padx=self.paddingx+20)

        barra_filtros = ttk.Separator(janela_trabalhos, orient="horizontal")
        barra_filtros.pack(fill="x")

        listagem_trabalhos = ttk.Separator(janela_trabalhos, orient="horizontal")
        listagem_trabalhos.pack(fill="x")

        self.barra_filtros_opcoes_trabalho(barra_filtros)
        self.barra_filtros_status_trabalho(barra_filtros)
        self.barra_filtros_pesquisa(barra_filtros)
        self.lista_de_trabalho(listagem_trabalhos)
        self.informacoes_adicionais_trabalho(janela_trabalhos)


        janela_trabalhos.title("Pesquisa de Trabalhos")

    def janela_financeiro(self):
        janela_financeiro = Toplevel()
        self.configurar_janela_auxiliar(janela_financeiro)
        funcoes = [self.novo_financeiro,self.altera_financeiro, self.exclui_financeiro]

        self.barra_alteracoes(janela_financeiro,funcoes)

        listagem_trabalhos_financeiro = ttk.Separator(janela_financeiro, orient="horizontal")
        listagem_trabalhos_financeiro.pack(fill="x")

        self.lista_de_trabalho_financeiro(listagem_trabalhos_financeiro)

        janela_financeiro.title("Controle Financeiro")

    def set_text_entry(self, entry, texto):
        if texto is None:
            texto = ""
        entry.delete(0, END)
        entry.insert(0, texto)
        return
    def set_textarea(self, entry, texto):
        entry.delete(1.0, "end-1c")
        entry.insert("end-1c", texto)
        return

'''def barra_menu(janela):
    menus = Menu(janela) 

    menuCadastroClientes = Menu(menus)
    menuCadastroClientes.add_command(label="Cadastros",command=sem_comando)

    menuFinalizar = Menu(menus)
    menuFinalizar.add_command(label="Cadastros",command=sem_comando)

    return menus'''

if __name__ == '__main__':

    Aplicacao()


