import tkinter as tk



calc = tk.Tk()
calc.title ("1_janela")
calc.resizable(width=False , height=False)
calc.geometry("500x600")
calc.config(bg = "#454545")


calculadora = tk.Entry (calc, width=50)
calculadora.place (x=100 , y=25)

bt1 = tk.Button(calc, text = "1" , width = 10, height = 3)
bt1.place(x = 50, y = 150)


bt2 = tk.Button(calc, text = "2" , width = 10, height = 3)
bt2.place(x = 150, y=150)

bt3 = tk.Button(calc, text = "3" , width = 10, height = 3)
bt3.place(x = 250, y = 150)

bt4 = tk.Button(calc, text = "4" , width = 10, height = 3)
bt4.place(x = 50, y = 225)

bt5 = tk.Button(calc, text = "5" , width = 10, height = 3)
bt5.place(x = 150, y = 225)

bt6 = tk.Button(calc, text = "6" , width = 10, height = 3)
bt6.place(x = 250, y = 225)

bt7 = tk.Button(calc, text = "7" , width = 10, height = 3)
bt7.place(x = 50, y = 300)

bt8 = tk.Button(calc, text = "8" , width = 10, height = 3)
bt8.place(x = 150, y = 300)

bt9 = tk.Button(calc, text = "9" , width = 10, height = 3)
bt9.place(x = 250, y = 300)

bt0 = tk.Button(calc, text = "0" , width = 10, height = 3)
bt0.place(x = 150, y = 375)


calc.mainloop()

btIGUAL = tk.Button(calc, text = "=" , relief = FLAT, width = 10, height = 3)
btIGUAL.place(x = 250, y = 375)

btDIV = tk.Button(calc, text = "/" , relief = FLAT, width = 10, height = 3)
btDIV.place(x = 350, y = 150)

btMULT = tk.Button(calc, text = "x" , relief = FLAT, width = 10, height = 3)
btMULT.place(x = 350, y = 225)

btSOMA = tk.Button(calc, text = "+" , relief = FLAT, width = 10, height = 3)
btSOMA.place(x = 350, y = 300)

btSUB = tk.Button(calc, text = "-" , relief = FLAT, width = 10, height = 3)
btSUB.place(x = 350, y = 375)



def somaaa():
    n1 = int(entrada1.get())
    n2 = int(entrada2.get())
    resul1 = n1 + n2
    resul1_label.config(text = f'\nResultado da soma: {resul1}', bg= "white")
    
def sub():
    n1 = int(entrada1.get())
    n2 = int(entrada2.get())
    resul2 = n1 - n2
    resul2_label.config(text = f'\nResultado da subtração: {resul2}', bg= "white")

def mult():
    n1 = int(entrada1.get())
    n2 = int(entrada2.get())
    resul3 = n1 * n2
    resul3_label.config(text = f'\nResultado da multplicação: {resul3}', bg= "white")

def div():
    n1 = int(entrada1.get())
    n2 = int(entrada2.get())
    resul4 = n1 / n2
    resul4_label.config(text = f'\nResultado da divisão: {resul4}', bg= "white")

