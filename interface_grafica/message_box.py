from tkinter import *
from tkinter import messagebox


def mostrar_msg(tipomsg, msg):
    if tipomsg.lower() == 'i':
        messagebox.showinfo(title='Informação',
                            message=msg)
    elif tipomsg.lower() == 'e':
        messagebox.showerror(title='Erro',
                             message=msg)
    elif tipomsg.lower() == 'w':
        messagebox.showwarning(title='Alerta',
                               message=msg)


def resetar_tb_msg():
    res = messagebox.askyesno('Resetar Mensagem', 'Confirma reset da mensagem? ')
    if res:
        tb_msg.delete(0, END)
        messagebox.showinfo(title='Limpar', message='Mensagem apagada!')


lista_msg = ['Informação', 'Erro', 'Alerta']

app = Tk()
app.geometry('500x300')

vmsg = StringVar()
vnum_cstexto = StringVar()
vnum_cstexto.set('i')
Label(app, text='Tipo de cx(I, E ou W)').pack()
tb_num = Entry(app,
               textvariable=vnum_cstexto)
tb_num.pack()
Label(app, text='Mensagem: ').pack()
tb_msg = Entry(app,
               textvariable=vmsg)
tb_msg.pack()

btn_msg = Button(app,
                 text='Mostrar mensagem',
                 command=lambda: mostrar_msg(vnum_cstexto.get(), vmsg.get()))
btn_msg.pack()

btn_resetar = Button(app,
                     text='Resetar',
                     command=resetar_tb_msg)
btn_resetar.pack()

app.mainloop()
