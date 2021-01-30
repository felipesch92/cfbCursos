from tkinter import *


def futebol_clicado():
    if vfutebol.get() == 1:
        print('Futebol selecionado')


def volei_clicado():
    if vvolei.get() == 1:
        print('Volei selecionado')


def basquete_clicado():
    if vbasquete.get() == 1:
        print('Basquete selecionado')


app = Tk()
app.title('Check Button')
app.geometry('400x200')

vfutebol = IntVar()
vvolei = IntVar()
vbasquete = IntVar()

frm_1 = Frame(app,
              borderwidth=2,
              relief='solid')
frm_1.grid(row=0, column=0)

cb_futebol = Checkbutton(frm_1,
                         text='Futebol',
                         variable=vfutebol,
                         onvalue=1,
                         offvalue=0,
                         command=futebol_clicado)
cb_volei = Checkbutton(frm_1,
                         text='Volei',
                         variable=vvolei,
                         onvalue=1,
                         offvalue=0,
                         command=volei_clicado)
cb_basquete = Checkbutton(frm_1,
                         text='Basquete',
                         variable=vbasquete,
                         onvalue=1,
                         offvalue=0,
                         command=basquete_clicado)
cb_futebol.grid(row=0, column=0)
cb_volei.grid(row=1, column=0)
cb_basquete.grid(row=2, column=0)

app.mainloop()
