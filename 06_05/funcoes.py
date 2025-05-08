def soma(num1, num2):
    resultado = num1+num2
    return resultado


def fatorial(fator):
    resultado=1
    for conta in range(1, fator+1):
        resultado *=conta
    return resultado


def eh_palindromo(palim):
    teste=palim.upper().replace(" ", "")
    if teste==teste[::-1]:
        print(True)
    else:
        print(False)


def primos(a,b):
    numeros=[]
    for primos in range(a, b):
        if primos>1:
            for i in range(2, primos):
                if primos % i==0:
                    break
                else: 
                    numeros.append(int(primos))
    print(f"Os números primos são: {numeros}")
        
