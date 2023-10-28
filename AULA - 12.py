# 4: Crie um conjunto chamado "frutas" com as seguintes frutas: 
# maçã, banana, laranja, pêra e abacaxi. Em seguida, imprima o número de 
# elementos no conjunto.

# frutas = {maça, banana, laranja, pera, abacaxi}
# elementos = len(frutas)
# print(elementos)


# 5: Crie dois conjuntos, "conjunto1" e "conjunto2", 
# com alguns números inteiros. 
# Imprima a união desses dois conjuntos

# conjunto1 = {1,2,3,4,5}
# conjunto2 = {6,7,8,9,10}
# print(conjunto1.union(conjunto2))

# 6: Dado o conjunto "cores" com cores diferentes, remova a cor 
# "vermelho" do conjunto.

# cores = {'vermelho', 'amarelo', 'azul'}
# cores.remove('vermelho')
# print(cores)

# 7: Crie um conjunto chamado "numeros" com os números de 1 a 10. 
# Em seguida, crie um novo conjunto chamado "pares" 
# contendo os números pares do conjunto "numeros".

# numeros = {1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10}
# pares = list(filter(lambda x : x % 2 ==0, numeros ))
# print(pares)

alunos_aprovados ={'igor' , 'jotape' , 'pompeu' , 'gustavo' , 'zé'}
todos_alunos = {'igor' , 'jotape' , 'pompeu' , 'gustavo' , 'zé' , 'samuel' , 'artur' , ' gui'}
sit = todos_alunos.difference(alunos_aprovados)
print('Os alunos aprovados são' , (sit))