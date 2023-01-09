from functools import partial

from modulos.auxiliares import Funcs
from modulos.database import pega_ultimo_id, grava_db_tipos, pega_um_item_tipo, pega_todos_tipos_sessoes_lista
from tkinter import Toplevel, DISABLED, Entry, END, Label, Button, BOTTOM
from tkinter.ttk import Separator, Treeview, Scrollbar



class Tipos(Funcs):
    def __init__(self,janela_trabalhos = None):
        super().__init__()
        self.janela_tipos_var = None
        self.lista_tipos = None
        self.janela_trabalhos_var = janela_trabalhos

    def novo_cadastro_tipo(self):
        janela = Toplevel()
        self.configurar_janela_auxiliar3(janela)
        janela.title("Cadastro Tipos")

        codigo = pega_ultimo_id("tipos")

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

        lb_nome = Label(separador2, text="Nome*", font=self.lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=89)
        entry_nome.grid(column=0, row=1, padx=self.paddingx)

        separador3 = Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_descricao = Label(separador3, text="Descrição", font=self.lb_style)
        lb_descricao.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_descricao = Entry(separador3, font=self.entry_style, width=89)
        entry_descricao.grid(column=0, row=1, padx=self.paddingx)

        separador5 = Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy, side=BOTTOM)

        grava_db_pessoa_args = partial(grava_db_tipos, entry_codigo.get, entry_cadastro.get, entry_nome.get,
                                       entry_descricao.get)
        grava = Button(separador5, text="GRAVA", font=self.lb_style, command=grava_db_pessoa_args)
        grava.grid(column=0, row=0, sticky="WS")

        cancela = Button(separador5, text="CANCELA", font=self.lb_style)
        cancela.grid(column=1, row=0, sticky="WS")

    def altera_cadastro_tipo(self):
        pass
    def exclui_cadastro_tipo(self):
        pass
    def janela_tipos(self, tipo = None):
        janela = Toplevel()
        self.configurar_janela_auxiliar2(janela)
        janela.title("Tipos")

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", pady=self.paddingy)

        funcoes = [self.novo_cadastro_tipo, self.altera_cadastro_tipo,self.exclui_cadastro_tipo]

        barra_alteracoes = self.barra_alteracoes(separador1, funcoes)

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x")

        lista_tipos = Treeview(separador2, columns=("col1", "col2", "col3"), padding=(0, 0, 0, 25))
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
            lista_tipos.insert("", END, values=i)

        lista_tipos.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(separador2, orient="vertical")
        lista_tipos.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")

        self.lista_tipos = lista_tipos
        self.janela_tipos_var = janela

        if tipo == "escolha":
            def funcao(event):
                tipo = None
                for selected_item in self.lista_tipos.selection():
                    item = self.lista_tipos.item(selected_item, 'values')
                    tipo = pega_um_item_tipo(item[0])
                    print(tipo)
                    self.janela_trabalhos_var.set_argumentos_tipo_trabalho(tipo[0][0], tipo[0][1])
                    self.janela_tipos_var.destroy()
                    return

            self.lista_tipos.bind("<Double-1>", funcao)