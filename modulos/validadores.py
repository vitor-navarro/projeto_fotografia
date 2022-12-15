from datetime import date
import re

from tkinter import END
class Validadores:

    def validador_entry_apenas_numeros(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def validador_data(self, event,entry):
        print(event)
        print(entry.get())
        caractere_recebido = event.char
        if caractere_recebido == "/":
            return True
        elif caractere_recebido.isdigit():
            return True
        try:
            day, month, year = entry.get().split("/")
            date(int(year), int(month), int(day))
            return True
        except ValueError:
            return False

    def validador_horario(self,entry,event_caractere_digitado,set_entry_horario_posicao,set_entry_horario_text):
        caracteres = entry.get()

        if event_caractere_digitado.keycode == 8:
            return True
        elif len(caracteres) >= 5:
            return False
        elif event_caractere_digitado.char == ":":
            if caracteres.count(":") == 1:
                return False
            else:
                return True
        elif event_caractere_digitado.char.isdigit():
            return True
        else:
            return False
    def valida_formato_hora(self, event, entry_get, lb_erro):
        valor_entry = entry_get()
        regex = r"\d\d:\d\d"
        resultado = re.match(regex, valor_entry)
        if resultado == None:
            lb_erro["text"] = "O horário deve estar no formato HH:MM"
            return
        else:
            valor_entry_split = valor_entry.split(":")
            if int(valor_entry_split[0]) <= 23 and int(valor_entry_split[1]) <= 59:
                lb_erro["text"] = ""
                pass
            else:
                lb_erro["text"] = "Horário incorreto"

    def to_uppercase(self, text):
        #no entry crie uma string var e coloque na text variable,
        #depois chame ele com o trace_add exemplo: meu_string_var.trace_add("write", self.to_uppercase)

        text.set(text.get().upper())