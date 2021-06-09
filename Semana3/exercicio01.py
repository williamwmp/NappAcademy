import csv


def find_subtring_credit_card(lista, parametro='322'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca a string 'parâmetro' como substring
    do campo 'Cartão de Crédito'.

    Args:
        lista (List): [description]
        parametro (str, optional): Substring a ser encontrada. Padrão '322'.

    Returns:
        List: Lista com os nomes de pessoas que possuam substring
        no cartão de crédito
    """
    pessoa = []
    lista_nomes = []

    for i in lista:
        if len(i[2]) == 16 and parametro in i[2]:
            pessoa.append(i)   
            # print(pessoa[0])
    for registro in pessoa:
        lista_nomes.append(registro)
    return lista_nomes
    


def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o reader e carrega os dados em uma lista retornada.

    Args:
        path (String): Nome do arquivo

    Returns:
        (List): Lista com todos os registros
    """
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = '/home/williampereira/workspace/NappAcademy/Semana3/usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    # print(lista[1][2])
    print(find_subtring_credit_card(lista))
    print(find_subtring_credit_card(lista, '222'))
