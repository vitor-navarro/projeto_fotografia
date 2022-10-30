from tkinter import *
from tkinter import ttk

def configurar_janela_auxiliar(janela):
    janela.update_idletasks()

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = int((screen_width / 2) - (964 / 2) - 50)
    y = int((screen_height / 2) - (580 / 2) - 50)

    janela.geometry("+%d+%d" % (x, y))

    janela.geometry("1024x624")

#substituir por tk
janela = Tk()

configurar_janela_auxiliar(janela)

lb_style = ("monospace", 12)

separador1 = ttk.Separator(janela)
separador1.pack()



lb_codigo = Label(separador1, text="Código", font=lb_style)
lb_codigo.grid(column=0, row=0, sticky="W")
entry_codigo = Entry(separador1, font=lb_style, width=8,state=DISABLED)
entry_codigo.grid(column=0, row=1)

lb_cadastro = Label(separador1, text="Cadastro", font=lb_style)
lb_cadastro.grid(column=1, row=0, sticky="W")
entry_cadastro = Entry(separador1, font=lb_style, width=8)
entry_cadastro.grid(column=1, row=1)

#mudar para opções
lb_status = Label(separador1, text="Status", font=lb_style)
lb_status.grid(column=2, row=0, sticky="W")
entry_status = Entry(separador1, font=lb_style, width=8,state=DISABLED)
entry_status.grid(column=2, row=1)

#mudar para opções
lb_tipo = Label(separador1, text="Tipo", font=lb_style)
lb_tipo.grid(column=3, row=0, sticky="W")
entry_tipo = Entry(separador1, font=lb_style, width=8,state=DISABLED)
entry_tipo.grid(column=3, row=1)


separador2 = ttk.Separator(janela)
separador2.pack()

#condicao para mudar quando for tipo juridica
lb_cpf_cnpj = Label(separador2, text="CPF", font=lb_style)
lb_cpf_cnpj.grid(column=0, row=0, sticky="W")
entry_cpf_cnpj = Entry(separador2, font=lb_style, width=20)
entry_cpf_cnpj.grid(column=0, row=1)

#condicao para mudar quando for tipo juridica
lb_rg_inscricao = Label(separador2, text="RG", font=lb_style)
lb_rg_inscricao.grid(column=1, row=0, sticky="W")
entry_rg_inscricao = Entry(separador2, font=lb_style, width=20)
entry_rg_inscricao.grid(column=1, row=1)

lb_nascimento = Label(separador2, text="Nascimento", font=lb_style)
lb_nascimento.grid(column=2, row=0, sticky="W")
entry_nascimento = Entry(separador2, font=lb_style, width=20)
entry_nascimento.grid(column=2, row=1)

separador3 = ttk.Separator(janela)
separador3.pack()

lb_nome = Label(separador3, text="Nome*", font=lb_style)
lb_nome.grid(column=0, row=0, sticky="W")
entry_nome = Entry(separador3, font=lb_style)
entry_nome.grid(column=0, row=1)

lb_apelido = Label(separador3, text="Apelido", font=lb_style)
lb_apelido.grid(column=0, row=2, sticky="W")
entry_apelido = Entry(separador3, font=lb_style)
entry_apelido.grid(column=0, row=3)

separador4 = ttk.Separator(janela)
separador4.pack()

lb_endereco = Label(separador4, text="Endereço", font=lb_style)
lb_endereco.grid(column=0, row=0, sticky="W")
entry_endereco = Entry(separador4, font=lb_style)
entry_endereco.grid(column=0, row=1)

lb_numero = Label(separador4, text="Numero", font=lb_style)
lb_numero.grid(column=1, row=0, sticky="W")
entry_numero = Entry(separador4, font=lb_style)
entry_numero.grid(column=1, row=1)

lb_complemento = Label(separador4, text="Complemento", font=lb_style)
lb_complemento.grid(column=0, row=2, sticky="W")
entry_complemento = Entry(separador4, font=lb_style)
entry_complemento.grid(column=0, row=3)

lb_bairro = Label(separador4, text="Bairro", font=lb_style)
lb_bairro.grid(column=1, row=2, sticky="W")
entry_bairro = Entry(separador4, font=lb_style)
entry_bairro.grid(column=1, row=3)

lb_cidade = Label(separador4, text="Cidade", font=lb_style)
lb_cidade.grid(column=0, row=4, sticky="W")
entry_cidade = Entry(separador4, font=lb_style)
entry_cidade.grid(column=0, row=5)

lb_nome_cidade = Label(separador4, text="Nome da cidade", font=lb_style)
lb_nome_cidade.grid(column=1, row=4, sticky="W")
entry_nome_cidade = Entry(separador4, font=lb_style)
entry_nome_cidade.grid(column=1, row=5)

lb_uf = Label(separador4, text="UF", font=lb_style)
lb_uf.grid(column=2, row=4, sticky="W")
entry_uf = Entry(separador4, font=lb_style)
entry_uf.grid(column=2, row=5)

lb_cep = Label(separador4, text="CEP", font=lb_style)
lb_cep.grid(column=3, row=4, sticky="W")
entry_cep = Entry(separador4, font=lb_style)
entry_cep.grid(column=3, row=5)


separador5 = ttk.Separator(janela)
separador5.pack()

lb_fone1 = Label(separador5, text="Fone 1", font=lb_style)
lb_fone1.grid(column=0, row=0, sticky="W")
entry_fone1 = Entry(separador5, font=lb_style)
entry_fone1.grid(column=0, row=1)

lb_operadora1 = Label(separador5, text="Operadora", font=lb_style)
lb_operadora1.grid(column=1, row=0, sticky="W")
entry_operadora1 = Entry(separador5, font=lb_style)
entry_operadora1.grid(column=1, row=1)

lb_fone2 = Label(separador5, text="Fone 2", font=lb_style)
lb_fone2.grid(column=2, row=0, sticky="W")
entry_fone2 = Entry(separador5, font=lb_style)
entry_fone2.grid(column=2, row=1)

lb_operadora2 = Label(separador5, text="Operadora", font=lb_style)
lb_operadora2.grid(column=3, row=0, sticky="W")
entry_operadora1 = Entry(separador5, font=lb_style)
entry_operadora1.grid(column=3, row=1)

lb_fone3 = Label(separador5, text="Fone 3", font=lb_style)
lb_fone3.grid(column=4, row=0, sticky="W")
entry_fone3 = Entry(separador5, font=lb_style)
entry_fone3.grid(column=4, row=1)

lb_operadora3 = Label(separador5, text="Operadora", font=lb_style)
lb_operadora3.grid(column=5, row=0, sticky="W")
entry_operadora3 = Entry(separador5, font=lb_style)
entry_operadora3.grid(column=5, row=1)


separador6 = ttk.Separator(janela)
separador6.pack()

lb_email = Label(separador6, text="Email", font=lb_style)
lb_email.grid(column=0, row=0, sticky="W")
entry_email = Entry(separador6, font=lb_style)
entry_email.grid(column=0, row=1)


#retirar
janela.mainloop()