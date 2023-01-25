from modulos.auxiliares import Funcs
from modulos.database import pega_ultimo_id, grava_db_tipos, pega_um_item_tipo, pega_todos_tipos_sessoes_lista, \
    altera_db_tipos, deleta_db_tipo,filtro_database_tipos

from tkinter import Toplevel, DISABLED, Entry, END, Label, Button, BOTTOM, StringVar, messagebox
from tkinter.ttk import Separator, Treeview, Scrollbar



class Tipos(Funcs):
    def __init__(self,janela_trabalhos = None):
        super().__init__()
        self.janela_tipos_var = None
        self.lista_de_tipos = None
        self.janela_trabalhos_var = janela_trabalhos

    def callback_pesquisa(self, event = None):
        self.janela_tipos_var.after(200, self._executa_filtro)

    def _executa_filtro(self):
        search_data = self.search_var.get()
        retorno = filtro_database_tipos(search_data=search_data)
        self.update_treeview(retorno)
    def update_treeview(self, retorno):
        print(retorno)
        for child in self.lista_de_tipos.get_children():
            self.lista_de_tipos.delete(child)
        for item in retorno:
            self.lista_de_tipos.insert("", "end", values=item)
    def seleciona_item_tipo(self):
        for selected_item in self.lista_de_tipos.selection():
            item = self.lista_de_tipos.item(selected_item)
            record = item['values']
            tipo = pega_um_item_tipo(record[0])
            return tipo

    def novo_cadastro_tipo(self):
        janela = Toplevel()
        self.configurar_janela_auxiliar3(janela)
        janela.title("Cadastro Tipos")
        janela.bind("<Return>", self.next_focus)
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
        def grava_db_tipo_args():
            if self.confirmacao_salvamento(janela):
                grava_db_tipos(entry_codigo.get, entry_cadastro.get, entry_nome.get,entry_descricao.get)
                self.janela_tipos_var.destroy()
                janela.destroy()
                self.janela_tipos()

        grava = Button(separador5, text="GRAVA", font=self.lb_style, command=grava_db_tipo_args)
        grava.grid(column=0, row=0, sticky="WS")

        def cancelar():
            if self.confirmacao_cancelamento(janela):
                self.janela_tipos_var.destroy()
                janela.destroy()
                self.janela_tipos()

        cancela = Button(separador5, text="CANCELA", font=self.lb_style, command=cancelar)
        cancela.grid(column=1, row=0, sticky="WS")

    def altera_cadastro_tipo(self):
        tipo = self.seleciona_item_tipo()[0]

        if tipo is None:
            return

        janela = Toplevel()
        janela.bind("<Return>", self.next_focus)
        self.configurar_janela_auxiliar3(janela)
        janela.title("Cadastro Tipos")

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")
        self.insert_entry_desabilitado(entry_codigo, tipo[0])

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
        entry_cadastro.insert(END, self.data_sistema)
        entry_cadastro.grid(column=1, row=1, padx=self.paddingx)
        self.set_text_entry(entry_cadastro, tipo[3])

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador2, text="Nome*", font=self.lb_style)
        lb_nome.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=89)
        entry_nome.grid(column=0, row=1, padx=self.paddingx)
        self.set_text_entry(entry_nome, tipo[1])

        separador3 = Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_descricao = Label(separador3, text="Descrição", font=self.lb_style)
        lb_descricao.grid(column=0, row=0, sticky="W", padx=self.paddingx)
        entry_descricao = Entry(separador3, font=self.entry_style, width=89)
        entry_descricao.grid(column=0, row=1, padx=self.paddingx)
        self.set_text_entry(entry_descricao, tipo[2])

        separador5 = Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy, side=BOTTOM)
        def altera_db_tipo_args(event = None):

            if self.confirmacao_salvamento(janela):
                altera_db_tipos(entry_codigo.get, entry_cadastro.get, entry_nome.get,entry_descricao.get)

                janela.destroy()
                self.janela_tipos_var.destroy()
                self.janela_tipos()

        grava = Button(separador5, text="GRAVA", font=self.lb_style, command=altera_db_tipo_args)
        grava.grid(column=0, row=0, sticky="WS")
        grava.bind("<Return>", altera_db_tipo_args)
        def cancelar():
            if self.confirmacao_cancelamento(janela):
                self.janela_tipos_var.destroy()
                janela.destroy()
                self.janela_tipos()

        cancela = Button(separador5, text="CANCELA", font=self.lb_style, command=cancelar)
        cancela.grid(column=1, row=0, sticky="WS")
    def exclui_cadastro_tipo(self):
        tipo = self.seleciona_item_tipo()
        id = tipo[0][0]

        if self.confirmacao_exclusao(frase="O tipo", valor=tipo[0][1], janela_principal=self.janela_tipos_var):
            deleta_db_tipo(id)
            self.janela_tipos_var.destroy()
            self.janela_tipos()
    def janela_tipos(self, tipo = None):
        janela = Toplevel()
        self.configurar_janela_auxiliar2(janela)
        janela.title("Tipos")

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", pady=self.paddingy)

        funcoes = [self.novo_cadastro_tipo, self.altera_cadastro_tipo,self.exclui_cadastro_tipo]

        barra_alteracoes = self.barra_alteracoes_grid(separador1, funcoes)
        self.barra_de_pesquisa(barra_filtros=barra_alteracoes,callback_pesquisa=self.callback_pesquisa, tamanho_pequeno=True)

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x")

        self.lista_de_tipos = Treeview(separador2, columns=("col1", "col2", "col3"), padding=(0, 0, 0, 25))
        self.lista_de_tipos.heading("#0", text="")
        self.lista_de_tipos.heading("#1", text="Cod")
        self.lista_de_tipos.heading("#2", text="Nome")
        self.lista_de_tipos.heading("#3", text="Descrição")

        self.lista_de_tipos.column("#0", width=0)
        self.lista_de_tipos.column("#1", width=50)
        self.lista_de_tipos.column("#2", width=100)
        self.lista_de_tipos.column("#3", width=342)

        lista = pega_todos_tipos_sessoes_lista()

        for i in lista:
            self.lista_de_tipos.insert("", END, values=i)

        self.lista_de_tipos.grid(column=0, row=0, sticky="WSNE")

        barra_rolagem = Scrollbar(separador2, orient="vertical")
        self.lista_de_tipos.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")

        self.janela_tipos_var = janela

        if tipo == "escolha":
            def funcao(event):
                tipo = None
                for selected_item in self.lista_de_tipos.selection():
                    item = self.lista_de_tipos.item(selected_item, 'values')
                    tipo = pega_um_item_tipo(item[0])
                    self.janela_trabalhos_var.set_argumentos_tipo_trabalho(tipo[0][0], tipo[0][1])
                    self.janela_tipos_var.destroy()
                    return

            self.lista_de_tipos.bind("<Double-1>", funcao)