from tkinter import *
from tkinter import ttk

app = Tk()
app.title('Abas e Notbook')
app.geometry('500x300')

nb_1 = ttk.Notebook(app)
nb_1.grid(row=0, column=0)

frm_1 = Frame(nb_1)
frm_2 = Frame(nb_1)
nb_1.add(frm_1, text='Clientes')
nb_1.add(frm_2, text='Novo')

Label(frm_1, text='Nome').grid(row=0, column=0)
Label(frm_1, text='Telefone').grid(row=0, column=1)
Label(frm_1, text='Whats').grid(row=0, column=2)
Label(frm_1, text='Planos').grid(row=0, column=3)

Label(frm_2,
      text='Nome: ').grid(row=0, column=0)
txt_nome = Entry(frm_2)
txt_nome.grid(row=0, column=1)
btn_salvar = Button(frm_2,
                    text='Salvar')
btn_salvar.grid(row=1, columnspan=2)

app.mainloop()
