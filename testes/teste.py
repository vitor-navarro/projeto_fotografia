from tkinter import *
from functools import partial

janela = Tk()

label = Label(janela, text="Filtros")
label.grid(column=0, row=0)

botao = Button(janela, text="Clique em min")
botao.grid(column=3, row=0)


janela.mainloop()