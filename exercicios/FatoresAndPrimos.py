numUser = int(input("Digite um número inteiro maior que 1: "))

fator = 2
multiplicidade = 0

while numUser > 1:
    while numUser % fator == 0:
        multiplicidade = multiplicidade + 1
        numUser = numUser / fator
    if multiplicidade > 0:
        print("Fator", fator, "Multiplicidade", multiplicidade)
    fator = fator + 1
    multiplicidade = 0
