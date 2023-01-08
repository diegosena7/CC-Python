fatorial = int(input("Digite um número número: "))

resultado = 1
count = 1

while count <= fatorial:
    resultado *= count
    count += 1

print(resultado)

