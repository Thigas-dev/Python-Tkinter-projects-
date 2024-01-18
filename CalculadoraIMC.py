from tkinter import *
from tkinter import ttk

#cores
cor1 ="#3b2061" #roxo
cor2 ="#1c1b1c" #preto/cinza
cor3 ="#ffffff" #branco
cor4 ="#69696b" #cinza
cor5 ="#98999c" #cinza claro

jane =Tk()
jane.title("Calculadora de IMC")
jane.geometry("500x300")
jane.config(bg=cor3)

tela = Frame(jane, width=200, height=100, bg=cor3)
tela.grid(row=0, column=0)

nome= Label(jane, text= 'Calculadora de IMC',width=23,height=1, padx=0,anchor="center",font=("Ivy 16 bold"),bg=cor3,fg=cor1)
nome.place(x=95,y=10)

linha= Label(jane, text= '',width=500,height=1, padx=0,anchor="center",font=("Ivy 3 bold"),bg=cor2,fg=cor1)
linha.place(x=0,y=50)

#DEF ----------
def calcular():

    pesoc = float(peso2.get())
    altura = float(altu2.get())

    imc = pesoc / altura**2

    resultado = imc

    if resultado < 18.4:
       resutexto['text'] = "Seu IMC é classificado como: Magreza"

    elif resultado >= 18.5 and resultado < 24.9:
        resutexto['text'] = "Seu IMC é classificado como: Normal"

    elif resultado >= 25 and resultado < 29.9:
        resutexto['text'] = "Seu IMC é classificado como: Sobrepeso(Obesidade Grau I)"

    elif resultado >= 30 and resultado < 39.9:
        resutexto['text'] = "Seu IMC é classificado como: Obesidade(Obesidade Grau II)"

    else:
        resutexto['text'] = "Seu IMC é classificado como: Obesidade(Obesidade Grau III)"

    resu['text'] = "{:.{}f}".format(resultado, 2)


peso = Label(jane, text="Insira seu peso(KG)",height=1,padx= 0,anchor= "center", font=("Ivy 10 bold"),bg=cor3,fg=cor2)
peso.grid(row=1,column=0, columnspan=1, pady=10,padx=3)
peso2 = Entry(jane, width= 7, font=("Ivy 10 bold"),justify="center",relief=SOLID)
peso2.grid(row=1,column=2,columnspan=1,pady=0,padx=0)

altu = Label(jane, text="Insira sua altura(M)",height=1,padx= 0,anchor= "center", font=("Ivy 10 bold"),bg=cor3,fg=cor2)
altu.grid(row=2,column=0, columnspan=1, pady=0,padx=0)
altu2 = Entry(jane, width= 7, font=("Ivy 10 bold"),justify="center",relief=SOLID)
altu2.grid(row=2,column=2,columnspan=1,pady=10,padx=3)

resu = Label(jane,text="---",width=8,height=1,padx=6,pady=12,relief="flat",anchor="center",font=("Ivy 20 bold"),bg=cor1,fg=cor3)
resu.place(x=300,y=110)

resutexto = Label(jane,text="",width=50,height=1,padx=6,pady=12,relief="flat",anchor="center",font=("Ivy 10 bold"),bg=cor3,fg=cor1)
resutexto.place(x=50,y=190)

b1= Button(jane,command=calcular, text="Calcular",width=50,height=2, padx=0,anchor="center",font=("Ivy 9 bold"),bg=cor1,fg=cor3)
b1.place(x=70,y=245)


jane.mainloop()
