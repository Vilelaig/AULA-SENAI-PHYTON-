# Exercício 1: Criar um Diretório
# import os

# os.mkdir('Novo_Repositorio')


# # Exercício 2: Entrar em um Diretório

# # AULA 22.py
# # print("Olá, mundo!")

# # Exercício 3: Renomear um Diretório
# import os
# os.rename('C:/Users/aluno/Desktop/AULA 22/Novo_Repositorio', 'Novo_Diretorio.txt')


# # Exercício 4: Remover um Diretório

# import shutil
# shutil.rmtree("C:/Users/aluno/Desktop/AULA 22/Novo_Diretorio.txt")


# # Exercício 5: Listar Arquivos em um Diretório

# import os
# with os.scandir('C:/Users/aluno/Desktop/AULA 22/Novo_Diretorio.txt') as entrada:
#     for arquivo in entrada:
#         if arquivo.is_file():
#             print(f'Arquivo encontrado: {arquivo.name}') 


# # Exercício 6: Copiar Arquivos em um Diretório

# import shutil

# shutil.copytree('Novo' , 'Novo_2')
