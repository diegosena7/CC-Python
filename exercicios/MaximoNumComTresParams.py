def maximo(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    else:
        return z


print(maximo(30, 14, 10))
print(maximo(0, -1, 1))
