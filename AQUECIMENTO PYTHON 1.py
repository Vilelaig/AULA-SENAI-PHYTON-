# Exercício 1
# Faça um programa que leia um número inteiro do usuário e imprima o seu quadrado. Se o usuário digitar um valor não inteiro ou valor negativo, imprima uma mensagem de erro.


# try:
#     number =int(input("Digite o seu número: "))
#     if number < 0:
#         raise ValueError("Digite números positivos")
    
#     else:
#         square = number ** 2
#         print(f' O quadrado de {number} é {square}')
        
# except ZeroDivisionError as e:
#     print(f'Calculo não pode ser menor ou igual a zero')


# Exercício 2
# Faça um programa que leia dois números inteiros do usuário e imprima a sua soma. Se o usuário digitar um número não inteiro, imprima uma mensagem de erro.

# try:
#     numero_1 = int(input("Digite o seu número: "))
#     if numero_1 < 0:
#         raise ValueError ("O primeiro valor tem que ser positivo")
    
#     numero_2 = int(input("Digite o seu número: "))
#     if numero_2 < 0:
#         raise ValueError ("O segundo valor tem que ser positivo")

#     soma = numero_1 + numero_2
#     print(f"A soma de {numero_1} com {numero_2} é {soma}: ")

# except ValueError as e:
#     print(f"{e} !!!")


 
# Exercício 3
# Faça um programa que leia um número inteiro do usuário e imprima o seu fatorial. Se o usuário digitar um número não inteiro ou menor que zero, imprima uma mensagem de erro.


try:
    number = int(input("Digite um número: "))
    if number <= 0:
        raise ValueError ("Digite um número maior que zero")
    else:
       fatorial = 1
       
    for i in range (1,number+1):
        fatorial = fatorial * i
        print(f'{number}! = {fatorial}'. format(number,fatorial))

except ValueError as e:
    print(f"Digite um valor positivo maior que zero {e}")