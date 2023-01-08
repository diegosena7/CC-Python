inputUsuario = int(input("Numero: "))
soma = 0
while inputUsuario != 0:
    resto = inputUsuario % 10
    inputUsuario = (inputUsuario - resto) // 10
    soma = soma + resto
print(soma)
