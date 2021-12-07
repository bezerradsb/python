n = int(input("Digite um número inteiro: "))

teste = True
resto1 = 1
resto2 = 1
quociente = 1

while teste == True:
    quociente = n // 10
    resto1 = n % 10
    resto2 = quociente % 10
    if resto1 == resto2:
        teste = False
    else:
        n = quociente

if teste == False and n > 0:
    print("sim")
else:
    print("Não")
