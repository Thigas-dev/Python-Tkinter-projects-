from tkinter import *
from tkinter import ttk
import random
import string

#cores

c1 ="#3b2061" #roxo
c2 ="#1c1b1c" #preto/cinza
c3 ="#ffffff" #branco

jane = Tk()
jane.title("Gerador de senha")
jane.geometry("800x400")
jane.config(bg=c1)

corp1 = Frame(jane,width=800,height=90,bg=c3)
corp1.grid(row=0, column=0)

nome= Label(corp1, text="Gerador de senha",width=20,height=2,anchor="center",font=("Ivy 26 bold"),bg=c3,fg=c1)
nome.place(x=190,y=0)

corp2 = Frame(jane,width=800,height=330,bg=c1)
corp2.grid(row=1, column=0)

linha= Label(jane, text= '',width=400,height=3,anchor="center",font=("Ivy 3 bold"),bg=c2,fg=c1)
linha.place(x=0,y=90)

#def

def Gerar():
    
    min = string.ascii_lowercase
    mai = string.ascii_uppercase
    num = '123456789'
    simbolos = "[]{}()*;/,_-"

    comb = min
    comb = comb + mai
    comb = comb + num
    comb = comb + simbolos

    compri = 7

    senha = "".join(random.sample(comb, compri))

    resu['text'] = senha


resu = Label(corp2,text="---",width=10,height=1,padx=250,pady=50,relief="flat",anchor="center",font=("Ivy 20 bold"),bg=c3,fg=c2)
resu.place(x=65,y=60)

b= Button(command=Gerar,text="Gerar senha",width=50,height=2, anchor="center",font="Ivy 12 bold", bg=c2,fg=c3)
b.place(x= 150, y= 320 )

jane.mainloop()