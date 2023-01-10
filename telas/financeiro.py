from modulos.auxiliares import Funcs

from tkinter import Toplevel, LEFT, Button, Label, Entry, DISABLED, END, Text, StringVar, Radiobutton, BOTTOM, Frame, CENTER
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

        separador_titulo = Separator(janela_financeiro)
        separador_titulo.pack(fill="x", padx=10, pady=10)

        label_financeiro = Label(separador_titulo, text="FINANCEIRO", font=("Helvetica", 16))
        label_financeiro.pack(side=LEFT)

        separador1 = Separator(janela_financeiro)
        separador1.pack(fill="x")

        frame_data_inicial = Frame(separador1)

        label_data_inicial = Label(frame_data_inicial, text="Data Inicial")
        entry_data_inicial = Entry(frame_data_inicial)

        frame_data_inicial.grid(column=0, row=0)
        label_data_inicial.pack(anchor="w")
        entry_data_inicial.pack()

        frame_data_final = Frame(separador1)

        label_data_final = Label(frame_data_final, text="Data Final")
        entry_data_final = Entry(frame_data_final)

        frame_data_final.grid(column=1, row=0)
        label_data_final.pack(anchor="w")
        entry_data_final.pack()

        separador2 = Separator(janela_financeiro, orient="horizontal")
        separador2.pack(fill="x")

        frame_auxiliar2 = Frame(separador2)
        frame_auxiliar2.pack()

        frame1 = Frame(frame_auxiliar2, borderwidth=2, relief="groove", padx=50, pady=10)
        frame2 = Frame(frame_auxiliar2, borderwidth=2, relief="groove", padx=50, pady=10)
        frame3 = Frame(frame_auxiliar2, borderwidth=2, relief="groove", padx=50, pady=10)
        frame4 = Frame(frame_auxiliar2, borderwidth=2, relief="groove", padx=50, pady=10)

        saldo_atual =Label(frame1, text="Saldo atual", font=("Helvetica", 16))
        valor_saldo_atual = Label(frame1, text="0.00", font=("Helvetica", 20))
        a_pagar =Label(frame2, text="A pagar", font=("Helvetica", 16))
        valor_a_pagar = Label(frame2, text="0.00", font=("Helvetica", 20))
        a_receber =Label(frame3, text="A receber", font=("Helvetica", 16))
        valor_a_receber =Label(frame3, text="0.00", font=("Helvetica", 20))
        saldo_projetado =Label(frame4, text="Saldo projetado", font=("Helvetica", 16))
        valor_saldo_projetado =Label(frame4, text="0.00", font=("Helvetica", 20))

        saldo_atual.pack()
        valor_saldo_atual.pack()
        a_pagar.pack()
        valor_a_pagar.pack()
        a_receber.pack()
        valor_a_receber.pack()
        saldo_projetado.pack()
        valor_saldo_projetado.pack()

        frame1.grid(row=0,column=0,padx=10, pady=10)
        frame2.grid(row=0,column=1,padx=10, pady=10)
        frame3.grid(row=0,column=2,padx=10, pady=10)
        frame4.grid(row=0,column=3,padx=10, pady=10)

        separador3 = Separator(janela_financeiro, orient="horizontal")
        separador3.pack(fill="x")

        self.lista_de_trabalho_financeiro(separador3)

        janela_financeiro.title("Controle Financeiro")