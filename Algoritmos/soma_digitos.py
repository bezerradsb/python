n = int(input("Digite o valor de n: "))

v = 1
novo = 0
sobra = 0

while n != 0:
    v = n % 10
    n = n // 10
    sobra = sobra + v
    

print(sobra) 



