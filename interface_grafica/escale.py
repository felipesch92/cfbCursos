from tkinter import *


def mostrar_scale():
    print(lbl_scale.get())


def definir_scale():
    lbl_scale.set(valor_escala.get())


app = Tk()
app.title('Scale')
app.geometry('500x300')

valor_escala = IntVar()

lb_valor = Label(app,
                 text='Valor: ')
lb_valor.grid(row=0, column=0)
txt_valor = Entry(app,
                  textvariable=valor_escala)
txt_valor.grid(row=0, column=1)

btn_definir = Button(app,
                     text='Definir',
                     command=definir_scale)
btn_definir.grid(row=1, columnspan=2)

lbl_scale = Scale(app,
                  from_=0,
                  to_=50,
                  orient=HORIZONTAL)
lbl_scale.set(20)
lbl_scale.grid(row=2, column=0)

btn_mostrar = Button(app,
                     text='Mostrar',
                     command=mostrar_scale)
btn_mostrar.grid(row=3, column=0)


app.mainloop()
