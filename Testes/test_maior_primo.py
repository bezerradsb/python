def maior_primo(x):
    teste = True
    cont = 1
    n = x
    while teste != False:
        while ((teste==True) and (cont < x)):
            if  (x % cont) == 0:
                teste = False
            else:
                cont = x + 1
                n = n - 1
    return n

def teste_maior_primo():
    assert maior_primo(100) == 97
