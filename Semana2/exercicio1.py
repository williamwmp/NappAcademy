from massa_dados import list_spend_money


def spend_by_login(login):
    for i in list_spend_money:
        if i[1] == login:
            print(f'Nome: {i[0]}, Login: {i[1]}, Genero: {i[2]}, Gasto: {i[3]}')
        else:
            pass


def sum_by_login(login):
    soma = 0
    for i in list_spend_money:
        if i[1] == login:
            if i[3] == '':
                soma += 0   
            else:
                soma += float(i[3])
        else:
            pass
    return(soma)


if __name__ == "__main__":
    login = 'william.pereira'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))

