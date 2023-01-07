numUsuario = int(input("Informe um número: "))

if numUsuario % 5 == 0 and numUsuario % 3 == 0:
    print("FizzBuzz")
else:
    print(numUsuario)