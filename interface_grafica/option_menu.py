from tkinter import *


def mostrar_esporte():
    ve = vesporte.get()
    print(ve)


app = Tk()
app.geometry('500x300')

lista_esportes = ['Futebol', 'Vôlei', 'Basquete']

vesporte = StringVar()
# Valor padrão
vesporte.set(lista_esportes[1])

lbl_esportes = Label(app,
                     text='Esportes')
lbl_esportes.pack()

op_esportes = OptionMenu(app, vesporte, *lista_esportes)
op_esportes.pack()

btn_esporte = Button(app,
                     text='Selecionar',
                     command=mostrar_esporte)
btn_esporte.pack()

app.mainloop()
