from tkinter import *
from tkinter import ttk
from datetime import date
from modulos.auxiliares import Funcs
from telas.financeiro import Financeiro
from telas.pessoas import Pessoas
from telas.trabalhos import Trabalhos


class Aplicacao(Funcs):
    def __init__(self):
        super().__init__()
        self.pessoas = Pessoas()
        self.trabalhos = Trabalhos()
        self.financeiro = Financeiro()
        self.funcs = Funcs()
        self.lb_style = ("monospace", 12)
        self.paddingx = 10
        self.paddingy = 7
        self.entry_style = ("monospace", 14)
        self.btn_style = ("monospace", 12)
        self.data = date.today().strftime('%d/%m/%Y')
        self.lista_de_pessoas = None

        janela = Tk()
        # pre config

        janela.title("Projeto fotografia")
        janela.state("zoomed")

        barra_menu = ttk.Separator(janela, orient="horizontal")
        barra_menu.pack(fill="x")

        pessoas = Button(barra_menu, text="PESSOAS", font=("monospace", 12), command=self.pessoas.janela_pessoas, padx=10, pady=30)
        pessoas.pack(side=LEFT)

        trabalhos = Button(barra_menu, text="TRABALHOS", font=("monospace", 12), command=self.trabalhos.janela_trabalhos, padx=10,
                           pady=30)
        trabalhos.pack(side=LEFT)

        financeiro = Button(barra_menu, text="FINANCEIRO", font=("monospace", 12), command=self.financeiro.janela_financeiro, padx=10,
                            pady=30)
        financeiro.pack(side=LEFT)

        separador_corpo = ttk.Separator(janela, orient="horizontal")
        separador_corpo.pack(fill="x")

        barra_proximos_trabalhos = Label(separador_corpo, text="Próximos Trabalhos",font=self.lb_style, pady=self.paddingy,padx=self.paddingx)
        barra_proximos_trabalhos.pack(side=LEFT)

        janela.mainloop()


if __name__ == '__main__':

    Aplicacao()


