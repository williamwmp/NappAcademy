import re
'''
Dado um script com uma lista de frases, imprimir na tela apenas os verbos no gerúndio ( sufixo ando, endo,
indo).
'''
lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

buscar = ['ando', 'endo','indo']

# Seu código aqui
for frase in lista_frases:
    # print(frase)
    for palavra in frase.split(" "):
        # print(palavra)
        for i in buscar:
            if palavra.endswith(i):
                print(palavra)

