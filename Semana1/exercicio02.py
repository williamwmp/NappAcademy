lista_nomes = ['Ana', 'Maria', 'José', 'Pedro', 'Elena', 'Helena', 'elen']
vogais = ['A', 'E', 'I', 'O', 'U']

# Seu código aqui
for nome  in lista_nomes:
    if nome[0].upper() in vogais:
        print(nome)