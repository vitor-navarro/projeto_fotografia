from modulos.auxiliares import Funcs

from tkinter import Toplevel, LEFT, Button, Label, Entry, DISABLED, END, Text, StringVar, Radiobutton, BOTTOM
from tkinter.ttk import Separator, Combobox, Treeview, Scrollbar

class Financeiro(Funcs):

    def lista_de_trabalho_financeiro(self,janela):
        trabalho = [1, "vitor", "091.861.449-01", "são jorge do ivai"]
        #codigo, lote + sessao, pessoa,condicao, valor, pago

        lista_pessoas = Treeview(janela, columns=("col1", "col2", "col3", "col4", "col5"))
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

    #modificar assim que tiver as informações do que colocar
    def novo_financeiro(self):
        janela = Toplevel()

        janela.title("Cadastro Financeiro")

        self.configurar_janela_auxiliar2(janela)

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_data = Label(separador1, text="Data", font=self.lb_style)
        lb_data.grid(column=2, row=1, sticky="W", padx=self.paddingx)
        entry_data = Entry(separador1, font=self.entry_style, width=10)
        entry_data.grid(column=2, row=2, padx=self.paddingx)

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_codigo_sessao = Label(separador2, text="Sessão", font=self.lb_style)
        lb_codigo_sessao.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo_sessao = Entry(separador2, font=self.entry_style, width=8)
        entry_codigo_sessao.grid(column=0, row=1, padx=self.paddingx, sticky="NW")

        lb_nome = Label(separador2, text="Nome", font=self.lb_style)
        lb_nome.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=30, state=DISABLED)
        entry_nome.grid(column=1, row=1, padx=self.paddingx)

        separador3 = Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_valor = Label(separador3, text="Valor", font=self.lb_style)
        lb_valor.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_valor = Entry(separador3, font=self.entry_style, width=10)
        entry_valor.grid(column=0, row=1, padx=self.paddingx)

        pagamentos_possiveis = ["Dinheiro", "Pix", "Cartão"]

        # mudar para opções
        lb_tipo = Label(separador3, text="Status", font=self.lb_style)
        lb_tipo.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        cb_tipo = Combobox(separador3, font=self.entry_style, width=15, values=pagamentos_possiveis, state="readonly")
        cb_tipo.set("Dinheiro")
        cb_tipo.grid(column=1, row=1, padx=self.paddingx)

        lb_parcelas= Label(separador3, text="Nº Parcelas", font=self.lb_style)
        lb_parcelas.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_parcelas = Entry(separador3, font=self.entry_style, width=10)
        entry_parcelas.grid(column=2, row=1, padx=self.paddingx)

        separador4 = Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy,side=BOTTOM)

        grava = Button(separador4, text="GRAVA", font=self.lb_style)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador4, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")

    def altera_cadastro_trabalho(self):
        print("Tela ainda não cadastrada")
        pass
    def altera_financeiro(self):
        print("Tela ainda não cadastrada")
        pass
    def exclui_cadastro_trabalho(self):
        print("Tela ainda não cadastrada")
        pass
    def exclui_financeiro(self):
        print("Tela ainda não cadastrada")
        pass

    def janela_financeiro(self):
        janela_financeiro = Toplevel()
        self.configurar_janela_auxiliar(janela_financeiro)
        funcoes = [self.novo_financeiro,self.altera_financeiro, self.exclui_financeiro]

        self.barra_alteracoes(janela_financeiro,funcoes)

        listagem_trabalhos_financeiro = Separator(janela_financeiro, orient="horizontal")
        listagem_trabalhos_financeiro.pack(fill="x")

        self.lista_de_trabalho_financeiro(listagem_trabalhos_financeiro)

        janela_financeiro.title("Controle Financeiro")