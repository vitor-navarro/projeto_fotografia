from modulos.auxiliares import Funcs
from modulos.database import pega_ultimo_id, grava_db_trabalhos, pega_todas_trabalhos_lista, pega_um_item_trabalho, \
    altera_db_trabalhos

from tkinter import Toplevel, LEFT, Button, Label, Entry, DISABLED, END, Text, StringVar, Radiobutton, BOTTOM
from tkinter.ttk import Separator, Combobox, Treeview, Scrollbar

from telinhas.pessoas import Pessoas
from telinhas.tipos import Tipos
from telinhas.planos import Planos
from modulos.validadores import Validadores

class Trabalhos(Funcs):

    def __init__(self):
        super().__init__()
        self.class_validadores = Validadores()
        self.class_tipos = Tipos(self)
        self.class_pessoas = Pessoas(self)
        self.class_planos = Planos(self)
        self.janela_trabalhos_var = None
        self.lista_de_trabalhos = None
        self.nome_pessoa_trabalho = None
        self.entry_nome = None
        self.codigo_pessoa_trabalho = None
        self.codigo_tipo_trabalho = None
        self.entry_tipo = None
        self.nome_tipo_trabalho = None
        self.codigo_plano_trabalho = None
        self.nome_plano_trabalho = None
        self.valores_pagamento = []
        self.event_ultimo_caractere_digitrado = None
        self.argumentos = None
    def retorna_variaveis_none_trabalhos(self):
        self.argumentos = None
        self.codigo_pessoa_trabalho = None
        self.nome_pessoa_trabalho = None
        self.codigo_tipo_trabalho = None
        self.nome_tipo_trabalho = None
        self.codigo_plano_trabalho = None
        self.nome_plano_trabalho = None
        self.valores_pagamento = []

    def set_ultimo_caractere_digitado(self, event):
        self.event_ultimo_caractere_digitrado = event

    def set_entry_horario_posicao(self, posicao):
        self.entry_horario_sessao.icursor(posicao)
    def set_entry_horario_text(self, texto_entry):
        self.entry_horario_sessao.delete(0,END)
        self.entry_horario_sessao.insert(0,texto_entry)
    def set_codigo_nome_trabalho(self,codigo,nome):
        self.insert_entry_desabilitado(entry=self.entry_nome, valor=nome)
        self.nome_pessoa_trabalho = nome
        self.codigo_pessoa_trabalho = codigo

    def set_codigo_tipo_trabalho(self,codigo,tipo):
        self.insert_entry_desabilitado(entry=self.entry_tipo, valor=tipo)
        self.codigo_tipo_trabalho = codigo
        self.nome_tipo_trabalho = tipo
    def set_codigo_plano_trabalho(self,codigo,plano):
        self.insert_entry_desabilitado(entry=self.entry_plano, valor=plano)
        self.codigo_plano_trabalho = codigo
        self.nome_plano_trabalho = plano
    def buscar_pessoa_trabalho(self,janela_trabalhos):
        self.class_pessoas.janela_pessoas(btn_grava_escolhe = "escolhe")

    def seleciona_item_trabalhos(self):
        for selected_item in self.lista_de_trabalhos.selection():
            item = self.lista_de_trabalhos.item(selected_item)
            record = item['values']
            trabalho = pega_um_item_trabalho(record[0])
            return trabalho
    def barra_filtros_opcoes_trabalho(self,barra_filtros):
        # opções 1
        barra_filtro_opcoes = Separator(barra_filtros, orient="vertical")
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

    def barra_filtros_status_trabalho(self, barra_filtros):
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
    def novo_cadastro_trabalho(self):
        janela = Toplevel()
        janela.focus_force()

        janela.title("Cadastro Trabalho")

        self.configurar_janela_auxiliar(janela)

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        self.lb_aviso_erro = Label(separador1, text="", font=self.lb_style)
        self.lb_aviso_erro.grid(column=4, row=1, sticky="W", padx=self.paddingx)

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

        def validador_horario_args():
            retorno = self.class_validadores.validador_horario(self.entry_horario_sessao, self.event_ultimo_caractere_digitrado, self.set_entry_horario_posicao, self.set_entry_horario_text)
            return retorno

        lb_horario_sessao = Label(separador1, text="Horário da Sessão", font=self.lb_style)
        lb_horario_sessao.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        self.entry_horario_sessao = Entry(separador1, font=self.entry_style, width=10)
        self.entry_horario_sessao.config(validate="key", validatecommand=validador_horario_args)
        self.entry_horario_sessao.grid(column=3, row=1, padx=self.paddingx)
        self.entry_horario_sessao.bind("<Any-KeyPress>", self.set_ultimo_caractere_digitado)
        self.entry_horario_sessao.bind("<FocusOut>", lambda event, parametro = self.entry_horario_sessao.get, lb_erro=self.lb_aviso_erro: self.class_validadores.valida_formato_hora(event, parametro, lb_erro))

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador2, text="Nome", font=self.lb_style)
        lb_nome.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=89, state=DISABLED)
        entry_nome.grid(column=1, row=1, padx=self.paddingx)
        self.entry_nome = entry_nome

        separador3 = Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        # mudar para opções
        lb_tipo_sessao = Label(separador3, text="tipo da Sessão", font=self.lb_style)
        lb_tipo_sessao.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        cb_tipo_sessao = Entry(separador3, font=self.entry_style, width=20, state=DISABLED)
        #cb_tipo_sessao = ttk.Combobox(separador1, font=self.entry_style, width=15, values=tipos_possiveis, state="readonly")
        #cb_tipo_sessao.set("Ativo")
        cb_tipo_sessao.grid(column=1, row=1, padx=self.paddingx,sticky="W")
        self.entry_tipo = cb_tipo_sessao

        lb_plano = Label(separador3, text="Plano", font=self.lb_style)
        lb_plano.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        cb_plano = Entry(separador3, font=self.entry_style, width=20, state=DISABLED)
        #cb_plano = ttk.Combobox(separador1, font=self.entry_style, width=15, values=planos_possiveis, state="readonly")
        #cb_plano.set("Ativo")
        cb_plano.grid(column=3, row=1, padx=self.paddingx,sticky="W")
        self.entry_plano = cb_plano

        separador4 = Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        opcoes_pagamento = ['DINHEIRO','PIX', 'CARTÃO DÉBITO', 'CARTÃO CRÉDITO', 'OUTRO']

        lb_condicao_pagamento1 = Label(separador4, text="Condicao Pagamento", font=self.lb_style)
        lb_condicao_pagamento1.grid(column=0, row=0, sticky="W", padx=self.paddingx, columnspan=2)

        lb_valor = Label(separador4, text="Valor", font=self.lb_style)
        lb_valor.grid(column=3, row=0, sticky="W", padx=self.paddingx, columnspan=2)

        lb_total = Label(separador4, text="Total", font=self.lb_style)
        lb_total.grid(column=5, row=0, sticky="W", padx=self.paddingx)

        entry_total = Entry(separador4, font=self.entry_style, width=10,state=DISABLED)

        lb_condicao_pagamento_numero1 = Label(separador4, text="1º", font=self.lb_style)
        lb_condicao_pagamento_numero1.grid(column=0, row=1, padx=self.paddingx,pady=self.paddingy)
        cb_condicao_pagamento1 = Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento, state="readonly")
        cb_condicao_pagamento1.set("DINHEIRO")
        cb_condicao_pagamento1.grid(column=1, row=1, padx=self.paddingx,pady=self.paddingy)
        entry_valor1 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor1.grid(column=3, row=1, padx=self.paddingx,pady=self.paddingy)

        lb_condicao_pagamento_numero2 = Label(separador4, text="2º", font=self.lb_style)
        lb_condicao_pagamento_numero2.grid(column=0, row=2, padx=self.paddingx,pady=self.paddingy)
        cb_condicao_pagamento2 = Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento, state="readonly")
        cb_condicao_pagamento2.set("DINHEIRO")
        cb_condicao_pagamento2.grid(column=1, row=2, padx=self.paddingx,pady=self.paddingy)
        entry_valor2 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor2.grid(column=3, row=2, padx=self.paddingx,pady=self.paddingy)

        lb_condicao_pagamento_numero3 = Label(separador4, text="3º", font=self.lb_style)
        lb_condicao_pagamento_numero3.grid(column=0, row=3, padx=self.paddingx,pady=self.paddingy)
        cb_condicao_pagamento3 = Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento, state="readonly")
        cb_condicao_pagamento3.set("DINHEIRO")
        cb_condicao_pagamento3.grid(column=1, row=3, padx=self.paddingx,pady= self.paddingy)
        entry_valor3 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor3.grid(column=3, row=3, padx=self.paddingx,pady=self.paddingy)

        def soma_condicao_pagamento(event):
            try:
                valor1 = entry_valor1.get().replace(",",".")
                valor2 = entry_valor2.get().replace(",",".")
                valor3 = entry_valor3.get().replace(",",".")
                self.lb_aviso_erro['text'] = "."
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
                self.lb_aviso_erro['text'] = "VERIFIQUE OS VALORES DO PAGAMENTO"

        entry_valor1.bind("<FocusOut>",soma_condicao_pagamento)
        entry_valor2.bind("<FocusOut>",soma_condicao_pagamento)
        entry_valor3.bind("<FocusOut>",soma_condicao_pagamento)

        entry_total.grid(column=5, row=3, padx=self.paddingx,pady=self.paddingy)

        separador5 = Separator(janela, orient="horizontal")
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
            argumentos.append(self.entry_horario_sessao.get())
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
            self.class_tipos.janela_tipos(tipo = "escolha")

        bt_busca_sessao = Button(separador3, text="busca", font=self.btn_style, command=buscar_tipos_sessao_trabalho_args)
        bt_busca_sessao.grid(column=0, row=1)

        def buscar_plano_sessao_trabalho_args():
            coleta_argumentos()
            self.class_planos.janela_planos(tipo = "escolha")

        bt_busca_plano = Button(separador3, text="busca", font=self.btn_style, command=buscar_plano_sessao_trabalho_args)
        bt_busca_plano.grid(column=2, row=1)

        separador9 = Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)

        if self.argumentos is not None:
            self.insert_entry_desabilitado(entry_codigo,self.argumentos[0])
            self.set_text_entry(entry_cadastro,self.argumentos[1])
            self.set_text_entry(entry_data_sessao,self.argumentos[2])
            self.set_text_entry(self.entry_horario_sessao,self.argumentos[3])
            self.set_text_entry(entry_nome,self.nome_pessoa_trabalho)
            self.insert_entry_desabilitado(cb_tipo_sessao,self.nome_tipo_trabalho)
            self.insert_entry_desabilitado(cb_plano,self.nome_plano_trabalho)
            self.set_text_entry(entry_valor1,self.argumentos[8])
            self.set_text_entry(entry_valor2,self.argumentos[9])
            self.set_text_entry(entry_valor3,self.argumentos[10])
            self.insert_entry_desabilitado(entry_total,self.argumentos[11])
            self.set_textarea(textarea_observacoes,self.argumentos[12])
        def grava_db_trabalho_args():
            if self.nome_pessoa_trabalho is None:
                self.lb_aviso_erro['text'] = "Nome é obrigatório"
            elif self.nome_tipo_trabalho is None:
                self.lb_aviso_erro['text'] = "Tipo da Sessão é obrigatório"
            elif self.nome_plano_trabalho is None:
                self.lb_aviso_erro['text'] = "Plano é obrigatório"
            elif len(self.valores_pagamento) == 0:
                self.lb_aviso_erro['text'] = "Insira ao menos uma forma de pagamento"
            else:
                grava_db_trabalhos(entry_codigo.get,entry_cadastro.get,entry_data_sessao.get,self.entry_horario_sessao.get,self.codigo_pessoa_trabalho,entry_nome.get,cb_tipo_sessao.get,self.codigo_tipo_trabalho,cb_plano.get,self.codigo_plano_trabalho,cb_condicao_pagamento1.get,self.valores_pagamento[0],cb_condicao_pagamento2.get,self.valores_pagamento[1],cb_condicao_pagamento3.get,self.valores_pagamento[2],entry_total.get,textarea_observacoes.get)
                self.retorna_variaveis_none_trabalhos()
                janela.destroy()
                self.janela_trabalhos_var.destroy()
                self.janela_trabalhos()

        grava = Button(separador9, text="GRAVA", font=self.lb_style, command=grava_db_trabalho_args)
        grava.grid(column=0, row=0, sticky="WS")

        def cancelar():
            self.retorna_variaveis_none_trabalhos()
            janela.destroy()


        cancela = Button(separador9, text="CANCELA", font=self.lb_style, command=cancelar)
        cancela.grid(column=1, row=0, sticky="WS")

    def altera_cadastro_trabalho(self):

        trabalho = self.seleciona_item_trabalhos()[0]

        self.codigo_pessoa_trabalho = trabalho[1]
        self.nome_pessoa_trabalho = trabalho[2]
        self.codigo_tipo_trabalho = trabalho[3]
        self.nome_tipo_trabalho = trabalho[4]
        self.codigo_plano_trabalho = trabalho[5]
        self.nome_plano_trabalho = trabalho[6]
        self.valores_pagamento.append(trabalho[12])
        self.valores_pagamento.append(trabalho[14])
        self.valores_pagamento.append(trabalho[16])

        if trabalho is None:
            return

        janela = Toplevel()
        janela.focus_force()

        janela.title("Cadastro Trabalho")

        self.configurar_janela_auxiliar(janela)

        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        self.lb_aviso_erro = Label(separador1, text="", font=self.lb_style)
        self.lb_aviso_erro.grid(column=4, row=1, sticky="W", padx=self.paddingx)

        lb_codigo = Label(separador1, text="Código", font=self.lb_style)
        lb_codigo.grid(column=0, row=0, sticky="NW", padx=self.paddingx)
        entry_codigo = Entry(separador1, font=self.entry_style, width=8, state=DISABLED)
        entry_codigo.grid(column=0, row=1, padx=self.paddingx, sticky="NW")
        self.insert_entry_desabilitado(entry_codigo, trabalho[0])

        lb_cadastro = Label(separador1, text="Cadastro", font=self.lb_style)
        lb_cadastro.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_cadastro = Entry(separador1, font=self.entry_style, width=10)
        entry_cadastro.grid(column=1, row=1, padx=self.paddingx)
        entry_cadastro.insert(END,trabalho[19])

        lb_data_sessao = Label(separador1, text="Data da Sessão", font=self.lb_style)
        lb_data_sessao.grid(column=2, row=0, sticky="W", padx=self.paddingx)
        entry_data_sessao = Entry(separador1, font=self.entry_style, width=10)
        entry_data_sessao.grid(column=2, row=1, padx=self.paddingx)
        entry_data_sessao.insert(END,trabalho[7])
        def validador_horario_args():
            retorno = self.class_validadores.validador_horario(self.entry_horario_sessao,
                                                               self.event_ultimo_caractere_digitrado,
                                                               self.set_entry_horario_posicao,
                                                               self.set_entry_horario_text)
            return retorno

        lb_horario_sessao = Label(separador1, text="Horário da Sessão", font=self.lb_style)
        lb_horario_sessao.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        self.entry_horario_sessao = Entry(separador1, font=self.entry_style, width=10)
        self.entry_horario_sessao.insert(END,trabalho[8])
        self.entry_horario_sessao.config(validate="key", validatecommand=validador_horario_args)
        self.entry_horario_sessao.grid(column=3, row=1, padx=self.paddingx)
        self.entry_horario_sessao.bind("<Any-KeyPress>", self.set_ultimo_caractere_digitado)
        self.entry_horario_sessao.bind("<FocusOut>", lambda event, parametro=self.entry_horario_sessao.get,
                                                            lb_erro=self.lb_aviso_erro: self.class_validadores.valida_formato_hora(
            event, parametro, lb_erro))


        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador2, text="Nome", font=self.lb_style)
        lb_nome.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=89, state=DISABLED)
        entry_nome.grid(column=1, row=1, padx=self.paddingx)
        self.insert_entry_desabilitado(entry_nome, trabalho[2])
        self.entry_nome = entry_nome

        separador3 = Separator(janela, orient="horizontal")
        separador3.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        # mudar para opções
        lb_tipo_sessao = Label(separador3, text="tipo da Sessão", font=self.lb_style)
        lb_tipo_sessao.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        cb_tipo_sessao = Entry(separador3, font=self.entry_style, width=20, state=DISABLED)
        self.insert_entry_desabilitado(cb_tipo_sessao, trabalho[4])
        cb_tipo_sessao.grid(column=1, row=1, padx=self.paddingx, sticky="W")
        self.entry_tipo = cb_tipo_sessao

        lb_plano = Label(separador3, text="Plano", font=self.lb_style)
        lb_plano.grid(column=3, row=0, sticky="W", padx=self.paddingx)
        cb_plano = Entry(separador3, font=self.entry_style, width=20, state=DISABLED)
        self.insert_entry_desabilitado(cb_plano, trabalho[6])
        cb_plano.grid(column=3, row=1, padx=self.paddingx, sticky="W")
        self.entry_plano = cb_plano

        separador4 = Separator(janela, orient="horizontal")
        separador4.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        opcoes_pagamento = ['DINHEIRO', 'PIX', 'CARTÃO DÉBITO', 'CARTÃO CRÉDITO', 'OUTRO']

        lb_condicao_pagamento1 = Label(separador4, text="Condicao Pagamento", font=self.lb_style)
        lb_condicao_pagamento1.grid(column=0, row=0, sticky="W", padx=self.paddingx, columnspan=2)

        lb_valor = Label(separador4, text="Valor", font=self.lb_style)
        lb_valor.grid(column=3, row=0, sticky="W", padx=self.paddingx, columnspan=2)

        lb_total = Label(separador4, text="Total", font=self.lb_style)
        lb_total.grid(column=5, row=0, sticky="W", padx=self.paddingx)

        entry_total = Entry(separador4, font=self.entry_style, width=10, state=DISABLED)

        lb_condicao_pagamento_numero1 = Label(separador4, text="1º", font=self.lb_style)
        lb_condicao_pagamento_numero1.grid(column=0, row=1, padx=self.paddingx, pady=self.paddingy)
        cb_condicao_pagamento1 = Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento,
                                          state="readonly")
        cb_condicao_pagamento1.set(trabalho[11])
        cb_condicao_pagamento1.grid(column=1, row=1, padx=self.paddingx, pady=self.paddingy)
        entry_valor1 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor1.grid(column=3, row=1, padx=self.paddingx, pady=self.paddingy)
        entry_valor1.insert(END, trabalho[12])

        lb_condicao_pagamento_numero2 = Label(separador4, text="2º", font=self.lb_style)
        lb_condicao_pagamento_numero2.grid(column=0, row=2, padx=self.paddingx, pady=self.paddingy)
        cb_condicao_pagamento2 = Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento,
                                          state="readonly")
        cb_condicao_pagamento2.set(trabalho[13])
        cb_condicao_pagamento2.grid(column=1, row=2, padx=self.paddingx, pady=self.paddingy)
        entry_valor2 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor2.grid(column=3, row=2, padx=self.paddingx, pady=self.paddingy)
        entry_valor2.insert(END, trabalho[14])

        lb_condicao_pagamento_numero3 = Label(separador4, text="3º", font=self.lb_style)
        lb_condicao_pagamento_numero3.grid(column=0, row=3, padx=self.paddingx, pady=self.paddingy)
        cb_condicao_pagamento3 = Combobox(separador4, font=self.entry_style, width=10, values=opcoes_pagamento,
                                          state="readonly")
        cb_condicao_pagamento3.set(trabalho[15])
        cb_condicao_pagamento3.grid(column=1, row=3, padx=self.paddingx, pady=self.paddingy)
        entry_valor3 = Entry(separador4, font=self.entry_style, width=10)
        entry_valor3.grid(column=3, row=3, padx=self.paddingx, pady=self.paddingy)
        entry_valor3.insert(END, trabalho[16])
        def soma_condicao_pagamento(event):
            try:
                valor1 = entry_valor1.get().replace(",", ".")
                valor2 = entry_valor2.get().replace(",", ".")
                valor3 = entry_valor3.get().replace(",", ".")
                self.lb_aviso_erro['text'] = "."
                self.valores_pagamento = []

                if valor1 == '':
                    valor1 = "0"
                    valor1 = float(valor1)
                else:
                    valor1 = float(valor1)
                if valor2 == '':
                    valor2 = "0"
                    valor2 = float(valor2)
                else:
                    valor2 = float(valor2)
                if valor3 == '':
                    valor3 = "0"
                    valor3 = float(valor3)
                else:
                    valor3 = float(valor3)

                total = str(valor1 + valor2 + valor3)
                self.valores_pagamento.append(valor1)
                self.valores_pagamento.append(valor2)
                self.valores_pagamento.append(valor3)
                self.insert_entry_desabilitado(entry_total, total, 0)
                return
            except ValueError:
                self.lb_aviso_erro['text'] = "VERIFIQUE OS VALORES DO PAGAMENTO"

        entry_valor1.bind("<FocusOut>", soma_condicao_pagamento)
        entry_valor2.bind("<FocusOut>", soma_condicao_pagamento)
        entry_valor3.bind("<FocusOut>", soma_condicao_pagamento)

        entry_total.grid(column=5, row=3, padx=self.paddingx, pady=self.paddingy)
        self.insert_entry_desabilitado(entry_total, trabalho[17])

        separador5 = Separator(janela, orient="horizontal")
        separador5.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_observacoes = Label(separador5, text="Observações", font=self.lb_style)
        lb_observacoes.grid(column=0, row=0, padx=self.paddingx, pady=self.paddingy, sticky="W")
        textarea_observacoes = Text(separador5, font=self.entry_style, height=6)
        textarea_observacoes.grid(column=0, row=1, padx=self.paddingx, pady=self.paddingy, sticky="W")
        self.set_textarea(textarea_observacoes, trabalho[18])
        def coleta_argumentos():
            argumentos = []
            argumentos.append(entry_codigo.get())
            argumentos.append(entry_cadastro.get())
            argumentos.append(entry_data_sessao.get())
            argumentos.append(self.entry_horario_sessao.get())
            argumentos.append(entry_nome.get())
            argumentos.append(self.codigo_pessoa_trabalho)
            argumentos.append(cb_tipo_sessao.get())
            argumentos.append(cb_plano.get())
            argumentos.append(entry_valor1.get())
            argumentos.append(entry_valor2.get())
            argumentos.append(entry_valor3.get())
            argumentos.append(entry_total.get())
            argumentos.append(textarea_observacoes.get("1.0", "end-1c"))
            self.argumentos = argumentos

        def buscar_pessoa_trabalho_args():
            coleta_argumentos()
            self.buscar_pessoa_trabalho(janela)

        bt_busca_pessoa = Button(separador2, text="busca", font=self.btn_style, command=buscar_pessoa_trabalho_args)
        bt_busca_pessoa.grid(column=0, row=1)

        def buscar_tipos_sessao_trabalho_args():
            coleta_argumentos()
            self.class_tipos.janela_tipos(tipo="escolha")

        bt_busca_sessao = Button(separador3, text="busca", font=self.btn_style,
                                 command=buscar_tipos_sessao_trabalho_args)
        bt_busca_sessao.grid(column=0, row=1)

        def buscar_plano_sessao_trabalho_args():
            coleta_argumentos()
            self.class_planos.janela_planos(tipo="escolha")

        bt_busca_plano = Button(separador3, text="busca", font=self.btn_style,
                                command=buscar_plano_sessao_trabalho_args)
        bt_busca_plano.grid(column=2, row=1)

        separador9 = Separator(janela, orient="horizontal")
        separador9.pack(fill="x", pady=10, padx=10)

        if self.argumentos is not None:
            self.insert_entry_desabilitado(entry_codigo, self.argumentos[0])
            self.set_text_entry(entry_cadastro, self.argumentos[1])
            self.set_text_entry(entry_data_sessao, self.argumentos[2])
            self.set_text_entry(self.entry_horario_sessao, self.argumentos[3])
            self.set_text_entry(entry_nome, self.nome_pessoa_trabalho)
            self.insert_entry_desabilitado(cb_tipo_sessao, self.nome_tipo_trabalho)
            self.insert_entry_desabilitado(cb_plano, self.nome_plano_trabalho)
            self.set_text_entry(entry_valor1, self.argumentos[8])
            self.set_text_entry(entry_valor2, self.argumentos[9])
            self.set_text_entry(entry_valor3, self.argumentos[10])
            self.insert_entry_desabilitado(entry_total, self.argumentos[11])
            self.set_textarea(textarea_observacoes, self.argumentos[12])

        def altera_db_trabalho_args():
            if self.nome_pessoa_trabalho is None:
                self.lb_aviso_erro['text'] = "Nome é obrigatório"
            elif self.nome_tipo_trabalho is None:
                self.lb_aviso_erro['text'] = "Tipo da Sessão é obrigatório"
            elif self.nome_plano_trabalho is None:
                self.lb_aviso_erro['text'] = "Plano é obrigatório"
            elif len(self.valores_pagamento) == 0:
                self.lb_aviso_erro['text'] = "Insira ao menos uma forma de pagamento"
            else:
                altera_db_trabalhos(entry_codigo.get, entry_cadastro.get, entry_data_sessao.get,
                                   self.entry_horario_sessao.get, self.codigo_pessoa_trabalho, entry_nome.get,
                                   cb_tipo_sessao.get, self.codigo_tipo_trabalho, cb_plano.get,
                                   self.codigo_plano_trabalho, cb_condicao_pagamento1.get, self.valores_pagamento[0],
                                   cb_condicao_pagamento2.get, self.valores_pagamento[1], cb_condicao_pagamento3.get,
                                   self.valores_pagamento[2], entry_total.get, textarea_observacoes.get)
                self.retorna_variaveis_none_trabalhos()
                janela.destroy()
                self.janela_trabalhos_var.destroy()
                self.janela_trabalhos()

        grava = Button(separador9, text="GRAVA", font=self.lb_style, command=altera_db_trabalho_args)
        grava.grid(column=0, row=0, sticky="WS")

        def cancelar():
            self.retorna_variaveis_none_trabalhos()
            janela.destroy()

        cancela = Button(separador9, text="CANCELA", font=self.lb_style, command=cancelar)
        cancela.grid(column=1, row=0, sticky="WS")

    def exclui_cadastro_trabalho(self):
        print("Tela ainda não cadastrada")
        pass
    def barra_filtros_opcoes_trabalho(self,barra_filtros):
        # opções 1
        barra_filtro_opcoes = Separator(barra_filtros, orient="vertical")
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

    def barra_filtros_status_trabalho(self, barra_filtros):
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

    def lista_de_trabalho(self,janela):
        lista = pega_todas_trabalhos_lista()

        lista_trabalho = Treeview(janela, columns=("col1", "col2", "col3","col4","col5","col6","col7"))
        lista_trabalho.heading("#0", text="")
        lista_trabalho.heading("#1", text="Cod")
        lista_trabalho.heading("#2", text="Data")
        lista_trabalho.heading("#3", text="hora")
        lista_trabalho.heading("#4", text="Nome")
        lista_trabalho.heading("#5", text="Tipo sessão")
        lista_trabalho.heading("#6", text="Plano")
        lista_trabalho.heading("#7", text="Etapa")

        lista_trabalho.column("#0", width=0)
        lista_trabalho.column("#1", width=50)
        lista_trabalho.column("#2", width=100)
        lista_trabalho.column("#3", width=100)
        lista_trabalho.column("#4", width=300)
        lista_trabalho.column("#5", width=200)
        lista_trabalho.column("#6", width=127)
        lista_trabalho.column("#7", width=128)

        lista_trabalho.grid(column=0, row=0, sticky="WSNE")

        for i in lista:
            lista_trabalho.insert("",END,values=i)

        barra_rolagem = Scrollbar(janela, orient="vertical")
        lista_trabalho.configure(yscrollcommand=barra_rolagem)
        barra_rolagem.grid(column=1, row=0, sticky="WSNE")

        self.lista_de_trabalhos = lista_trabalho

    def informacoes_adicionais_trabalho(self,janela):
        separador1 = Separator(janela, orient="horizontal")
        separador1.pack(fill="x", side=BOTTOM, padx=self.paddingx, pady=self.paddingy+10)

        separador2 = Separator(separador1, orient="horizontal")
        separador2.grid(column=0,row=0,rowspan=3)

        lb_observacoes = Label(separador2, text="Observações", font=self.lb_style)
        lb_observacoes.grid(column=0, row=0, sticky="NW", padx=self.paddingx, rowspan=3)
        entry_observacoes = Text(separador2, font=self.entry_style, width=78,height=3, state=DISABLED,pady=self.paddingy)
        entry_observacoes.grid(column=1, row=0, padx=self.paddingx,sticky="NW")

        separador3 = Separator(separador2, orient="horizontal")
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

        return entry_observacoes, entry_valor, entry_pago, entry_devendo
        # entry_numero.grid(column=3, row=0, padx=self.paddingx, sticky="ew")

    def janela_trabalhos(self, btn_grava_escolhe = None):
        janela_trabalhos = Toplevel()

        self.configurar_janela_auxiliar(janela_trabalhos)

        funcoes = [self.novo_cadastro_trabalho, self.altera_cadastro_trabalho, self.exclui_cadastro_trabalho]

        barra_alteracoes = self.barra_alteracoes(janela_trabalhos,funcoes)

        bt_planos = Button(barra_alteracoes, text="Planos",padx=5,pady=10,font=("monospace", 10), command=self.class_planos.janela_planos)
        bt_planos.pack(side = LEFT, padx=self.paddingx+20)

        barra_filtros = Separator(janela_trabalhos, orient="horizontal")
        barra_filtros.pack(fill="x")

        listagem_trabalhos = Separator(janela_trabalhos, orient="horizontal")
        listagem_trabalhos.pack(fill="x")

        self.barra_filtros_opcoes_trabalho(barra_filtros)
        self.barra_filtros_status_trabalho(barra_filtros)
        self.barra_filtros_pesquisa(barra_filtros)
        self.lista_de_trabalho(listagem_trabalhos)
        entry_observacoes, entry_valor, entry_pago, entry_devendo = self.informacoes_adicionais_trabalho(janela_trabalhos)

        def adiciona_informacoes_adicionais(event):

            for selected_item in self.lista_de_trabalhos.selection():
                item = self.lista_de_trabalhos.item(selected_item,'values')
                trabalho = pega_um_item_trabalho(item[0])

                self.set_textarea(entry_observacoes,trabalho[0][18])
                self.insert_entry_desabilitado(entry_valor, trabalho[0][17])
                #self.insert_entry_desabilitado(entry_pago, trabalho[0][1])
                #self.insert_entry_desabilitado(entry_devendo, trabalho[0][18])

        if btn_grava_escolhe == "escolhe":
            def funcao(event):
                pessoa = None
                for selected_item in self.lista_de_trabalhos.selection():
                    item = self.lista_de_trabalhos.item(selected_item, 'values')
                    trabalho = pega_um_item_trabalho(item[0])
                    self.janela_trabalhos_var.set_codigo_nome_trabalho(trabalho[0][0],trabalho[0][2])
                    self.lista_de_trabalhos.destroy()
                    return

            self.lista_de_trabalhos.bind("<Double-1>", funcao)

        self.lista_de_trabalhos.bind("<Button-1>", adiciona_informacoes_adicionais)

        janela_trabalhos.title("Pesquisa de Trabalhos")
        self.janela_trabalhos_var = janela_trabalhos

