# print(20 / 3)
# print(2 + 5 * 3)
# print(20.0 / 3)
# print(10 > 10)
# print(9 ** 2 == 80 + 1)
# print(((5 - 3) ** 3))
# print((4 * ((33 - 31) * 2)))
# a = 5
# b = 3
# soma = a + b
# print("A soma é", soma)
# x = 10
#
# y = 15
#
# print(x + y)
#
# soma = 5.5
#
# print("soma =", soma)
#
# x = 10
#
# y = 30
#
# x = x + 10
#
# y = x + 10
# x = x + y
# print(x)
#
# x = 50
#
# y = 20
#
# aux = x
#
# x = y
#
# y = aux
# print(y)
# print(x)
#
# a = 1
# b = 2
#
# print(a + 2 * b)
#
# teste = "oi, bb"
# print("teste =", len(teste))
# peso = 74
# altura = 1.74
# imc = peso/ (altura ** 2)
# print("imc = ", imc)
#
# imcInt = int(imc)
# print("imcInt = ", imcInt)
#
# imcStr = str(imc)
# print("imcStr = ", imcStr)
# print("imcStr =", len(imcStr))
#
# print("oi =", (22 % 3))
# print("oii =", 2*1**2)
#
# a = int(input("Qual o valor de a? "))
# b = int(input("Qual o valor de b? "))
# aux = a
# a = b
# b = aux
# print(a)
# print(b)

dinheiroEmConta = 10000
terDinheiro = True
fizerSol = True
forFeriado = False
vouPraPraia = fizerSol and forFeriado
print(vouPraPraia)

vouViajar = fizerSol or fizerSol
print(vouViajar)

tirarFerias = (dinheiroEmConta > 1000 and terDinheiro == False) or not forFeriado
print(tirarFerias)

# x = 5
# y = 3
# z = 7
# print(x > 3)
# print(x > y and x < z)

idade = 15
maioridade = 18
pode_dirigir = idade >= maioridade
print(pode_dirigir)

# x = 10
# y = 15
# z = 25
# print(x == z - y and z != y - x or not y != z - x)

x = 10
# y = 20
# z = 30
# print(not y < 10 or not z == 10)
# print(x <= 30 and y >= 5)
# print(x >= 10 or y != z - x)
# print(not y > 10 or not z > 10)
print(1 + 1 + 1 == 3)

texto = "computação"
if len(texto) > 10:
    print("texto com mais de 10 caracteres")
else:
    print("texto com 10 ou menos caracteres")

a = 0
b = 2
c = 1
if (a > 0):
    if (b > 0):
        print("Tudo ok para decolagem!")
    else:
        print("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print("Foguete não tem piloto, mas há outros foguetes disponíveis!")
