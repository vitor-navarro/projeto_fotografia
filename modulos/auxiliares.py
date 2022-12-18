from datetime import date
from tkinter import END, Button, LEFT, StringVar, Label, Radiobutton, Entry
from tkinter.ttk import Separator

from modulos.validadores import Validadores
class Funcs():

    def __init__(self):
        self.validadores = Validadores()
        self.lb_style = ("monospace", 12)
        self.paddingx = 10
        self.paddingy = 7
        self.entry_style = ("monospace", 14)
        self.btn_style = ("monospace", 12)
        self.data_sistema = date.today().strftime('%d/%m/%Y')

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

    def barra_alteracoes(self,janela, funcoes):
        barra_alteracoes = Separator(janela, orient="horizontal")
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

    def barra_filtros_pesquisa(self, barra_filtros):
        barra_filtro_opcoes3 = Separator(barra_filtros, orient="horizontal")
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

    def replace_virgula_ponto(self, valor):
        valor = valor.replace(",", ".")
        return valor

    def entry_data(self, janela):
        entry = Entry(janela)
        entry.config(validate="key", validatecommand=(entry.register(self.validadores.validador_data), "%P"))

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