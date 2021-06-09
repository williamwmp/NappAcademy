from massa_dados import list_spend_money


def spend_by_gender(gender):
    for i in list_spend_money:
        if i[2] == gender:
            print(f'Nome: {i[0]}, Login: {i[1]}, Genero: {i[2]}, Gasto: {i[3]}')
        else:
            pass


def sum_by_gender(gender):
    soma = 0
    for i in list_spend_money:
        if i[2] == gender:
            if i[3] == '':
                soma += 0   
            else:
                soma += float(i[3])
        else:
            pass
    return(soma)


if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(sum_by_gender(gender))