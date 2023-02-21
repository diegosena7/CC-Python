inputUsuario = int(input("Informe um número para verificar se é primo: "))

while inputUsuario != 0:
    if inputUsuario % 2 == 1 or inputUsuario == 2:
        print("primo")
        break
    else:
        print("não primo")
        break
