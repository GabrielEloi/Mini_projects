from tkinter import *

def limpar():
    visor.delete(0,END)

def inserir(valor):
    visor.insert(END, valor)

def calcular():
    texto_visor = visor.get()
    resultado = eval(texto_visor)
    visor.delete(0, END)
    visor.insert(0, str(resultado))

janelaPrincipal = Tk()
janelaPrincipal.title("Calculadora")


#criar um visor para digitar os números
visor = Entry (janelaPrincipal, font= "Arial 20 bold", bg="#F0FFFF", fg="DodgerBlue", width=19)
visor.pack()

#criar o quadro dos botões
panel = Frame(janelaPrincipal)

#criar os botões
botao_0 = Button(panel, bg="Black", bd=0, text="0", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("0"))
botao_igual = Button(panel, bg="Black", bd=0, text="=", font= "Arial 16 bold", fg="Silver", width=5, height=3, command=calcular)
botao_C = Button(panel, bg="Black", bd=0, text="C", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= limpar)
botao_menos = Button(panel, bg="Black", bd=0, text="-", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("-"))
botao_1 = Button(panel, bg="Black", bd=0, text="1", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("1"))
botao_2 = Button(panel, bg="Black", bd=0, text="2", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("2"))
botao_3 = Button(panel, bg="Black", bd=0, text="3", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("3"))
botao_soma = Button(panel, bg="Black", bd=0, text="+ ", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir(" +"))
botao_4 = Button(panel, bg="Black", bd=0, text="4", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("4"))
botao_5 = Button(panel, bg="Black", bd=0, text="5", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("5"))
botao_6 = Button(panel, bg="Black", bd=0, text="6", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("6"))
botao_multi = Button(panel, bg="Black", bd=0, text="*", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("*"))
botao_7 = Button(panel, bg="Black", bd=0, text="7", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("7"))
botao_8 = Button(panel, bg="Black", bd=0, text="8", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("8"))
botao_9 = Button(panel, bg="Black", bd=0, text="9", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("9"))
botao_divisao = Button(panel, bg="Black", bd=0, text="/", font= "Arial 16 bold", fg="Silver", width=5, height=3, command= lambda: inserir("/"))



panel.pack()

#primeira linha
botao_7.grid(row=0, column=0)
botao_8.grid(row=0, column=1)
botao_9.grid(row=0, column=2)
botao_divisao.grid(row=0, column=3)

#segunda linha
botao_4.grid(row=1, column=0)
botao_5.grid(row=1, column=1)
botao_6.grid(row=1, column=2)
botao_multi.grid(row=1, column=3)

#terceira linha
botao_1.grid(row=2, column=0)
botao_2.grid(row=2, column=1)
botao_3.grid(row=2, column=2)
botao_soma.grid(row=2, column=3)

#quarta linha
botao_0.grid(row=3, column=0)
botao_igual.grid(row=3, column=2)
botao_C.grid(row=3, column=1)
botao_menos.grid(row=3, column=3)



janelaPrincipal.mainloop()