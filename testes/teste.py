'''import sqlite3

banco = sqlite3.connect("../modulos/database.db")

cursor = banco.cursor()

cursor.execute(f"UPDATE pessoas SET status='ATIVO'")

banco.commit()

banco.close()
'''
import re
import tkinter as tk
from tkinter import ttk
from datetime import datetime


def is_valid_date(date_string):
    print(date_string)
    ultimo_caractere = date_string[len(date_string) - 1]

    if re.match(r'^\d{2}/\d{2}/\d{5}$', date_string):
        try:
            datetime.strptime(date_string, '%d/%m/%Y')
            #não retorna nada, se precionar enter vai para o próximo entry
            return False
        except ValueError:
            #retorna no entry de erro ou em popup que a data é inválida
            return False

    elif ultimo_caractere.isdigit():
        return True
    elif ultimo_caractere == "/":
        return True
    '''

'''


root = tk.Tk()
date_entry = ttk.Entry(root, width=10, font=('Arial', 16),validate="key", validatecommand=(root.register(is_valid_date), '%P'))
date_entry.pack()
root.mainloop()





