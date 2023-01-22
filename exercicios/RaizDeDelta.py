import math


def main_delta():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)


def delta(a, b, c):
    return b ** 2 - 4 * a * c


def imprime_raizes(a, b, c):
    delta_func = delta(a, b, c)
    if delta_func == 0:
        raiz1 = (-b + math.sqrt(delta_func)) / (2 * a)
        print("A única raiz é:", raiz1)
    else:
        if delta_func < 0:
            print("Esta equação não possui raízes reais")
        else:
            raiz1 = (-b + math.sqrt(delta_func)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta_func)) / (2 * a)
            print("Raiz 1 = ", raiz1)
            print("Raiz 2 = ", raiz2)


main_delta()
print("Raiz: ", delta(5, 20, 5))
