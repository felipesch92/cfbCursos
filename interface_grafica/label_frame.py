from tkinter import *

app = Tk()
app.title('Label Frame')
app.geometry('500x300')

frame_1 = LabelFrame(app,
                     text='Frame 01',
                     borderwidth=1,
                     relief='solid')
frame_2 = LabelFrame(app,
                     text='Frame 02',
                     borderwidth=1,
                     relief='raised')
frame_1.grid(row=0, column=0)
frame_2.grid(row=0, column=1)

lbl1 = Label(frame_1, text='Label do frame 01').pack()
lbl2 = Label(frame_2, text='Label do frame 02').pack()

app.mainloop()
