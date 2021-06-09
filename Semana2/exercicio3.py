
from massa_dados import list_spend_money


def spend_by_subname(name):
    for i in list_spend_money:
        if name.lower() in i[0].lower():
            print(f'Nome: {i[0]}, Login: {i[1]}, Genero: {i[2]}, Gasto: {i[3]}')
        else:
            pass


def sum_by_subname(name):
    soma = 0
    for i in list_spend_money:
        if name.lower() in i[0].lower():
            if i[3] == '':
                soma += 0   
            else:
                soma += float(i[3])
        else:
            pass
    return(soma)


if __name__ == "__main__":
    name = 'Pereira'
    spend_by_subname(name)
    print('A soma total é: ')
    print(sum_by_subname(name))