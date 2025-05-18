#1 soma de dois numero 
def soma(num1, num2):
    resultado = num1+num2
    return resultado


# conversor de temperatura
def conversor(temp):
    calculo = str(input("Digite k se quiser converter para Kelvin, e f se quiser converter para Farenheit: "))
    kelvin = 273.15

    if calculo.upper() == "K":
        print(f"Convertido para Kelvin, a temperatura é: {temp + kelvin}")
    elif calculo.upper() == "F":
        print(f"Convertendo para Farenheit, a temperatura é: {((9*temp)/5) + 32}")
    else:
        print("Você digitou a letra errada")


# fatorial recursivo
def fatorial(fator):
    resultado=1
    for conta in range(1, fator+1):
        resultado *=conta
    return resultado


# verificador de palindromo 
def eh_palindromo(palim):
    teste=palim.upper().replace(" ", "")
    if teste==teste[::-1]:
        print(True)
    else:
        print(False)


# sequencia fibonacci
def fibonacci(limite):
    sequencia = []
    a = 0
    b = 1
    while b <= limite:
            sequencia.append(b)
            a, b = b, a + b
    print(sequencia)


# numero primos
def primos(a,b):
    numeros=[]
    for primos in range(a, b):
        if primos>1:
            for i in range(2, primos):
                if primos % i==0:
                    break
            else:    
              numeros.append(primos)
    print(f"Os números primos são: {numeros}")
    


# prefixo comum mais longo 
def prefixo(palavras):
    entrada=palavras.upper().split(", ")

    if entrada == []:
        return 'Não há elementos na lista'
    if len(entrada) == 1:
        return entrada[0]
    entrada.sort()
    palavra_1 = entrada[0]
    prefixo = ''
    for i in range(len(palavra_1)):
        if entrada[len(entrada) - 1][i] == palavra_1[i]:
            prefixo += entrada[len(entrada) - 1][i]
        else:
            break
    return prefixo


# validador de cpf
def validadorCPF(cpf):
    cpf = [int(d) for d in str(cpf)]
    digito1=cpf[0]
    digito2=cpf[1]
    digito3=cpf[2]
    digito4=cpf[3]
    digito5=cpf[4]
    digito6=cpf[5]
    digito7=cpf[6]
    digito8=cpf[7]
    digito9=cpf[8]

    # obter o primeiro digitos de validação
    soma= ((digito1*10)+(digito2*9)+(digito3*8)+(digito4*7)+(digito5*6)+(digito6*5)+(digito7*4)+(digito8*3)+(digito9*2))
    resto= soma%11
    digito10=11-resto

    if digito10 >9:
        digito10=0

    # obter o segundo digitos de validação
    somadg11=((digito1*11)+(digito2*10)+(digito3*9)+(digito4*8)+(digito5*7)+(digito6*6)+(digito7*5)+(digito8*4)+(digito9*3)+(digito10*2))
    restodigito11=somadg11%11
    digito11=11-restodigito11
    
    if digito11>9:
        digito11=0


    #resultado real
    if cpf[9]==digito10 and cpf[10]==digito11:
        print("O CPF informado é real")
    else:
        print("O CPF indormado não é real")