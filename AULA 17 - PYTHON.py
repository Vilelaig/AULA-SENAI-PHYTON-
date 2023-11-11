# 1 - Crie uma classe chamada Cachorro com um atributo nome e um método 
# latir que imprima "Woof!" quando chamado. 
# Em seguida, crie um objeto da 
# classe Cachorro e chame o método latir.

# class cachorro:
#   def __init__(self, nome):
#     self.nome = nome
    
#   def latir(self):
#     print("AUAU")
    
# cao_1 = cachorro("venha aqui vagabadundo")
# cao_1.latir()

# 2 Crie uma classe chamada Retangulo com atributos largura e 
# altura. Adicione um método chamado calcular_area que retorna a área do retângulo.

# class retangulo:
#   def __init__(self, largura, altura):
#     self.largura = largura
#     self.altura = altura
#   def calcular_area(self):
#     return self.largura * self.altura
    
# retangulo_1 = retangulo(20, 10)
# print(retangulo_1.calcular_area())
# print(retangulo_1.altura)
# print(retangulo_1.largura)


# 3: Crie uma classe chamada Carro com um atributo chamado velocidade 
# (inicialmente 0). Em seguida, adicione um método chamado acelerar que aumenta a
# velocidade em 5 unidades a cada vez que é chamado.

# class carro:
#   def __init__(self, velocidade):
#     self.velocidade = velocidade
    
#   def acelerar(self):
#     self.velocidade += 5
    
# carro_1 = carro(0)
 
# print(carro_1.velocidade)
# carro_1.acelerar()
# print(carro_1.velocidade)
# carro_1.acelerar()
# print(carro_1.velocidade)
# carro_1.acelerar()
# print(carro_1.velocidade)
# carro_1.acelerar()
# print(carro_1.velocidade)
# carro_1.acelerar()
# print(carro_1.velocidade)

# 4 - Crie uma classe chamada Gato que herda da classe Cachorro do exercício anterior. 
#  O método latir da classe Cachorro deve ser substituído por um método miar na classe 
# Gato que imprime "Miau!".

# class cachorro:
#   def __init__(self, nome):
#     self.nome = nome
    
#   def latir(self):
#     print("AUAU")
    
# class gato(cachorro):
#   def miar(self):
#     print("Miau")
    
# gato_1 = gato("Venha aqui seu safado")
# gato_1.miar()

# Exercício 4: Crie uma classe chamada Conta_bancaria com um atributo saldo inicializado com 0. Em seguida, crie métodos deposito e saque que atualizem o saldo. Crie um objeto da classe ContaBancaria, faça um depósito e um saque, e imprima o saldo resultante.

# class conta_bancaria:
#   def __init__(self, saldo):
#     self.saldo = saldo
    
#   def deposito(self, valor):
#     self.saldo += valor
    
#   def saque(self, valor):
#     self.saldo -= valor
    
# conta_1 = conta_bancaria(0)
# conta_1.deposito(500)
# conta_1.saque(520)
# print(conta_1.saldo)