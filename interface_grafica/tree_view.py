from tkinter import *
from tkinter import ttk

app = Tk()
app.title('TreeView')
app.geometry('600x300')

lista_clientes = [['0', 'Felipe', '29'],
                  ['1', 'Tamara', '30'],
                  ['2', 'Dolores', '67'],
                  ['3', 'Fernando', '37']]

tv_clientes = ttk.Treeview(app,
                           columns=('id', 'nome', 'idade'),
                           show='headings')
tv_clientes.column('id', minwidth=0, width=50)
tv_clientes.column('nome', minwidth=0, width=250)
tv_clientes.column('idade', minwidth=0, width=50)
tv_clientes.heading('id', text='ID')
tv_clientes.heading('nome', text='Nome')
tv_clientes.heading('idade', text='Idade')
tv_clientes.grid(row=0, column=0)

for l in lista_clientes:
    tv_clientes.insert('', 'end', values=(l[0], l[1], l[2]))

app.mainloop()
