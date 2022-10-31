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
    janela.resizable(False,False)
#substituir por tk
janela = Tk()

configurar_janela_auxiliar(janela)



lb_style = ("monospace", 12)
entry_style = ("monospace", 14)
paddingx = 10
paddingy = 7

separador1 = ttk.Separator(janela,orient="horizontal")
separador1.pack(fill="x", padx=paddingx,pady=paddingy)


lb_codigo = Label(separador1, text="Código", font=lb_style)
lb_codigo.grid(column=0, row=0, sticky="NW",padx=paddingx)
entry_codigo = Entry(separador1, font=entry_style, width=8,state=DISABLED)
entry_codigo.grid(column=0, row=1,padx=paddingx, sticky="NW")

lb_cadastro = Label(separador1, text="Cadastro", font=lb_style)
lb_cadastro.grid(column=1, row=0, sticky="W", padx=paddingx)
entry_cadastro = Entry(separador1, font=entry_style, width=10)
entry_cadastro.grid(column=1, row=1, padx=paddingx)

status_possiveis = ["Ativo", "Inativo"]
tipos_possiveis_pessoas = ["Física", "Jurídica"]

#mudar para opções
lb_status = Label(separador1, text="Status", font=lb_style)
lb_status.grid(column=2, row=0, sticky="W", padx=paddingx)
cb_status = ttk.Combobox(separador1, font=entry_style, width=15,values=status_possiveis)
cb_status.set("Ativo")
cb_status.grid(column=2, row=1, padx=paddingx)

#mudar para opções
lb_tipo = Label(separador1, text="Tipo", font=lb_style)
lb_tipo.grid(column=3, row=0, sticky="W", padx=paddingx)
cb_tipo = ttk.Combobox(separador1, font=entry_style, width=15,values=tipos_possiveis_pessoas)
cb_tipo.set("Física")
cb_tipo.grid(column=3, row=1, padx=paddingx)

separador2 = ttk.Separator(janela,orient="horizontal")
separador2.pack(fill="x", padx=paddingx,pady=paddingy)

#condicao para mudar quando for tipo juridica
lb_cpf_cnpj = Label(separador2, text="CPF", font=lb_style)
lb_cpf_cnpj.grid(column=0, row=0, sticky="W", padx=paddingx)
entry_cpf_cnpj = Entry(separador2, font=entry_style, width=20)
entry_cpf_cnpj.grid(column=0, row=1, padx=paddingx)

#condicao para mudar quando for tipo juridica
lb_rg_inscricao = Label(separador2, text="RG", font=lb_style)
lb_rg_inscricao.grid(column=1, row=0, sticky="W", padx=paddingx)
entry_rg_inscricao = Entry(separador2, font=entry_style, width=20)
entry_rg_inscricao.grid(column=1, row=1, padx=paddingx)

lb_nascimento = Label(separador2, text="Nascimento", font=lb_style)
lb_nascimento.grid(column=2, row=0, sticky="W", padx=paddingx)
entry_nascimento = Entry(separador2, font=entry_style, width=10)
entry_nascimento.grid(column=2, row=1, padx=paddingx)


separador3 = ttk.Separator(janela,orient="horizontal")
separador3.pack(fill="x", padx=paddingx,pady=paddingy)

lb_nome = Label(separador3, text="Nome*", font=lb_style)
lb_nome.grid(column=0, row=0, sticky="W", padx=paddingx)
entry_nome = Entry(separador3, font=entry_style, width=89)
entry_nome.grid(column=0, row=1, padx=paddingx)

lb_apelido = Label(separador3, text="Apelido", font=lb_style)
lb_apelido.grid(column=0, row=2, sticky="W", padx=paddingx)
entry_apelido = Entry(separador3, font=entry_style, width=89)
entry_apelido.grid(column=0, row=3, padx=paddingx)


separador4 = ttk.Separator(janela,orient="horizontal")
separador4.pack(fill="x", padx=paddingx,pady=paddingy)

lb_endereco = Label(separador4, text="Endereço", font=lb_style)
lb_endereco.grid(column=0, row=0, sticky="W", padx=paddingx)
entry_endereco = Entry(separador4, font=entry_style,width=82)
entry_endereco.grid(column=0, row=1, padx=paddingx)

lb_numero = Label(separador4, text="Numero", font=lb_style)
lb_numero.grid(column=1, row=0, sticky="W", padx=paddingx)
entry_numero = Entry(separador4, font=entry_style,width=5)
entry_numero.grid(column=1, row=1, padx=paddingx)

separador5 = ttk.Separator(janela, orient="horizontal")
separador5.pack(fill="x", padx=paddingx, pady=paddingy)

lb_complemento = Label(separador5, text="Complemento", font=lb_style)
lb_complemento.grid(column=0, row=2, sticky="W", padx=paddingx)
entry_complemento = Entry(separador5, font=entry_style, width=44)
entry_complemento.grid(column=0, row=3, padx=paddingx)

