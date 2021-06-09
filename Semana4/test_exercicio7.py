from exercicio07 import calculo_porcentagem_entre_0_e_100

def test_1():
    result = calculo_porcentagem_entre_0_e_100(100, 0)
    return result
 
def test_2():
    result = calculo_porcentagem_entre_0_e_100(100, 25)
    return result

def test_3():
    result = calculo_porcentagem_entre_0_e_100(100, 50)
    return result

def test_4():
    result = calculo_porcentagem_entre_0_e_100(100, 75)
    return result

def test_5():
    result = calculo_porcentagem_entre_0_e_100(100, 100)
    return result

print(test_2())