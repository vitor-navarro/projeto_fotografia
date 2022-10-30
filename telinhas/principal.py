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

def novo_cadastro():
    print("Tela ainda não cadastrada")
    pass
def altera_cadastro():
    print("Tela ainda não cadastrada")
    pass
def exclui_cadastro():
    print("Tela ainda não cadastrada")
    pass
def janela_pessoas():
    janela_pessoas = Toplevel()

    configurar_janela_auxiliar(janela_pessoas)

    barra_alteracoes = ttk.Separator(janela_pessoas,orient="horizontal")
    barra_alteracoes.pack(fill="x")

    novo = Button(barra_alteracoes, text="Novo",font=("monospace", 10), command=novo_cadastro, padx=5, pady=10)
    novo.pack(side=LEFT)

    alterar = Button(barra_alteracoes, text="Alterar",font=("monospace", 10), command=sem_comando, padx=5, pady=10)
    alterar.pack(side=LEFT)

    excluir = Button(barra_alteracoes, text="Excluir",font=("monospace", 10), command=sem_comando, padx=5, pady=10)
    excluir.pack(side=LEFT)


    barra_filtros = ttk.Separator(janela_pessoas,orient="horizontal")
    barra_filtros.pack(fill="x")

    listagem_pessoas = ttk.Separator(janela_pessoas,orient="horizontal")
    listagem_pessoas.pack(fill="x")


    #opções 1
    barra_filtro_opcoes = ttk.Separator(barra_filtros,orient="vertical")
    barra_filtro_opcoes.grid(column=0, row=0,sticky="W")

    varaivel_opcoes = StringVar(barra_filtro_opcoes)

    label_opcoes = Label(barra_filtro_opcoes, text="Filtros")
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

    #opções 2
    barra_filtro_opcoes2 = ttk.Separator(barra_filtros,orient="vertical")
    barra_filtro_opcoes2.grid(column=1, row=0,sticky="W")

    varaivel_opcoes2 = StringVar(barra_filtro_opcoes2, value="nome_fantasia")

    label_opcoes2 = Label(barra_filtro_opcoes2, text="Status")
    label_opcoes2.grid(column=0, row=0, columnspan=2, sticky="W")

    rb_ativo = Radiobutton(barra_filtro_opcoes2, text="ativos", value="ativo", variable=varaivel_opcoes2)
    rb_ativo.grid(column=0, row=1, sticky="W")

    rb_terminado = Radiobutton(barra_filtro_opcoes2, text="Terminados", value="terminado",variable=varaivel_opcoes2)
    rb_terminado.grid(column=0, row=2, sticky="W")

    rb_todos = Radiobutton(barra_filtro_opcoes2, text="Todos", value="todos",variable=varaivel_opcoes2)
    rb_todos.grid(column=0, row=3, sticky="W")

    label_vazio = Label(barra_filtro_opcoes2, text="")
    label_vazio.grid(column=0, row=4, sticky="W")

    rb_ativo.select()

    #opções 3
    barra_filtro_opcoes3 = ttk.Separator(barra_filtros, orient="horizontal")
    barra_filtro_opcoes3.grid(column=2, row=0, sticky="NE")

    varaivel_opcoes3 = StringVar(barra_filtro_opcoes3)

    label_opcoes3 = Label(barra_filtro_opcoes3, text="Pesquisa")
    label_opcoes3.grid(column=0, row=0, sticky="N")

    rb_inicio = Radiobutton(barra_filtro_opcoes3, text="Inicio", value="inicio", variable=varaivel_opcoes3)
    rb_inicio.grid(column=0, row=1, sticky="E")

    rb_aproximacao = Radiobutton(barra_filtro_opcoes3, text="Aproximação", value="aproximacao",variable=varaivel_opcoes3)
    rb_aproximacao.grid(column=1, row=1, sticky="E")

    rb_qualquer_parte = Radiobutton(barra_filtro_opcoes3, text="Qualquer parte", value="qualquer_parte",variable=varaivel_opcoes3)
    rb_qualquer_parte.grid(column=2, row=1, sticky="E")

    rb_exato = Radiobutton(barra_filtro_opcoes3, text="Exato", value="exato",variable=varaivel_opcoes3)
    rb_exato.grid(column=3, row=1, sticky="E")

    rb_aproximacao.select()

    pessoa = [1,"vitor","091.861.449-01","são jorge do ivai"]

    lista_pessoas = ttk.Treeview(listagem_pessoas, columns=("col1","col2","col3"))
    lista_pessoas.heading("#0",text="Cod")
    lista_pessoas.heading("#1",text="Nome")
    lista_pessoas.heading("#2",text="CPF/CNPJ")
    lista_pessoas.heading("#3",text="Cidade")

    lista_pessoas.column("#0",width=50)
    lista_pessoas.column("#1",width=450)
    lista_pessoas.column("#2",width=204)
    lista_pessoas.column("#3",width=300)

    lista_pessoas.grid(column=0,row=0,sticky="WSNE")

    barra_rolagem = Scrollbar(listagem_pessoas, orient="vertical")
    lista_pessoas.configure(yscrollcommand=barra_rolagem)
    barra_rolagem.grid(column=1,row=0,sticky="WSNE")

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