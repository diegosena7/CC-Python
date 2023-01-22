def maximo(x, y):
    if x > y:
        return x
    if x == y:
        return "Números são iguais"
    else:
        return y


print(maximo(2, 3))