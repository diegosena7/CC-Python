def soma(x, y):
    return x + y


print(soma(5, 7))


def multiplicaValores(x, y):
    return x * y


print(multiplicaValores(5, 7))


def subtraiValores(x, y):
    return x - y


print(subtraiValores(5, 3))


def divideValores(x, y):
    return x / y


print(divideValores(10, 5))


def test_soma():
    assert soma(5, 7) == 12


def test_subtracao():
    assert subtraiValores(5, 3) == 2


def test_multiplicacao():
    assert multiplicaValores(3, 5) == 15


def test_divisao():
    assert divideValores(15, 3) == 5