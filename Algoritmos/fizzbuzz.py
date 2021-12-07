valor = int(input("Digite o valor: "))

resto1 = valor % 5
resto2 = valor % 3

if resto1 == 0 and resto2 == 0:
    print("FizzBuzz")
else:
    print(valor)
