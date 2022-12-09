
from modulos.auxiliares import Funcs

from modulos.database import pega_ultimo_id, grava_db_planos, pega_todos_planos_sessoes_lista, pega_um_item_plano
from tkinter import Toplevel, DISABLED, Entry, END, Label, Button, BOTTOM
from tkinter.ttk import Separator, Scrollbar,Treeview

class Planos(Funcs):
    def __init__(self, janela_trabalhos = None):
        super().__init__()
        class_funcs = Funcs()
        self.janela_planos_var = None
        self.janela_trabalhos_var = janela_trabalhos
        self.nome = None
        self.entry_codigo = None
        self.lb_erro = None
        self.entry_quantidade_fotos = None

    def validador_entry_apenas_numeros(self, P):
        if str.isdigit(P) or P == "":
            print("verdadeiro")
            return True
        else:
            print("Falso")
            return False

    def novo_cadastro_plano(self):
        janela = Toplevel()
        self.configurar_janela_auxiliar3(janela)
        janela.title("Cadastro Planos")

        codigo = pega_ultimo_id("planos")

        separador1 = Separator(janela, orient="horizontal")
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

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        def set_sem_texto_lb_erro(event):
            self.lb_erro["text"] = ""

        lb_nome_plano = Label(separador2, text="Nome*", font=self.lb_style)
        lb_nome_plano.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome_plano = Entry(separador2, font=self.entry_style,width=89)
        entry_nome_plano.grid(column=0, row=1, padx=self.paddingx)
        entry_nome_plano.bind("<FocusOut>", set_sem_texto_lb_erro)

        separador3 = Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_descricao = Label(separador3, text="Descrição", font=self.lb_style)
        lb_descricao.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_descricao = Entry(separador3, font=self.entry_style,width=89)
        entry_descricao.grid(column=0, row=1, padx=self.paddingx)

        separador4 = Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_valor_base = Label(separador4, text="Valor do Plano", font=self.lb_style)
        lb_valor_base.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_valor_base = Entry(separador4, font=self.entry_style)
        entry_valor_base.grid(column=0, row=1, padx=self.paddingx)

        separador5 = Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        vcmd = self.janela_planos_var.register((self.validador_entry_apenas_numeros))
        lb_quantidade_fotos = Label(separador5, text="Quantidade de fotos", font=self.lb_style)
        lb_quantidade_fotos.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        self.entry_quantidade_fotos = Entry(separador5,font=self.entry_style, validate="all", validatecommand=(vcmd, "%P"))
        self.entry_quantidade_fotos.grid(column=1, row=1, padx=self.paddingx)

        lb_valor_foto_extra = Label(separador5, text="Valor Fotos extra", font=self.lb_style)
        lb_valor_foto_extra.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_valor_foto_extra = Entry(separador5, font=self.entry_style)
        entry_valor_foto_extra.grid(column=2, row=1, padx=self.paddingx)

        lb_espaco = Label(separador5, text="", font=self.lb_style)
        lb_espaco.grid(column=1, row=3, sticky="W", padx=self.paddingx)

        lb_erro = Label(separador5, text="", font=self.lb_style)
        lb_erro.grid(column=1, row=4,columnspan=2, sticky="W", padx=self.paddingx)
        self.lb_erro = lb_erro

        separador5 = Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy,side=BOTTOM)
        def grava_db_pessoa_args():
            valor_entry_nome = entry_nome_plano.get()

            if len(valor_entry_nome) < 1:
                self.lb_erro["text"] = "Por favor insira o nome do plano"
            elif entry_valor_base.get() == '':
                self.lb_erro["text"] = "Por favor insira o valor do plano"
            else:
                try:
                    quantidade_fotos = int(self.entry_quantidade_fotos.get())
                except ValueError:
                    quantidade_fotos = '0'
                try:
                    valor_fotos_extra = float(self.replace_virgula_ponto(entry_valor_foto_extra.get()))
                    print(valor_fotos_extra)
                except ValueError:
                    valor_fotos_extra = "0.0"

                valor_base = self.replace_virgula_ponto(entry_valor_base.get())

                grava_db_planos(entry_codigo.get,entry_cadastro.get,entry_nome_plano.get,entry_descricao.get,valor_base,quantidade_fotos,valor_fotos_extra)
                janela.destroy()
                self.janela_planos_var.destroy()
                self.janela_planos()

        grava = Button(separador5, text="GRAVA", font=self.lb_style, command=grava_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador5, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")
    def altera_cadastro_plano(self):
        pass
    def exclui_cadastro_plano(self):
        pass
    def janela_planos(self, tipo=None):

        janela = Toplevel()
        self.configurar_janela_auxiliar2(janela)
        janela.title("Planos")

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", pady=self.paddingy)

        funcoes = [self.novo_cadastro_plano, self.altera_cadastro_plano, self.exclui_cadastro_plano]

        barra_alteracoes = self.barra_alteracoes(separador1, funcoes)

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x")

        lista_planos = Treeview(separador2, columns=("col1", "col2"), padding=(0,0,0,25))
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
        self.janela_planos_var = janela

        if tipo == "escolha":
            def funcao(event):
                plano = None
                for selected_item in self.lista_planos.selection():
                    item = self.lista_planos.item(selected_item, 'values')
                    plano = pega_um_item_plano(item[0])
                    self.janela_trabalhos_var.set_codigo_plano_trabalho(plano[0][0],plano[0][1])
                    self.janela_planos_var.destroy()
                    return

            self.lista_planos.bind("<Double-1>", funcao)