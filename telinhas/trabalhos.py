from modulos.auxiliares import Funcs
from modulos.database import pega_ultimo_id,grava_db_trabalhos

from tkinter import Toplevel, LEFT, Button,Label,Entry,DISABLED,END,Text
from tkinter.ttk import Separator, Combobox


class Trabalhos(Funcs):

    def __init__(self):
        super().__init__()
        class_funcs = Funcs()
        self.janela_trabalhos_var = None
        self.lista_de_trabalhos = None
        self.nome_pessoa_trabalho = None
        self.codigo_pessoa_trabalho = None
        self.codigo_tipo_trabalho = None
        self.nome_tipo_trabalho = None
        self.codigo_plano_trabalho = None
        self.nome_plano_trabalho = None
        self.valores_pagamento = []

    def buscar_pessoa_trabalho(self,janela_trabalhos):
        self.janela_pessoas(btn_grava_escolhe = "escolhe", janela_trabalhos = janela_trabalhos)

    def novo_cadastro_trabalho(self):
        janela = Toplevel()
        janela.focus_force()

        janela.title("Cadastro Trabalho")

        self.configurar_janela_auxiliar(janela)

        separador1 = Separator(janela, orient="horizontal")
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

        separador2 = Separator(janela, orient="horizontal")
        separador2.pack(fill="x", padx=self.paddingx, pady=self.paddingy)

        lb_nome = Label(separador2, text="Nome", font=self.lb_style)
        lb_nome.grid(column=1, row=0, sticky="W", padx=self.paddingx)
        entry_nome = Entry(separador2, font=self.entry_style, width=89)
        entry_nome.grid(column=1, row=1, padx=self.paddingx)

        separador3 = Separator(janela, orient="horizontal")
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
        lb_aviso_valores = Label(separador4, text="", font=self.lb_style)
        lb_aviso_valores.grid(column=6, row=1, sticky="W", padx=self.paddingx)

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

        separador9 = Separator(janela, orient="horizontal")
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
            if self.nome_pessoa_trabalho is None:
                lb_aviso_valores['text'] = "Nome é obrigatório"
            elif self.nome_tipo_trabalho is None:
                lb_aviso_valores['text'] = "Tipo da Sessão é obrigatório"
            elif self.nome_plano_trabalho is None:
                lb_aviso_valores['text'] = "Plano é obrigatório"
            elif len(self.valores_pagamento) == 0:
                lb_aviso_valores['text'] = "Insira ao menos uma forma de pagamento"
            else:
                grava_db_trabalhos(entry_codigo.get,entry_cadastro.get,entry_data_sessao.get,entry_horario_sessao.get,self.codigo_pessoa_trabalho,entry_nome.get,cb_tipo_sessao.get,self.codigo_tipo_trabalho,cb_plano.get,self.codigo_plano_trabalho,cb_condicao_pagamento1.get,self.valores_pagamento[0],cb_condicao_pagamento2.get,self.valores_pagamento[1],cb_condicao_pagamento3.get,self.valores_pagamento[2],entry_total.get,textarea_observacoes.get)
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

    def janela_trabalhos(self):
        janela_trabalhos = Toplevel()

        self.configurar_janela_auxiliar(janela_trabalhos)


        funcoes = [self.novo_cadastro_trabalho, self.altera_cadastro_trabalho, self.exclui_cadastro_trabalho]

        barra_alteracoes = self.barra_alteracoes(janela_trabalhos,funcoes)

        bt_planos = Button(barra_alteracoes, text="Planos",padx=5,pady=10,font=("monospace", 10), command=self.buscar_tipos_sessao_trabalho)
        bt_planos.pack(side = LEFT, padx=self.paddingx+20)

        barra_filtros = Separator(janela_trabalhos, orient="horizontal")
        barra_filtros.pack(fill="x")

        listagem_trabalhos = Separator(janela_trabalhos, orient="horizontal")
        listagem_trabalhos.pack(fill="x")

        self.barra_filtros_opcoes_trabalho(barra_filtros)
        self.barra_filtros_status_trabalho(barra_filtros)
        self.barra_filtros_pesquisa(barra_filtros)
        self.lista_de_trabalho(listagem_trabalhos)
        self.informacoes_adicionais_trabalho(janela_trabalhos)

        janela_trabalhos.title("Pesquisa de Trabalhos")
        self.janela_trabalhos_var = janela_trabalhos
