from tkinter import *
from tkinter import ttk
from datetime import date
class Funcs():
    def __init__(self):
        self.lb_style = ("monospace", 12)
        self.paddingx = 10
        self.paddingy = 7
        self.entry_style = ("monospace", 14)
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
#modificar para ficar no meio da tela
        x = int((screen_width / 2) - (964 / 2) - 50)
        y = int((screen_height / 2) - (580 / 2) - 50)

        janela.geometry("+%d+%d" % (x, y))

        janela.geometry("512x312")
        janela.resizable(False,False)

    def novo_cadastro_pessoa(self):
        janela = Toplevel()

        janela.title("Cadastro Pessoas")

        self.configurar_janela_auxiliar(janela)

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
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
        entry_operadora1 = Entry(separador7, font=self.entry_style, width=width_operadora)
        entry_operadora1.grid(column=3, row=1, padx=self.paddingx)

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

        grava = Button(separador9, text="GRAVA", font=self.lb_style)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador9, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")

    def novo_cadastro_tabalho(self):
        janela = Toplevel()

        janela.title("Cadastro Trabalhos")

        lb_style = ("monospace", 12)
        entry_style = ("monospace", 14)
        paddingx = 10
        paddingy = 7

        self.configurar_janela_auxiliar(janela)

        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=paddingx, pady=paddingy)

        lb_codigo = Label(separador1, text="Código", font=lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=paddingx)
        entry_codigo = Entry(separador1, font=entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=paddingx, sticky="NW")

        lb_cadastro = Label(separador1, text="Cadastro", font=lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=paddingx)
        entry_cadastro = Entry(separador1, font=entry_style, width=10)
        entry_cadastro.grid(column=1, row=1, padx=paddingx)

        status_possiveis = ["Ativo", "Inativo"]
        tipos_possiveis_pessoas = ["Física", "Jurídica"]

        # mudar para opções
        lb_status = Label(separador1, text="Status", font=lb_style)
        lb_status.grid(column=2, row=0, sticky="W", padx=paddingx)
        cb_status = ttk.Combobox(separador1, font=entry_style, width=15, values=status_possiveis, state="readonly")
        cb_status.set("Ativo")
        cb_status.grid(column=2, row=1, padx=paddingx)

        # mudar para opções
        lb_tipo = Label(separador1, text="Tipo", font=lb_style)
        lb_tipo.grid(column=3, row=0, sticky="W", padx=paddingx)
        cb_tipo = ttk.Combobox(separador1, font=entry_style, width=15, values=tipos_possiveis_pessoas, state="readonly")
        cb_tipo.set("Física")
        cb_tipo.grid(column=3, row=1, padx=paddingx)

        separador2 = ttk.Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=paddingx, pady=paddingy)

        # condicao para mudar quando for tipo juridica
        lb_cpf_cnpj = Label(separador2, text="CPF", font=lb_style)
        lb_cpf_cnpj.grid(column=0, row=0, sticky="W", padx=paddingx)
        entry_cpf_cnpj = Entry(separador2, font=entry_style, width=20)
        entry_cpf_cnpj.grid(column=0, row=1, padx=paddingx)

        # condicao para mudar quando for tipo juridica
        lb_rg_inscricao = Label(separador2, text="RG", font=lb_style)
        lb_rg_inscricao.grid(column=1, row=0, sticky="W", padx=paddingx)
        entry_rg_inscricao = Entry(separador2, font=entry_style, width=20)
        entry_rg_inscricao.grid(column=1, row=1, padx=paddingx)

        lb_nascimento = Label(separador2, text="Nascimento", font=lb_style)
        lb_nascimento.grid(column=2, row=0, sticky="W", padx=paddingx)
        entry_nascimento = Entry(separador2, font=entry_style, width=10)
        entry_nascimento.grid(column=2, row=1, padx=paddingx)

        separador3 = ttk.Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=paddingx, pady=paddingy)

        lb_nome = Label(separador3, text="Nome*", font=lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=paddingx)
        entry_nome = Entry(separador3, font=entry_style, width=89)
        entry_nome.grid(column=0, row=1, padx=paddingx)

        lb_apelido = Label(separador3, text="Apelido", font=lb_style)
        lb_apelido.grid(column=0, row=2, sticky="W", padx=paddingx)
        entry_apelido = Entry(separador3, font=entry_style, width=89)
        entry_apelido.grid(column=0, row=3, padx=paddingx)

        separador4 = ttk.Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=paddingx, pady=paddingy)

        lb_endereco = Label(separador4, text="Endereço", font=lb_style)
        lb_endereco.grid(column=0, row=0, sticky="W", padx=paddingx)
        entry_endereco = Entry(separador4, font=entry_style, width=82)
        entry_endereco.grid(column=0, row=1, padx=paddingx)

        lb_numero = Label(separador4, text="Numero", font=lb_style)
        lb_numero.grid(column=1, row=0, sticky="W", padx=paddingx)
        entry_numero = Entry(separador4, font=entry_style, width=5)
        entry_numero.grid(column=1, row=1, padx=paddingx)

        separador5 = ttk.Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=paddingx, pady=paddingy)

        lb_complemento = Label(separador5, text="Complemento", font=lb_style)
        lb_complemento.grid(column=0, row=2, sticky="W", padx=paddingx)
        entry_complemento = Entry(separador5, font=entry_style, width=44)
        entry_complemento.grid(column=0, row=3, padx=paddingx)

        lb_bairro = Label(separador5, text="Bairro", font=lb_style)
        lb_bairro.grid(column=1, row=2, sticky="W", padx=paddingx)
        entry_bairro = Entry(separador5, font=entry_style, width=43)
        entry_bairro.grid(column=1, row=3, padx=paddingx)

        separador6 = ttk.Separator(janela, orient="horizontal")
        separador6.pack(fill="x", padx=paddingx, pady=paddingy)
        '''
        lb_cidade = Label(separador6, text="Cidade", font=lb_style, state=DISABLED)
        lb_cidade.grid(column=0, row=4, sticky="W", padx=paddingx)
        entry_cidade = Entry(separador6, font=entry_style,width=5)
        entry_cidade.grid(column=0, row=5, padx=paddingx)
        '''

        lb_nome_cidade = Label(separador6, text="Cidade", font=lb_style)
        lb_nome_cidade.grid(column=1, row=4, sticky="W", padx=paddingx)
        entry_nome_cidade = Entry(separador6, font=entry_style, width=40)
        entry_nome_cidade.grid(column=1, row=5, padx=paddingx)

        lb_uf = Label(separador6, text="UF", font=lb_style)
        lb_uf.grid(column=2, row=4, sticky="W", padx=paddingx)
        entry_uf = Entry(separador6, font=entry_style, width=3)
        entry_uf.grid(column=2, row=5, padx=paddingx)

        lb_cep = Label(separador6, text="CEP", font=lb_style)
        lb_cep.grid(column=3, row=4, sticky="W", padx=paddingx)
        entry_cep = Entry(separador6, font=entry_style, width=10)
        entry_cep.grid(column=3, row=5, padx=paddingx)

        separador7 = ttk.Separator(janela, orient="horizontal")
        separador7.pack(fill="x", padx=paddingx, pady=paddingy)

        width_fone = 17
        width_operadora = 8
        lb_fone1 = Label(separador7, text="Fone 1", font=lb_style)
        lb_fone1.grid(column=0, row=0, sticky="W", padx=paddingx)
        entry_fone1 = Entry(separador7, font=entry_style, width=width_fone)
        entry_fone1.grid(column=0, row=1, padx=paddingx)

        lb_operadora1 = Label(separador7, text="Operadora", font=lb_style)
        lb_operadora1.grid(column=1, row=0, sticky="W", padx=paddingx)
        entry_operadora1 = Entry(separador7, font=entry_style, width=width_operadora)
        entry_operadora1.grid(column=1, row=1, padx=paddingx)

        lb_fone2 = Label(separador7, text="Fone 2", font=lb_style)
        lb_fone2.grid(column=2, row=0, sticky="W", padx=paddingx)
        entry_fone2 = Entry(separador7, font=entry_style, width=width_fone)
        entry_fone2.grid(column=2, row=1, padx=paddingx)

        lb_operadora2 = Label(separador7, text="Operadora", font=lb_style)
        lb_operadora2.grid(column=3, row=0, sticky="W", padx=paddingx)
        entry_operadora1 = Entry(separador7, font=entry_style, width=width_operadora)
        entry_operadora1.grid(column=3, row=1, padx=paddingx)

        lb_fone3 = Label(separador7, text="Fone 3", font=lb_style)
        lb_fone3.grid(column=4, row=0, sticky="W", padx=paddingx)
        entry_fone3 = Entry(separador7, font=entry_style, width=width_fone)
        entry_fone3.grid(column=4, row=1, padx=paddingx)

        lb_operadora3 = Label(separador7, text="Operadora", font=lb_style)
        lb_operadora3.grid(column=5, row=0, sticky="W", padx=paddingx)
        entry_operadora3 = Entry(separador7, font=entry_style, width=width_operadora)
        entry_operadora3.grid(column=5, row=1, padx=paddingx)

        separador8 = ttk.Separator(janela, orient="horizontal")
        separador8.pack(fill="x", padx=paddingx, pady=paddingy)

        lb_email = Label(separador8, text="Email", font=lb_style)
        lb_email.grid(column=0, row=0, sticky="W", padx=paddingx)
        entry_email = Entry(separador8, font=entry_style, width=89)
        entry_email.grid(column=0, row=1, padx=paddingx)

        lb_campos_obrigatorios = Label(janela, text="(*) Campos Obrigatórios")
        lb_campos_obrigatorios.pack(fill="x", side=RIGHT, anchor=NW)

        separador9 = ttk.Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)

        grava = Button(separador9, text="GRAVA", font=lb_style)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador9, text="CANCELA", font=lb_style)
        cancela.grid(column=1, row=0, sticky="WS")

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
        print("Tela ainda não cadastrada")
        pass
    def altera_cadastro_trabalho(self):
        print("Tela ainda não cadastrada")
        pass
    def altera_financeiro(self):
        print("Tela ainda não cadastrada")
        pass
    def exclui_cadastro_pessoa(self):
        print("Tela ainda não cadastrada")
        pass

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

    def lista_de_pessoas(self,janela):
        pessoa = [1, "vitor", "091.861.449-01", "são jorge do ivai"]

        lista_pessoas = ttk.Treeview(janela, columns=("col1", "col2", "col3"))
        lista_pessoas.heading("#0", text="Cod")
        lista_pessoas.heading("#1", text="Nome")
        lista_pessoas.heading("#2", text="CPF/CNPJ")
        lista_pessoas.heading("#3", text="Cidade")

        lista_pessoas.column("#0", width=50)
        lista_pessoas.column("#1", width=450)
        lista_pessoas.column("#2", width=204)
        lista_pessoas.column("#3", width=300)

        lista_pessoas.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(janela, orient="vertical")
        lista_pessoas.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")
    def lista_de_trabalho(self,janela):
        trabalho = [1, "vitor", "091.861.449-01", "são jorge do ivai"]

        lista_pessoas = ttk.Treeview(janela, columns=("col1", "col2", "col3","col4","col5","col6"))
        lista_pessoas.heading("#0", text="Cod")
        lista_pessoas.heading("#1", text="Data")
        lista_pessoas.heading("#2", text="hora")
        lista_pessoas.heading("#3", text="Nome")
        lista_pessoas.heading("#4", text="Criança")
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


    def informacoes_adicionais_pessoas(self,janela):
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

    #modificar assim que tiver as informações do que colocar
    def informacoes_adicionais_trabalho(self,janela):
        separador1 = ttk.Separator(janela, orient="horizontal")
        separador1.pack(fill="x", side=BOTTOM, padx=self.paddingx, pady=self.paddingy + 10)

        lb_nome_razao = Label(separador1, text="Nome/Razão Social", font=self.lb_style)
        lb_nome_razao.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_nome_razao = Entry(separador1, font=self.entry_style, width=50, state=DISABLED)
        entry_nome_razao.grid(column=1, row=0, padx=self.paddingx)

        lb_pessoa_extra = Label(separador1, text="Pessoa Extra", font=self.lb_style)
        lb_pessoa_extra.grid(column=0, row=1, sticky="NW", padx=self.paddingx)
        entry_pessoa_extra = Entry(separador1, font=self.entry_style, width=50, state=DISABLED)
        entry_pessoa_extra.grid(column=1, row=1, padx=self.paddingx)

        lb_lote = Label(separador1, text="Lote", font=self.lb_style)
        lb_lote.grid(column=2, row=0, sticky="NW", padx=self.paddingx)
        entry_lote = Entry(separador1, font=self.entry_style, width=20, state=DISABLED)
        entry_lote.grid(column=3, row=0, padx=self.paddingx)

        lb_fone2 = Label(separador1, text="Fone 1", font=self.lb_style)
        lb_fone2.grid(column=2, row=1, sticky="NW", padx=self.paddingx)
        entry_fone2 = Entry(separador1, font=self.entry_style, width=20, state=DISABLED)
        entry_fone2.grid(column=3, row=1, padx=self.paddingx)

        lb_fone3 = Label(separador1, text="Fone 2", font=self.lb_style)
        lb_fone3.grid(column=2, row=2, sticky="NW", padx=self.paddingx)
        entry_fone3 = Entry(separador1, font=self.entry_style, width=20, state=DISABLED)
        entry_fone3.grid(column=3, row=2, padx=self.paddingx)

        separador_endereco = ttk.Separator(separador1, orient="horizontal")
        separador_endereco.grid(column=0, row=2, padx=self.paddingx, sticky="ew", columnspan=2)

        lb_endereco = Label(separador_endereco, text="Endereço", font=self.lb_style)
        lb_endereco.pack(side=LEFT)
        # lb_endereco.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_endereco = Entry(separador_endereco, font=self.entry_style, width=41, state=DISABLED)

        # entry_endereco.grid(column=1, row=0, padx=self.paddingx, sticky="ew")

        lb_numero = Label(separador_endereco, text="N.", font=self.lb_style)
        # lb_numero.grid(column=2, row=0, sticky="EW", padx=self.paddingx)

        entry_numero = Entry(separador_endereco, font=self.entry_style, width=6, state=DISABLED)
        entry_numero.pack(side=RIGHT, padx=1)
        lb_numero.pack(side=RIGHT, padx=3)
        entry_endereco.pack(side=RIGHT)
        # entry_numero.grid(column=3, row=0, padx=self.paddingx, sticky="ew")

    def janela_pessoas(self):
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
        self.lista_de_pessoas(listagem_pessoas)
        self.informacoes_adicionais_pessoas(janela_pessoas)

        janela_pessoas.title("Pesquisa de Pessoas")

    def janela_trabalhos(self):
        janela_trabalhos = Toplevel()
        self.configurar_janela_auxiliar(janela_trabalhos)

        data_hoje = date.today().strftime("%d/%m/%Y")

        funcoes = [self.novo_cadastro_tabalho,self.altera_cadastro_trabalho, self.exclui_cadastro_trabalho]

        self.barra_alteracoes(janela_trabalhos,funcoes)

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



'''def barra_menu(janela):
    menus = Menu(janela)

    menuCadastroClientes = Menu(menus)
    menuCadastroClientes.add_command(label="Cadastros",command=sem_comando)

    menuFinalizar = Menu(menus)
    menuFinalizar.add_command(label="Cadastros",command=sem_comando)

    return menus'''

if __name__ == '__main__':

    Aplicacao()
