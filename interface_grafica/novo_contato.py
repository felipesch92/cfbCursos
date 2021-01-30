from tkinter import *
import banco


def salvar_dados():
    if txt_nome.get() != '':
        vnome = txt_nome.get()
        vtelefone = txt_telefone.get()
        vemail = txt_email.get()
        vobs = txt_obs.get()
        vquery = f'INSERT INTO cliente (nome, telefone, email, obs) VALUES ("{vnome}", "{vtelefone}", "{vemail}", "{vobs}")'
        banco.dml(vquery)
        txt_nome.delete(0, END)
        txt_telefone.delete(0, END)
        txt_email.delete(0, END)
        txt_obs.delete(0, END)
        print('Dados armazenados.')
    else:
        print('ERRO')


app = Tk()
app.title('Novo Contato')
app.geometry('300x200')

lbl_nome = Label(app,
             text='Nome: ')
lbl_telefone = Label(app,
             text='Telefone: ')
lbl_email = Label(app,
                  text='E-mail: ')
lbl_obs = Label(app,
                text='Obs.:')
txt_nome = Entry(app)
txt_telefone = Entry(app)
txt_email = Entry(app)
txt_obs = Entry(app)

btn_salvar = Button(app,
                    text='Salvar',
                    command=salvar_dados)

lbl_nome.grid(row=0, column=0)
txt_nome.grid(row=0, column=1)
lbl_telefone.grid(row=1, column=0)
txt_telefone.grid(row=1, column=1)
lbl_email.grid(row=2, column=0)
txt_email.grid(row=2, column=1)
lbl_obs.grid(row=3, column=0)
txt_obs.grid(row=3, column=1)
btn_salvar.grid(row=8, columnspan=2)


app.mainloop()
