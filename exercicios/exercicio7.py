decrescente = True

primeiroNumero = int(input("Digite o primeiro número da sequência."))

proximoNumero = 1
while proximoNumero != 0 and decrescente:
    proximoNumero = int(input("Digite o próximo número da sequência."))
    if proximoNumero > primeiroNumero:
        decrescente = False
    primeiroNumero = proximoNumero

if decrescente:
    print("Decrescente")
else:
    print("Crescente")