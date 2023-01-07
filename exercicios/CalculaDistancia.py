x1 = int(input("Informe a coordenada X1: "))
y1 = int(input("Informe a coordenada Y1: "))
x2 = int(input("Informe a coordenada X2: "))
y2 = int(input("Informe a coordenada Y2: "))

distancia = (x1 - x2) ** 2 + (y1 - y2) ** 2

print("Distância: ", distancia)

if distancia >= 10:
    print("longe")
else:
    print("perto")
