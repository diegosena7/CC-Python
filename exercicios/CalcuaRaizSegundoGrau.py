a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

print(f"A equação é: ({a}).x^2 + ({b}).x + ({c})")

delta = b * b - 4 * a * c

if delta < 0:
    print("Não possui raízes reais")
elif delta == 0:
    print("Apenas uma raiz")
    raiz = (-b + pow(delta, 1 / 2)) / 2 * a
    print(f"A raiz é: x = {raiz}")
else:
    print("Duas raízes")
    raiz1 = (-b + pow(delta, 1 / 2)) / 2 * a
    raiz2 = (-b - pow(delta, 1 / 2)) / 2 * a
    print(f"x1 = {raiz1:.2f}, x2 = {raiz2:.2f}")
