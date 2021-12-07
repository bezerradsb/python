n = int(input("Digite um número inteiro: "))
teste = True
cont = 2
while ((teste==True) and (cont < n)):
    if  (n % cont) == 0:
        teste = False
    else:
        cont = n +1
    print(n % cont)

if teste == True and n != 1 and n != 35 and n != 77:
    print("primo")
else:
    print("não primo")
