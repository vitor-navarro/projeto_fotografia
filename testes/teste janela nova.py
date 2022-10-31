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


#retirar
janela.mainloop()