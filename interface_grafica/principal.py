from tkinter import *


def semComando():
    a = 1


def novo_contato():
    exec(open('novo_contato.py').read())


app = Tk()
app.title('Contatos')
app.geometry('500x300')

# Barra de menus
barra_menus = Menu(app)

# Menu contato
menu_contato = Menu(barra_menus, tearoff=0)
menu_contato.add_command(label='Novo',
                         command=novo_contato)
menu_contato.add_command(label='Pesquisar',
                         command=semComando)
menu_contato.add_command(label='Deletar',
                         command=semComando)
menu_contato.add_separator()
menu_contato.add_command(label='Fechar',
                         command=app.quit)

# Adiciona o menu contato a barra de menus
barra_menus.add_cascade(label='Contatos',
                        menu=menu_contato)

# Menu manutenção
menu_manutencao = Menu(barra_menus, tearoff=0)
menu_manutencao.add_command(label='Banco de Dados',
                 command=semComando)
# Adiciona o menu manutenção a barra de menus
barra_menus.add_cascade(label='Manutenção',
                        menu=menu_manutencao)

# Menu sobre
menu_sobre = Menu(barra_menus, tearoff=0)
menu_sobre.add_command(label='Sobre nós',
               command=semComando)
# Adiciona o menu sobre a barra de menus
barra_menus.add_cascade(label='Sobre',
                        menu=menu_sobre)


app.config(menu=barra_menus)

app.mainloop()
