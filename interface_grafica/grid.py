from tkinter import *

app = Tk()
app.title('Grid')
app.geometry('500x300')

lb_titulo = Label(app, text='Novo Cliente')
lb_nome = Label(app, text='Nome: ')
lb_idade = Label(app, text='Idade: ')
et_nome = Entry(app)
et_idade = Entry(app)
btn_salvar = Button(app,
                    text='Salvar')

lb_titulo.grid(row=0, columnspan=2, sticky='e')
lb_nome.grid(row=1, column=0)
lb_idade.grid(row=2, column=0)
et_nome.grid(row=1, column=1)
et_idade.grid(row=2, column=1)
btn_salvar.grid(row=3, columnspan=2)

app.mainloop()
