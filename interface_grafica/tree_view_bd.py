from tkinter import *
from tkinter import ttk
import sqlite3

def buscar_dados():
    conn = sqlite3.connect('banco_dados.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cliente ORDER BY nome')
    res = c.fetchall()
    return res


app = Tk()
app.title('TreeView')

lista_clientes = [['0', 'Felipe', '51-99199-9899', 'felipe.jhe27312@gmail.com', 'Fixo, Pré, Pós'],
                  ['1', 'Tamara', '30', 'tamarasmo232@gmail.com', 'Fixo, Pós']]

tv_clientes = ttk.Treeview(app,
                           columns=('id', 'nome', 'telefone', 'email', 'plano'),
                           show='headings')
#Cabeçalho da planilha
tv_clientes.column('id', minwidth=0, width=25)
tv_clientes.column('nome', minwidth=0, width=250)
tv_clientes.column('telefone', minwidth=0, width=120)
tv_clientes.column('email', minwidth=0, width=250)
tv_clientes.column('plano', minwidth=0, width=200)
tv_clientes.heading('id', text='ID')
tv_clientes.heading('nome', text='Nome')
tv_clientes.heading('telefone', text='Telefone')
tv_clientes.heading('email', text='E-mail')
tv_clientes.heading('plano', text='Plano(s)')
tv_clientes.grid(row=0, column=0)

for l in lista_clientes:
    tv_clientes.insert('', 'end', values=(l[0], l[1], l[2], l[3], l[4]))

for l in buscar_dados():
    tv_clientes.insert('', 'end', values=(l[0], l[1], l[2], l[3], l[4]))
    print(l)

app.mainloop()
