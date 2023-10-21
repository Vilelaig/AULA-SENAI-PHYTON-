sinonimos_palavras={
'vacilão':'babacão',
'pobre':'duro',
'feio':'horrivel',
'belo':'lindo',
}

palavras = input('Digite a palavra: ')
if palavras in sinonimos_palavras:
    print(sinonimos_palavras[palavras])
else:
    print(f'A palavra {palavras} não existe!')
