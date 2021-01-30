from tkinter import *


def selecionar_esporte():
    print(lb_esportes.get(ACTIVE))
    vres.set(lb_esportes.get(ACTIVE))


def adicionar_esporte():
    lb_esportes.insert(END, vtxt_esporte.get())
    vtxt_esporte.set('')


app = Tk()
app.title('List Box')
app.geometry('500x300')

lista_esportes = ['Futebol', 'Volei', 'Basquete']
vres = StringVar()
vtxt_esporte = StringVar()

lb_esportes = Listbox(app)
for esporte in lista_esportes:
    lb_esportes.insert(END, esporte)
for x in range(0, 10):
    lb_esportes.insert(END, x)

btn_selecionar = Button(app,
                        text='Selecionar',
                        command=selecionar_esporte)

lbl_res = Label(app,
                textvariable=vres)

lb_esportes.grid(row=0, column=0)
btn_selecionar.grid(row=1, column=0)
lbl_res.grid(row=2, column=0)

frame_adicionar = LabelFrame(app,
                             text='Adicionar Esporte')
lbl_esporte = Label(frame_adicionar,
                    text='Esporte: ')
txt_esporte = Entry(frame_adicionar,
                    textvariable=vtxt_esporte)
btn_adicionar = Button(frame_adicionar,
                       text='Adicionar',
                       command=adicionar_esporte)

lbl_esporte.grid(row=0, column=0)
txt_esporte.grid(row=0, column=1)
btn_adicionar.grid(row=1, columnspan=2)
frame_adicionar.grid(row=0, column=1)

app.mainloop()
