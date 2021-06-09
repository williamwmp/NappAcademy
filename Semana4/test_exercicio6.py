from exercicio06 import calculo_porcentagem_entre_0_e_1

def test_1():
    result = calculo_porcentagem_entre_0_e_1(100, 0)
    return result


def test_2():
    result = calculo_porcentagem_entre_0_e_1(100, 0.25)
    return result

def test_3():
    result = calculo_porcentagem_entre_0_e_1(100, 0.50)
    return result

def test_4():
    result = calculo_porcentagem_entre_0_e_1(100, 0.75)
    return result

def test_5():
    result = calculo_porcentagem_entre_0_e_1(100, 1)
    return result

print(test_3())