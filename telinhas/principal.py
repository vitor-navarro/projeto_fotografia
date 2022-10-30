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



    barra_filtros = ttk.Separator(janela_pessoas,orient="horizontal")
    barra_filtros.pack(fill="x")

    barra_filtro_opcoes = ttk.Separator(barra_filtros,orient="vertical")
    barra_filtro_opcoes.grid(column=0, row=0,sticky="W")

    varaivel_opcoes = StringVar(barra_filtro_opcoes, value="nome_fantasia")

    label_opcoes = Label(barra_filtro_opcoes, text="Opções")
    label_opcoes.grid(column=0, row=0, columnspan=2, sticky="W")

    rb_codigo = Radiobutton(barra_filtro_opcoes, text="Código", value="codigo", variable=varaivel_opcoes)
    rb_codigo.grid(column=0, row=1, sticky="W")

    rb_nome_fantasia = Radiobutton(barra_filtro_opcoes, text="nome/fantasia", value="nome_fantasia", variable=varaivel_opcoes)
    rb_nome_fantasia.grid(column=0, row=2, sticky="W")

    rb_nome = Radiobutton(barra_filtro_opcoes, text="nome", value="nome", variable=varaivel_opcoes)
    rb_nome.grid(column=0, row=3, sticky="W")

    rb_fantasia = Radiobutton(barra_filtro_opcoes, text="fantasia", value="fantasia", variable=varaivel_opcoes)
    rb_fantasia.grid(column=0, row=4, sticky="W")

    rb_cidade = Radiobutton(barra_filtro_opcoes, text="cidade", value="cidade", variable=varaivel_opcoes)
    rb_cidade.grid(column=1, row=1, sticky="W")

    rb_endereco = Radiobutton(barra_filtro_opcoes, text="endereco", value="endereco", variable=varaivel_opcoes)
    rb_endereco.grid(column=1, row=2, sticky="W")

    rb_cpf_cnpj = Radiobutton(barra_filtro_opcoes, text="cpf/cnpj", value="cpf_cnpj", variable=varaivel_opcoes)
    rb_cpf_cnpj.grid(column=1, row=3, sticky="W")

    rb_bairro = Radiobutton(barra_filtro_opcoes, text="bairro", value="bairro", variable=varaivel_opcoes)
    rb_bairro.grid(column=1, row=4, sticky="W")

    rb_nome_fantasia.select()


    barra_filtro_opcoes2 = ttk.Separator(barra_filtros,orient="vertical")
    barra_filtro_opcoes2.grid(column=1, row=0,sticky="W")

    varaivel_opcoes2 = StringVar(barra_filtro_opcoes2, value="nome_fantasia")

    label_opcoes = Label(barra_filtro_opcoes2, text="Status")
    label_opcoes.grid(column=0, row=0, columnspan=2, sticky="W")

    rb_ativo = Radiobutton(barra_filtro_opcoes2, text="ativos", value="ativo", variable=varaivel_opcoes2)
    rb_ativo.grid(column=0, row=1, sticky="W")

    rb_terminado = Radiobutton(barra_filtro_opcoes2, text="Terminados", value="terminado",variable=varaivel_opcoes2)
    rb_terminado.grid(column=0, row=2, sticky="W")

    rb_todos = Radiobutton(barra_filtro_opcoes2, text="Todos", value="todos",
                                   variable=varaivel_opcoes2)
    rb_todos.grid(column=0, row=3, sticky="W")

    label_vazio = Label(barra_filtro_opcoes2, text="")
    label_vazio.grid(column=0, row=4, sticky="W")

    rb_ativo.select()


    janela_pessoas.title("Pesquisa de Pessoas")
    seleciona()
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