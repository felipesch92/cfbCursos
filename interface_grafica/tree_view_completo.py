from tkinter import *
from tkinter import ttk


def salvar():
    tv_clientes.insert('', 'end', values=(txt_id.get(), txt_nome.get(), txt_idade.get()))
    app.update()
    nb_clientes.select(0)


def deletar():
    try:
        item_selecionado = tv_clientes.selection()[0]
        tv_clientes.delete(item_selecionado)
    except:
        print('Selecione um registro para deletar.')


def editar():
    try:
        item_selecionado = tv_clientes.selection()[0]
        valores = tv_clientes.item(item_selecionado, 'values')
        print(valores)
    except:
        print('Selecione um registro para editar.')


app = Tk()
app.title('TreeView')


# Variáveis do formulário
txt_id = IntVar()
txt_nome = StringVar()
txt_idade = IntVar()

nb_clientes = ttk.Notebook(app)
nb_clientes.grid(row=0, column=0)

frm_clientes = Frame(nb_clientes)

tv_clientes = ttk.Treeview(frm_clientes, columns=('id', 'nome', 'idade'),
                           show='headings')
tv_clientes.column('id', minwidth=0, width=50)
tv_clientes.column('nome', minwidth=0, width=250)
tv_clientes.column('idade', minwidth=0, width=50)
tv_clientes.heading('id', text='ID')
tv_clientes.heading('nome', text='Nome')
tv_clientes.heading('idade', text='Idade')
tv_clientes.grid(row=0, columnspan=2)

btn_deletar = Button(frm_clientes,
                     text='Deletar',
                     command=deletar)
btn_editar = Button(frm_clientes,
                     text='Editar',
                     command=editar)
btn_deletar.grid(row=1, column=0)
btn_editar.grid(row=1, column=1)
frm_cadastro = Frame(nb_clientes)


Label(frm_cadastro, text='ID: ').grid(row=0, column=0, sticky='e')
Label(frm_cadastro, text='Nome: ').grid(row=1, column=0, sticky='e')
Label(frm_cadastro, text='Idade: ').grid(row=2, column=0, sticky='e')
et_id = Entry(frm_cadastro, textvariable=txt_id).grid(row=0, column=1)
et_nome = Entry(frm_cadastro, textvariable=txt_nome).grid(row=1, column=1)
et_idade = Entry(frm_cadastro, textvariable=txt_idade).grid(row=2, column=1)
btn_salvar = Button(frm_cadastro, text='Salvar', command=salvar)
btn_salvar.grid(row=3, columnspan=2)

nb_clientes.add(frm_clientes, text='Clientes')
nb_clientes.add(frm_cadastro, text='Cadastro')


app.mainloop()
