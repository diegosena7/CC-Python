qtidadeCartoesNaLista = int(input("Digite o número de cartões a serem procurados: "))
cartaoUsuario1 = int(input("Digite o número do seu cartão de crédito: "))
cartaoEncontrado = False

i = 1
while not cartaoEncontrado and i <= qtidadeCartoesNaLista:
    i = i + 1
    cartaoUsuario2 = int(input("Digite o número do próximo cartão de crédito: "))

    if cartaoUsuario1 == cartaoUsuario2:
        cartaoEncontrado = True
        print("Cartão encontrado")

    else:
        print("Cartão NÃO encontrado")