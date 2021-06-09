'''
Problema 4
Dado um script com uma lista de nomes, acrescentar entre uma letra e outra um espaço, um “pipe” e outro
espaço.

lista_nomes = ['Ana', 'Ana Maria', 'Pedro', 'Elena', 'Helena', 'Elen']
'''


lista_nomes = ['Ana', 'Ana Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']

# Seu código aqui
for nome in lista_nomes:
    lista = []
    for item in nome:
        lista.append('|'+ item)
    print(''.join(lista)+'|')



