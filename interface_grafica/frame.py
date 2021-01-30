from tkinter import *
from tkinter import messagebox


def mostrar_msg():
    messagebox.showinfo(title='Mensagem',
                        message='A mensagem foi criada!')


app = Tk()
app.geometry('500x300')

vmsg = StringVar()

frm_1 = Frame(app,
              borderwidth=1,
              relief='solid')
frm_1.grid(row=0, column=0, padx=10, pady=10)
frm_2 = Frame(app,
              borderwidth=1,
              relief='raised')
frm_2.grid(row=0, column=1)


Label(frm_1, text='Mensagem: ').grid(row=0, column=0)
txt_msg = Entry(frm_1, textvariable=vmsg)
txt_msg.grid(row=0, column=1)
btn_msg = Button(frm_1,
                 text='Mostrar mensagem',
                 command=mostrar_msg)
btn_msg.grid(row=1, columnspan=2)

lbl_1 = Label(frm_2, text='Este é um label dentro do frame 2').grid(row=0, column=0)
lbl_2 = Label(frm_2, text='Este é outro label dentro do frame 2').grid(row=1, column=0)

app.mainloop()
