numero_1 = float (input("Digite um número: "))
numero_2 = float (input("Digite um número: "))
operator = input("qual a operação que deseja fazer: ")

def calculadora():
   if operator == "+":
    print('a soma dos numeros são ' , numero_1+numero_2)
   elif operator == "-":
    print ('a subtração dos numeros são ' , numero_1-numero_2 )
   elif operator == "*":
     print ('a multiplação dos numeros são ' , numero_1*numero_2)
   elif operator == "/":
     print ('a divisão dos numeros são', numero_1/numero_2 )
   else:
     print( "Digite um operador válido")
calculadora()
 

2