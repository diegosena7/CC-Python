inputUsuario = int(input("Infome o número: "))
cond = True

while cond:
    x1 = inputUsuario % 10
    x = inputUsuario // 10
    x2 = x%10
    if inputUsuario <= 10:
        print('não')
        cond = False
    elif inputUsuario > 10 and x1 == x2:
        print('sim')
        cond = False
    else:
        inputUsuario = inputUsuario // 10