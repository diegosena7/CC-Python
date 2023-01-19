def fatorial(x):
    resultado = 1
    count = 1

    while count <= x:
        resultado *= count
        count += 1

    print(resultado)


fatorial(5)
