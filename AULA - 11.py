# produtos = {}

# for i in range(1):
#     nome_produto = input('Digite o nome do produto: ')
#     preço_produto = float(input('Digigte o seu preço '))
#     produtos[nome_produto] = preco_produto

#     print('leads')
    
# def soma (a,b):
#     print(a+b)

#     soma2 = lambda a,b: a+b
#     soma(1,2)
#     print(soma2(3,6))

# from functools import reduce 

# numeros = [1, 2, 3, 4, 5]
# soma = reduce(lambda)











# **EXERCÍCIOS:**

# 1 - Crie uma função lambda que retorne o dobro de um número.

# numeros = int(input('Digite o número: '))
# x2 = lambda x: x * 2
# print('O dobro do seu número é: ', x2(numeros))

# 2 - Crie uma função lambda que calcule a soma de dois números.

# numeros = int(input('Digite o número: '))
# numeros_2 = int(input(' Digite o numero: '))
# x_2 = lambda x1 : x1 
# print('A soma do seu número é: ', x_2(numeros+numeros_2))

# 3 - Crie uma função lambda que verifique se um número é par.

# numeros = int(input(' digite um número: '))
# soma =(lambda x: x % 2 == 0)
# if soma (numeros) == True:
#     print(f' o {numeros} é par')
# else:
#     print(f' o {numeros} é impar')

# 4 - Crie uma função lambda que converta uma string em maiúsculas.

# caractere = (input(' Digite os caracteres: '))
# maiusculo = lambda x:x
# print(maiusculo(caractere.upper()))

# 5 - Crie uma função lambda que calcule o produto de três números.

from functools import reduce
numeros = int(input(' Digite o numero: '))
numeros_2 = int(input(' Digite o numero: '))
numeros_3 = int(input(' Digite o numero: '))
somas = [numeros, numeros_2, numeros_3]
produto = reduce(lambda x,y : x * y, somas)
print(produto)
