from modulos.auxiliares import Funcs
from modulos.database import pega_um_item_pessoa, pega_ultimo_id, grava_db_pessoa, altera_db_pessoa, deleta_db_pessoa, \
    pega_todas_pessoas_lista

from tkinter import Toplevel, StringVar, Entry, Label, DISABLED, END, RIGHT, NW, Button, Radiobutton, LEFT, BOTTOM
from tkinter.ttk import Separator, Combobox, Treeview, Scrollbar


class Pessoas(Funcs):
    def __init__(self, janela_trabalhos = None):
        super().__init__()
        self.janela_pessoas_var = None
        self.lista_de_pessoas = None
        self.argumentos = None
        self.janela_trabalhos_var = janela_trabalhos

    def novo_cadastro_pessoa(self):
        janela = Toplevel()
        janela.bind("<Return>", self.next_focus)
        variavel_upercase = StringVar()

        janela.title("Cadastro Pessoas")

        self.configurar_janela_auxiliar(janela)

        separador1 = Separator(janela, orient="horizontal")
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
        cb_status = Combobox(separador1, font=self.entry_style, width=15, values=status_possiveis, state="readonly")
        cb_status.set("Ativo")
        cb_status.grid(column=2, row=1, padx=self.paddingx)

        # mudar para opções
        lb_tipo = Label(separador1, text="Tipo", font=self.lb_style)
        lb_tipo.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        cb_tipo = Combobox(separador1, font=self.entry_style, width=15, values=tipos_possiveis_pessoas,
                               state="readonly")
        cb_tipo.set("Física")
        cb_tipo.grid(column=3, row=1, padx=self.paddingx)

        separador2 = Separator(janela, orient="horizontal")
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

        separador3 = Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador3, text="Nome*", font=self.lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador3, font=self.entry_style, width=89)
        entry_nome.grid(column=0, row=1, padx=self.paddingx)

        lb_apelido = Label(separador3, text="Apelido", font=self.lb_style)
        lb_apelido.grid(column=0, row=2, sticky="W", padx=self.paddingx)
        entry_apelido = Entry(separador3, font=self.entry_style, width=89)
        entry_apelido.grid(column=0, row=3, padx=self.paddingx)

        separador4 = Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_endereco = Label(separador4, text="Endereço", font=self.lb_style)
        lb_endereco.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_endereco = Entry(separador4, font=self.entry_style, width=82)
        entry_endereco.grid(column=0, row=1, padx=self.paddingx)

        lb_numero = Label(separador4, text="Numero", font=self.lb_style)
        lb_numero.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_numero = Entry(separador4, font=self.entry_style, width=5)
        entry_numero.grid(column=1, row=1, padx=self.paddingx)

        separador5 = Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_complemento = Label(separador5, text="Complemento", font=self.lb_style)
        lb_complemento.grid(column=0, row=2, sticky="W", padx=self.paddingx)
        entry_complemento = Entry(separador5, font=self.entry_style, width=44)
        entry_complemento.grid(column=0, row=3, padx=self.paddingx)

        lb_bairro = Label(separador5, text="Bairro", font=self.lb_style)
        lb_bairro.grid(column=1, row=2, sticky="W", padx=self.paddingx)
        entry_bairro = Entry(separador5, font=self.entry_style, width=43)
        entry_bairro.grid(column=1, row=3, padx=self.paddingx)

        separador6 = Separator(janela, orient="horizontal")
        separador6.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

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

        separador7 = Separator(janela, orient="horizontal")
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

        separador8 = Separator(janela, orient="horizontal")
        separador8.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_email = Label(separador8, text="Email", font=self.lb_style)
        lb_email.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_email = Entry(separador8, font=self.entry_style, width=89)
        entry_email.grid(column=0, row=1, padx=self.paddingx)

        lb_campos_obrigatorios = Label(janela, text="(*) Campos Obrigatórios")
        lb_campos_obrigatorios.pack(fill="x", side=RIGHT, anchor=NW)

        separador9 = Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)

        def grava_db_pessoa_args():
            if self.confirmacao_salvamento(janela):
                grava_db_pessoa(entry_codigo.get, entry_cadastro.get, cb_status.get, cb_tipo.get, entry_cpf_cnpj.get,
                                entry_rg_inscricao.get, entry_nascimento.get, entry_nome.get, entry_apelido.get,
                                entry_endereco.get, entry_complemento.get, entry_bairro.get, entry_nome_cidade.get,
                                entry_uf.get, entry_cep.get, entry_fone1.get, entry_fone2.get, entry_fone3.get,
                                entry_operadora1.get, entry_operadora2.get, entry_operadora3.get, entry_email.get,
                                entry_numero.get)

                janela.destroy()
                self.janela_pessoas_var.destroy()
                self.janela_pessoas()

        grava = Button(separador9, text="GRAVA", font=self.lb_style, command=grava_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")
        def cancelar():
            if self.confirmacao_cancelamento(janela):
                janela.destroy()
                self.janela_pessoas_var.destroy()
                self.janela_pessoas()

        cancela = Button(separador9, text="CANCELA", font=self.lb_style, command= cancelar)
        cancela.grid(column=1, row=0, sticky="WS")

    def altera_cadastro_pessoa(self):
        pessoa = self.seleciona_item_pessoas()

        if pessoa is None:
            return

        janela = Toplevel()
        janela.bind("<Return>", self.next_focus)
        variavel_upercase = StringVar()

        janela.title("Cadastro Pessoas")

        self.configurar_janela_auxiliar(janela)

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

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
        cb_status = Combobox(separador1, font=self.entry_style, width=15, values=status_possiveis, state="readonly")
        cb_status.set(pessoa[0][3])
        cb_status.grid(column=2, row=1, padx=self.paddingx)

        # mudar para opções
        lb_tipo = Label(separador1, text="Tipo", font=self.lb_style)
        lb_tipo.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        cb_tipo = Combobox(separador1, font=self.entry_style, width=15, values=tipos_possiveis_pessoas,
                               state="readonly")
        cb_tipo.set(pessoa[0][4])
        cb_tipo.grid(column=3, row=1, padx=self.paddingx)

        separador2 = Separator(janela, orient="horizontal")
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

        separador3 = Separator(janela, orient="horizontal")
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

        separador4 = Separator(janela, orient="horizontal")
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

        separador5 = Separator(janela, orient="horizontal")
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

        separador6 = Separator(janela, orient="horizontal")
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

        separador7 = Separator(janela, orient="horizontal")
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

        separador8 = Separator(janela, orient="horizontal")
        separador8.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_email = Label(separador8, text="Email", font=self.lb_style)
        lb_email.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_email = Entry(separador8, font=self.entry_style, width=89)
        entry_email.grid(column=0, row=1, padx=self.paddingx)
        entry_email.insert(END, pessoa[0][22])

        lb_campos_obrigatorios = Label(janela, text="(*) Campos Obrigatórios")
        lb_campos_obrigatorios.pack(fill="x", side=RIGHT, anchor=NW)

        separador9 = Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)
        def altera_db_pessoa_args():
            if self.confirmacao_salvamento(janela):
                altera_db_pessoa(entry_codigo.get, entry_cadastro.get, cb_status.get,cb_tipo.get, entry_cpf_cnpj.get, entry_rg_inscricao.get, entry_nascimento.get,entry_nome.get, entry_apelido.get, entry_endereco.get, entry_complemento.get,entry_bairro.get, entry_nome_cidade.get, entry_uf.get,entry_cep.get, entry_fone1.get, entry_fone2.get, entry_fone3.get,entry_operadora1.get, entry_operadora2.get,entry_operadora3.get, entry_email.get, entry_numero.get)

                janela.destroy()
                self.janela_pessoas_var.destroy()
                self.janela_pessoas()

        grava = Button(separador9, text="GRAVA", font=self.lb_style, command=altera_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")
        def cancelar():
            if self.confirmacao_cancelamento(janela):
                janela.destroy()
                self.janela_pessoas_var.destroy()
                self.janela_pessoas()

        cancela = Button(separador9, text="CANCELA", font=self.lb_style, command= cancelar)
        cancela.grid(column=1, row=0, sticky="WS")

    def exclui_cadastro_pessoa(self):
        pessoa = self.seleciona_item_pessoas()
        id = pessoa[0][0]

        if self.confirmacao_exclusao(frase="", valor=pessoa[0][2], janela_principal=self.janela_pessoas_var):

            deleta_db_pessoa(id)
            self.janela_pessoas_var.destroy()
            self.janela_pessoas()

    def seleciona_item_pessoas(self):
        for selected_item in self.lista_de_pessoas.selection():
            item = self.lista_de_pessoas.item(selected_item)
            record = item['values']
            pessoa = pega_um_item_pessoa(record[0])
            return pessoa

    def barra_filtros_opcoes_pessoas(self,barra_filtros):
        # opções 1
        barra_filtro_opcoes = Separator(barra_filtros, orient="vertical")
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

    def barra_filtros_status_pessoas(self, barra_filtros):
        barra_filtro_opcoes2 = Separator(barra_filtros, orient="vertical")
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

    def cria_lista_de_pessoas(self,janela):
        lista = pega_todas_pessoas_lista()

        lista_pessoas = Treeview(janela, columns=("col0","col1", "col2", "col3"))
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

    def informacoes_adicionais_pessoas(self,janela, pessoa = None):
        separador1 = Separator(janela, orient="horizontal")
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

        separador_endereco = Separator(separador1, orient="horizontal")
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

    def janela_pessoas(self,btn_grava_escolhe = None):
        janela_pessoas = Toplevel()

        self.configurar_janela_auxiliar(janela_pessoas)
        funcoes = [self.novo_cadastro_pessoa,self.altera_cadastro_pessoa, self.exclui_cadastro_pessoa]

        barra_alteracoes = self.barra_alteracoes(janela_pessoas, funcoes)

        barra_filtros = Separator(janela_pessoas, orient="horizontal")
        barra_filtros.pack(fill="x")

        listagem_pessoas = Separator(janela_pessoas, orient="horizontal")
        listagem_pessoas.pack(fill="x")

        self.barra_filtros_opcoes_pessoas(barra_filtros)
        self.barra_filtros_status_pessoas(barra_filtros)
        self.barra_filtros_pesquisa(barra_filtros)
        self.cria_lista_de_pessoas(listagem_pessoas)
        entry_nome_razao, entry_fantasia_apelido, entry_fone1, entry_fone2, entry_fone3,entry_endereco,entry_numero = self.informacoes_adicionais_pessoas(janela_pessoas)

        self.janela_pessoas_var = janela_pessoas
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
                    self.janela_trabalhos_var.set_argumentos_nome_trabalho(pessoa[0][0], pessoa[0][2])
                    self.janela_pessoas_var.destroy()
                    return

            self.lista_de_pessoas.bind("<Double-1>", funcao)

        self.lista_de_pessoas.bind("<Button-1>", adiciona_informacoes_adicionais)

        janela_pessoas.title("Pesquisa de Pessoas")