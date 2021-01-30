from tkinter import *
import os

app = Tk()
app.title('Photo Image')
app.geometry('500x300')

img_certificado = PhotoImage(file='certificado.png')
l_img = Label(app,
              image=img_certificado)
l_img.grid(row=0, column=0)

app.mainloop()
