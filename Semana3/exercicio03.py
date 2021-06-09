import csv


def find_born_in(lista, birth_year='1992'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca os clientes nascidos em 'birth_year'.

    Args:
        lista (List): Lista de tuplas
        birth_year (str, optional): Ano de nascimento . Defaults to '1996'.

    Returns:
        List: Lista com os nomes de pessoas que nasceram no ano informado.
    """
    lista_nomes = list()
    for pessoa in lista:
        if len(pessoa[4]) == 10 and pessoa[4].startswith(birth_year):
            lista_nomes.append(pessoa)
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
    print(find_born_in(lista))
    print(find_born_in(lista, '1982'))
