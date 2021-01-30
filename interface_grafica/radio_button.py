from tkinter import *


def mostrar_esporte():
    ve = vesporte.get()
    if ve == 'f':
        print('Futebol!')
    elif ve == 'v':
        print('Volei!')
    elif ve == 'b':
        print('Basquete!')
    else:
        print('Selecione um esporte!')


def mostrar_cor():
    vc = vcor.get()
    if vc == 'a':
        print('Azul')
        app['bg'] = 'blue'
    elif vc == 'v':
        print('Vermelho')
        app['bg'] = 'red'
    elif vc == 'am':
        print('Amarelo')
        app['bg'] = 'yellow'
    else:
        print('Escolha uma cor')


app = Tk()
app.geometry('500x300')

vesporte = StringVar()
vcor = StringVar()

lbl_esportes = Label(app,
                     text='Esportes')
lbl_esportes.pack()

rb_futebol = Radiobutton(app,
                         text='Futebol',
                         value='f',
                         variable=vesporte)
rb_volei = Radiobutton(app,
                            text='Volei',
                            value='v',
                            variable=vesporte)
rb_basquete = Radiobutton(app,
                            text='Basquete',
                            value='b',
                            variable=vesporte)
btn_esporte = Button(app,
                     text='Selecionar',
                     command=mostrar_esporte)

rb_futebol.pack()
rb_volei.pack()
rb_basquete.pack()
btn_esporte.pack()

lbl_cores = Label(app,
                  text='Cores')
rb_azul = Radiobutton(app,
                      text='Azul',
                      value='a',
                      variable=vcor)
rb_vermelho = Radiobutton(app,
                          text='Vermelho',
                          value='v',
                          variable=vcor)
rb_amarelo = Radiobutton(app,
                         text='Amarelo',
                         value='am',
                         variable=vcor)
btn_cor = Button(app,
                 text='Escolher',
                 command=mostrar_cor)
lbl_cores.pack()
rb_azul.pack()
rb_vermelho.pack()
rb_amarelo.pack()
btn_cor.pack()


app.mainloop()
