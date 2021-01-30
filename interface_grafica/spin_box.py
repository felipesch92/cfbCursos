from tkinter import *


def mostrar():
    print(sb_numeros.get())


app = Tk()
app.title('Spin Box')
app.geometry('300x200')

#sb_numeros = Spinbox(app,
#                     from_=0,
#                     to_=10)
sb_numeros = Spinbox(app,
                     values=('Volei', 'Futebol', 'Basquete', 'Football'))
btn_mostrar = Button(app,
                     text='Mostrar',
                     command=mostrar)

sb_numeros.grid(row=0, column=0)
btn_mostrar.grid(row=1, column=0)

app.mainloop()
