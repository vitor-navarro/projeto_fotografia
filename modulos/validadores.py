from datetime import date

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

    def validador_horario(self,entry,event_caractere_digitado):
        caracteres = entry.get()
#falta apenas validar para que adicione o : automaticamente
        if event_caractere_digitado.keycode == 8:
            return True
        elif len(caracteres) >= 5:
                return False
        elif event_caractere_digitado.char.isdigit():
            return True
        else:
            return False

    def to_uppercase(self, text):
        #no entry crie uma string var e coloque na text variable,
        #depois chame ele com o trace_add exemplo: meu_string_var.trace_add("write", self.to_uppercase)

        text.set(text.get().upper())