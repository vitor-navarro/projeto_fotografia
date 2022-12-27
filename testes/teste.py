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


window = tk.Tk()

saldo_atual = tk.Label(window, text="0.00", padx=10, pady=10, borderwidth=2, relief="groove", font=("Helvetica", 20))
a_pagar = tk.Label(window, text="0.00", padx=10, pady=10, borderwidth=2, relief="groove", font=("Helvetica", 20))
a_receber = tk.Label(window, text="0.00", padx=10, pady=10, borderwidth=2, relief="groove", font=("Helvetica", 20))
saldo_projetado = tk.Label(window, text="0.00", padx=10, pady=10, borderwidth=2, relief="groove", font=("Helvetica", 20))

saldo_atual.grid(row=0, column=0)
a_pagar.grid(row=0, column=1)
a_receber.grid(row=0, column=2)
saldo_projetado.grid(row=0, column=3)

window.mainloop()

window.mainloop()



