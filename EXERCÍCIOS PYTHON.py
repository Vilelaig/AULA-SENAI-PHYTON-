# Exercício 1: Lidando com NameError

# # Exercício 1: Lidando com NameError
# # O código a seguir tenta calcular a média de uma lista de números, mas há um erro de NameError.
# # Sua tarefa é corrigir o código utilizando try-except para lidar com o erro.
# # Certifique-se de definir a lista de números corretamente dentro do bloco try.

# try:

#     lista_numeros =[1,2,3,4,5]

#     soma = sum(lista_numeros)
#     media = soma / len(lista_numeros)
#     print("A média é:", media)

# except NameError:
#     print("A lista de números não está definida")

                
# Exercício 2: Lidando com ValueError

# Exercício 2: Lidando com ValueError
# O código a seguir solicita ao usuário um número inteiro, mas pode gerar um ValueError se o usuário inserir uma string.
# Sua tarefa é corrigir o código utilizando try-except para lidar com o erro de ValueError.
# Informe ao usuário sobre o erro e peça para digitar um número inteiro válido.

# try:
    
#     numero = int(input("Digite um número inteiro: "))
#     print("O número digitado é:", numero)

#     if numero < 0:
#         raise ValueError

# except ValueError:
#     print("ERROR-Digite um valor inteiro")


                    
# Exercício 3: Lidando com AttributeError

# # Exercício 3: Lidando com AttributeError
# # O código abaixo tenta acessar um atributo 'comprimento' de uma string, o que causará um AttributeError.
# # Sua tarefa é corrigir o código utilizando try-except para lidar com o erro.
# # Informe ao usuário que o atributo não existe para essa string.

# try:

#     minha_string = "Olá, mundo!"
#     comprimento = minha_string.comprimento
#     print("O comprimento da string é:", minha_string)

#     if minha_string = comprimento:


# except AttributeError:
#     print("O atributo 'comprimento' não existe para essa string.")

# except AttributeError:
#     print("Erro: O atributo 'comprimento' não existe para esta string.")
# else:

#     print("O comprimento da string é:", comprimento)               



# Exercício 4: Lidando com KeyError

# # Exercício 5: Lidando com KeyError
# # O código a seguir tenta acessar uma chave inexistente em um dicionário.
# # Sua tarefa é corrigir o código utilizando try-except para lidar com o erro de KeyError.
# # Informe ao usuário sobre a chave inexistente no dicionário.

# try:

#     meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
#     valor = meu_dicionario['d']
#     print("O valor é:", valor)



                                   
# Exercício 5: Lidando com SyntaxError

# # Exercício 6: Lidando com SyntaxError
# # O código abaixo possui um erro de sintaxe que resultará em SyntaxError.
# # Sua tarefa é corrigir o código utilizando try-except para capturar o erro de sintaxe.
# # Informe ao usuário sobre o problema de sintaxe no código.

try:

    for i in range(5+1):
        print(i)

except SyntaxError:
      print("Erro de sintaxe")

                    
# Exercício 6: Lidando com IndexError

# # Exercício 4: Lidando com IndexError
# # O código a seguir tenta acessar um índice que não existe em uma lista.
# # Sua tarefa é corrigir o código utilizando try-except para lidar com o erro de IndexError.
# # Informe ao usuário que o índice está fora do intervalo da lista.

# minha_lista = [1, 2, 3, 4, 5]
# elemento = minha_lista[10]
# print("O elemento é:", elemento)