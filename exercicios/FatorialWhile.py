numero = int(input("Digite um numero inteiro positivo:  "))

while numero >= 0:
    fatorial = 1
    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1
    print("Fatorial:", fatorial)
    numero = int(input("Digite um numero inteiro positivo:  "))
