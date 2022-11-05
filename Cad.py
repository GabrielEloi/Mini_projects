import tkinter
from tkinter import *

Window = Tk()

Label(Window, text='Usuario').grid(row=0)
Label(Window, text='Senha').grid(row=1)
Label(Window, text='Curso desejado').grid(row=3)

Usuario = Entry(Window).grid(row=0, column=1)

Senha = Entry(Window).grid(row=1, column=1)

r1 =Radiobutton(Window, text='Programação', value=1).grid(row=4, column=0, sticky=W)
r2 = Radiobutton(Window, text='Criativo', value=2).grid(row=5, column=0, sticky=W)
r3 = Radiobutton(Window, text='Fotografia',value=3).grid(row=6, column=0, sticky=W)

button = tkinter.Button(Window, text= 'Cadastrar').grid(row=7, column=1)
button2 = tkinter.Button(Window, text='Fechar', command=Window.destroy).grid(row=7, column=0)


mainloop()