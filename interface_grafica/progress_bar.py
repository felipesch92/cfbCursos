from tkinter import *
from tkinter import ttk
from time import sleep


def carregar():
    for x in range(0, 101):
        var_barra.set(x)
        sleep(0.1)
        app.update()


app = Tk()
app.title('ProgressBar')
app.geometry('500x300')

var_barra = DoubleVar()
var_barra.set(0)


pb = ttk.Progressbar(app,
                     variable=var_barra,
                     maximum=100)
pb.place(x=0, y=0, width=500, height=40)
btn_carregar = Button(app,
                      text='Carregar',
                      command=carregar)
btn_carregar.place(x=200, y=50)

app.mainloop()
