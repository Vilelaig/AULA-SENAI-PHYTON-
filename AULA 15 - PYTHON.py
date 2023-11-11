# linha1 = "Esta é a primeira linha."
# linha2 = "Esta é a segunda linha."
# resultado = f"{linha1}\n{linha2}"
# print(resultado)

# CALCULO DE RAIZ

# import math
# print(math.sqrt(144))

# ALEATORIEDADE

# import random
# print(random.randint(1, 6))

# DIRETORIO DE TRABALHO 

# import os
# print(os.getcwd())

# DATA ATUAL

# from datetime import datetime
# data_atual = datetime.now()
# print(data_atual)

# JSON 

# import json
# dados = '{"nome": "João","idade": 30}'
# objeto = json.loads(dados)
# print(objeto["nome"])



# EXERCICIOS 

# Exercício 1:
# Calcule a raiz quadrada de um número inteiro inserido 
# pelo usuário usando o módulo math

# import math 
# numero = int(input("Digite um numero: "))
# raiz = math.sqrt(numero)
# print("Aqui está a raiz do seu numero" , raiz)

# Exercício 2:
# Calcule o valor absoluto de um número decimal inserido 
# pelo usuário usando o módulo math

# import math 
# numero = float(input("Digite seu numero decimal: "))
# valor_absoluto = math.fabs(numero)
# print("O valor absoluto do seu numero decimal é: ", valor_absoluto)

# Exercício 3:
# Arredonde um número decimal inserido pelo usuário para o 
# inteiro mais próximo usando o módulo math

# import math
# numero = float(input("Digite um numero decimal: "))
# numero_arredondado = math.ceil(numero)
# print("O numero arredondado é: " , numero_arredondado)

# Exercício 4:
# Calcule o seno de um ângulo em graus inserido pelo usuário 
# usando o módulo math.

# import math
# angulo = float(input("Digite um angulo em graus: "))
# seno = math.sin(angulo)
# print("O seno do angulo é: " , seno)

# `DESAFIO:`

# `CRIE UM MÓDULO QUE SEJA CAPAZ DE FAZER A OPERAÇÃO DE UM BANCO`

# `A PRINCIPIO APENAS SAQUES E DEPOSITO`

# import math
# import random 
# number = random.randint(1000,10000)
# random.seed(2)
# print("O valor do seu saldo é de: " , (number))

# saque_deposito = float(input("Digite o valor do seu saque ou deposito: "))

# saldo_final = + saque - deposito
# print(saldo_final)


# def __init__(self, saldo_inicial=0):
#         self.saldo = saldo_inicial

# def depositar(self, valor):
#         self.saldo += valor
#         print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

# def sacar(self, valor):
#         if valor > self.saldo:
#             print('Saldo insuficiente. Operação de saque não realizada.')
#         else:
#             self.saldo -= valor
#             print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}'

# DESAFIO CORRIGIDO 


def menu():
    print(''' 
          
        1 - para saque
        2 - para deposito
        3 - Verificar         
          
          
          
          ''')


def deposito(a,b):
    print(a+b)



def saque(a,b):
    print(a-b)


menu()
value = 100
def operation():
   
    choose = input('Digite a operação:')
    
    if choose == '1':
       meu_saque= float (input('digite o valor: '))
       print('Valor em conta R$')
       saque(value,meu_saque)
    elif choose == '2':
       meu_deposito= float (input('digite o valor: '))
       print('Valor em conta R$')
       deposito(value, meu_deposito)
    else: 
        print('Escolha uma opção valida')
        operation()          


operation()

def loop():
    choose2 = input('Deseja continuar? S/N')
    print(choose2)
    while choose2 == 'S': 
          operation()       
        

loop()

