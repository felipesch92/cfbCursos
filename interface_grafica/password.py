from tkinter import *
from tkinter import messagebox


def acessar():
    if vpd.get() == '0000':
        messagebox.showinfo('Login', 'Acesso garantido!')
    else:
        messagebox.showwarning('Login', 'Acesso negado!')
    print(vpd.get())


app = Tk()
app.title('Password')
app.geometry('300x150')

vpd = StringVar()

pd = Entry(app,
           textvariable=vpd,
           show='*')
pd.grid(row=0, column=0)
btn_acessar = Button(app,
                     text='Acessar',
                     command=acessar)
btn_acessar.grid(row=1, column=0)

app.mainloop()