lb_bairro = Label(separador5, text="Bairro", font=lb_style)
lb_bairro.grid(column=1, row=2, sticky="W", padx=paddingx)
entry_bairro = Entry(separador5, font=entry_style, width=43)
entry_bairro.grid(column=1, row=3, padx=paddingx)


separador6 = ttk.Separator(janela, orient="horizontal")
separador6.pack(fill="x", padx=paddingx, pady=paddingy)

lb_cidade = Label(separador6, text="Cidade", font=lb_style, state=DISABLED)
lb_cidade.grid(column=0, row=4, sticky="W", padx=paddingx)
entry_cidade = Entry(separador6, font=entry_style,width=5)
entry_cidade.grid(column=0, row=5, padx=paddingx)

lb_nome_cidade = Label(separador6, text="Nome da cidade", font=lb_style)
lb_nome_cidade.grid(column=1, row=4, sticky="W", padx=paddingx)
entry_nome_cidade = Entry(separador6, font=entry_style, width=40)
entry_nome_cidade.grid(column=1, row=5, padx=paddingx)

lb_uf = Label(separador6, text="UF", font=lb_style)
lb_uf.grid(column=2, row=4, sticky="W", padx=paddingx)
entry_uf = Entry(separador6, font=entry_style,width=3)
entry_uf.grid(column=2, row=5, padx=paddingx)

lb_cep = Label(separador6, text="CEP", font=lb_style)
lb_cep.grid(column=3, row=4, sticky="W", padx=paddingx)
entry_cep = Entry(separador6, font=entry_style,width=10)
entry_cep.grid(column=3, row=5, padx=paddingx)


separador7 = ttk.Separator(janela, orient="horizontal")
separador7.pack(fill="x", padx=paddingx, pady=paddingy)

width_fone = 17
width_operadora = 8
lb_fone1 = Label(separador7, text="Fone 1", font=lb_style)
lb_fone1.grid(column=0, row=0, sticky="W", padx=paddingx)
entry_fone1 = Entry(separador7, font=entry_style,width=width_fone)
entry_fone1.grid(column=0, row=1, padx=paddingx)

lb_operadora1 = Label(separador7, text="Operadora", font=lb_style)
lb_operadora1.grid(column=1, row=0, sticky="W", padx=paddingx)
entry_operadora1 = Entry(separador7, font=entry_style, width=width_operadora)
entry_operadora1.grid(column=1, row=1, padx=paddingx)

lb_fone2 = Label(separador7, text="Fone 2", font=lb_style)
lb_fone2.grid(column=2, row=0, sticky="W", padx=paddingx)
entry_fone2 = Entry(separador7, font=entry_style,width=width_fone)
entry_fone2.grid(column=2, row=1, padx=paddingx)

lb_operadora2 = Label(separador7, text="Operadora", font=lb_style)
lb_operadora2.grid(column=3, row=0, sticky="W", padx=paddingx)
entry_operadora1 = Entry(separador7, font=entry_style, width=width_operadora)
entry_operadora1.grid(column=3, row=1, padx=paddingx)

lb_fone3 = Label(separador7, text="Fone 3", font=lb_style)
lb_fone3.grid(column=4, row=0, sticky="W", padx=paddingx)
entry_fone3 = Entry(separador7, font=entry_style,width=width_fone)
entry_fone3.grid(column=4, row=1, padx=paddingx)

lb_operadora3 = Label(separador7, text="Operadora", font=lb_style)
lb_operadora3.grid(column=5, row=0, sticky="W", padx=paddingx)
entry_operadora3 = Entry(separador7, font=entry_style, width=width_operadora)
entry_operadora3.grid(column=5, row=1, padx=paddingx)


separador8 = ttk.Separator(janela, orient="horizontal")
separador8.pack(fill="x", padx=paddingx, pady=paddingy)

lb_email = Label(separador8, text="Email", font=lb_style)
lb_email.grid(column=0, row=0, sticky="W", padx=paddingx)
entry_email = Entry(separador8, font=entry_style, width=89)
entry_email.grid(column=0, row=1, padx=paddingx)

lb_campos_obrigatorios = Label(janela, text="(*) Campos Obrigatórios")
lb_campos_obrigatorios.pack(fill="x", side=RIGHT,anchor=NW)

separador9 = ttk.Separator(janela, orient="horizontal")
separador9.pack(fill="x",pady=10, padx=10)

grava = Button(separador9, text="GRAVA",font=lb_style)
grava.grid(column=0, row=0,sticky="WS")

cancela = Button(separador9, text="CANCELA",font=lb_style)
cancela.grid(column=1, row=0,sticky="WS")

#retirar
janela.mainloop()