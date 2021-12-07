import math

print("Entre com o valor de x,y do ponto 1")
x1 = float(input("Digite o valor de X1: "))
y1 = float(input("Digite o valor de Y1: "))

print("Entre com o valor de x,y do ponto 2")
x2 = float(input("Digite o valor de X2: "))
y2 = float(input("Digite o valor de Y2: "))

distancia = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if distancia >= 10:
    print("longe")
else:
    print("perto")
