from tkinter import *
from tkinter import ttk, messagebox


def mostrar_esporte():
    print(cb_esportes.get())
    messagebox.showinfo('Esporte', cb_esportes.get())


app = Tk()
app.title('Combo Box')
app.geometry('500x300')

lista_esportes = ['Futebol', 'Volei', 'Basquete']

Label(app, text='Esportes').grid(row=0, column=0)

cb_esportes = ttk.Combobox(app,
                           values=lista_esportes)
cb_esportes.set(lista_esportes[0])
cb_esportes.grid(row=0, column=1)

btn_mostra = Button(app,
                    text='Mostrar',
                    command=mostrar_esporte)
btn_mostra.grid(row=1, columnspan=2)

app.mainloop()
