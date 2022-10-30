from tkinter import *


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

lb_codigo = Label(janela, text="Código", font=lb_style)
lb_codigo.grid(column=0, row=0, sticky="W")

entry_codigo = Entry(janela,borderwidth=0)
entry_codigo.grid(column=0, row=1)


#retirar
janela.mainloop()