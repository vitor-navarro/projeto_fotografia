import sqlite3

'''banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

cadastro_valor ="10/11/2022"
nome_razao_social = "VITOR LUIZ DOS SANTOS NAVARRO"
id = 4

cursor.execute(f"UPDATE pessoas SET data_cadastro = ?,nome_razao_social=? WHERE id = ?",(cadastro_valor,nome_razao_social, id))
print(cursor.fetchall())
banco.commit()

banco.close()
'''

import tkinter as tk
def on_return(event):
    event.widget.tk_focusNext().focus()

window = tk.Tk()

entry1 = tk.Entry(window)
entry1.pack()
entry1.focus()
entry2 = tk.Entry(window)
entry2.pack()
entry3 = tk.Entry(window)
entry3.pack()
entry4 = tk.Entry(window)
entry4.pack()
entry5 = tk.Entry(window)
entry5.pack()

window.bind("<Return>", on_return)

window.mainloop()




