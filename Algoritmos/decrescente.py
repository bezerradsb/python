

decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequeência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente == True:
    print("A sequência está decrescente! :-) ")
else:
    print("A sequência não está decrescente! :-( ")
                
