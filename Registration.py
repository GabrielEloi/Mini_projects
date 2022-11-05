from tkinter import *

window = Tk()
window.title('Name and Password')

Label(window, text='LOGIN', width=100).grid(row=0)
Label(window, text='Name:', width=25).place(x=40, y=60)
Label(window, text='Password:', width=25).place(x=40, y=90)

entry_name = Entry(window)
entry_Password = Entry(window)
entry_name.place(x=160, y=60)
entry_Password.place(x=160, y= 90)

button_login = Button(window, text='Login', width=25, command=window.destroy).place(x=158, y= 125)

window.mainloop()
