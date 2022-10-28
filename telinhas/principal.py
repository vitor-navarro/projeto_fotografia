from tkinter import *
from tkinter import ttk

def sem_comando():
    print("Tela ainda não cadastrada")




def janela_principal():
    janela = Tk()
    #pre config

    janela.title("Projeto fotografia")
    janela.state("zoomed")


    barra_menu = ttk.Separator(janela,orient="horizontal")
    barra_menu.pack(fill="x")

    pessoas = Button(barra_menu, text="PESSOAS",font=("monospace", 12), command=janela_pessoas, padx=10, pady=30)
    pessoas.pack(side=LEFT)

    trabalhos = Button(barra_menu, text="TRABALHOS",font=("monospace", 12), command=janela_trabalhos, padx=10, pady=30)
    trabalhos.pack(side=LEFT)

    financeiro = Button(barra_menu, text="FINANCEIRO",font=("monospace", 12), command=janela_financeiro, padx=10, pady=30)
    financeiro.pack(side=LEFT)


    janela.mainloop()

def configurar_janela_auxiliar(janela):

    janela.update_idletasks()

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = int((screen_width / 2) - (964 / 2) - 50)
    y = int((screen_height / 2) - (580 / 2) - 50)

    janela.geometry("+%d+%d" % (x, y))

    janela.geometry("1024x624")


def janela_pessoas():
    janela_pessoas = Toplevel()

    configurar_janela_auxiliar(janela_pessoas)

    barra_alteracoes = ttk.Separator(janela_pessoas,orient="horizontal")
    barra_alteracoes.pack(fill="x")

    novo = Button(barra_alteracoes, text="Novo",font=("monospace", 10), command=sem_comando, padx=5, pady=10)
    novo.pack(side=LEFT)

    alterar = Button(barra_alteracoes, text="Alterar",font=("monospace", 10), command=sem_comando, padx=5, pady=10)
    alterar.pack(side=LEFT)

    excluir = Button(barra_alteracoes, text="Excluir",font=("monospace", 10), command=sem_comando, padx=5, pady=10)
    excluir.pack(side=LEFT)

    #to do
    barra_filtros = ttk.Separator(janela_pessoas,orient="horizontal")
    barra_filtros.pack(fill="x")



    #to do
    barra_lista_pessoas = ttk.Separator(janela_pessoas,orient="horizontal")
    barra_lista_pessoas.pack(fill="x")



    janela_pessoas.title("Pesquisa de Pessoas")

def janela_trabalhos():
    janela_trabalhos = Toplevel()

    janela_trabalhos.title("Pesquisa de Trabalhos")

def janela_financeiro():
    janela_financeiro = Toplevel()

    janela_financeiro.title("Controle Financeiro")
'''def barra_menu(janela):
    menus = Menu(janela)

    menuCadastroClientes = Menu(menus)
    menuCadastroClientes.add_command(label="Cadastros",command=sem_comando)

    menuFinalizar = Menu(menus)
    menuFinalizar.add_command(label="Cadastros",command=sem_comando)

    return menus'''

if __name__ == '__main__':

    janela_principal()