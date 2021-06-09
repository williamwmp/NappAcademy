'''
Problema 3
Dado um script com uma lista de nomes, verificar e imprimir na tela todos os nomes compostos ( que
possuem dois nomes).

lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']
lista_nomes = lista_nomes + ['Mário', 'Arnaldo', 'Lucas', 'Maria Vitória']
lista_nomes = lista_nomes + ['Vitor', 'Ana Paula', 'Maria Aparecida']
'''


lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'Elen']
lista_nomes = lista_nomes + ['Mário', 'Arnaldo', 'Lucas', 'Maria Vitória']
lista_nomes = lista_nomes + ['Vitor', 'Ana Paula', 'Maria Aparecida']

# Seu código aqui
for nome  in lista_nomes:
    if ' ' in nome:
        print(nome)