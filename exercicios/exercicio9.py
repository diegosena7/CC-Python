def maximo(x, y):
    if x > y:
        return x
    if x == y:
        return "Números são iguais"
    else:
        return y


print(maximo(2, 3))


def maior_primo(n):
    primos = []
    for i in range(n + 1):
        count = 0
        for j in range(n + 1):
            if i % (j + 1) == 0:
                count += 1
        if count == 2:
            primos.append(i)

    return max(primos)


print(maior_primo(100))


def vogal(n):
    if n in "aeiouAEIOU":
        return True
    else:
        return False


print(vogal('b'))
print(vogal('A'))
