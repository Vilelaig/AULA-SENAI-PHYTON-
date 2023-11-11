#  EXERCÍCIOS 1 

# 1 - Peça ao usuário que insira seu ano de nascimento e calcule sua idade.

# ano = int(input("Insira o seu ano de nascimento: "))
# idade = 2023 - ano
# print(f'Você tem {idade} anos.')

# 2 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.

# import datetime
# data = datetime.datetime.now()
# print(f'data: {data}')
# data_7_dias = data + datetime.timedelta(days=7)
# print(f'data 7 dias; {data_7_dias}')


# 3 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.

# import datetime
# ano = int(input("Insira um ano: "))
# ano_atual = datetime.datetime.now().year
# print(f'O ano atual é {ano_atual}')


# 4 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).

# import datetime
# data = datetime.datetime.now()
# print(f'data: {data}')
# print(f'data: {data: %d/%m/%Y , %H:%M:%S}')


