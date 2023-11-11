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
# saldo = float(input("Digite o saldo inicial: "))
# saque = float(input("Digite o valor do saque: "))
# deposito = float(input("Digite o valor do deposito: "))


# saldo_final = saldo + saque - deposito
# print(saldo_final)