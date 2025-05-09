import funcoes

while True:
    print("Escolha uma conta")
    print("Conta 1: Soma de Dois Números")
    print("Conta 2: Conversor de Temperatura")
    print("Conta 3:  Fatorial Recursivo")
    print("Conta 4: Verificador de Palíndromos")
    print("Conta 5: Sequência de Fibonacci até N")
    print("Conta 6: Números Primos em Intervalo")
    print("Conta 7: Prefixo Comum Mais Longo")
    print("Conta 8: Validador de CPF Simplificado")
    escolha=int(input("Qual a sua escolha: "))

    if escolha == 1:
        print(funcoes.soma( 2, 3))
        break
    elif escolha == 2:
          print(funcoes.conversor(int(input("Digite uma temperatura em Celsius: "))))
          break
    elif escolha==3:
        print(funcoes.fatorial(5))
        break
    elif escolha == 4:
        print(funcoes.eh_palindromo(input("Digite uma frase: ")))
        break
    elif escolha == 5:
        print(int(input("Digite um limite para a sequencia de Fibonacci: ")))
        break
    elif escolha == 6:
        print(funcoes.primos(a=int(input("Informe um numeros:  ")),b=int(input("Informe outro numeros:  "))))
        break
    elif escolha == 7:
        print(funcoes.prefixo(input("Informe uma sequência de palavras: ")))
        break
    elif escolha ==8:
        print(funcoes.validadorCPF(int(input("Insira um CPF SEM caracteres especiais: "))))
        break
    else:
        print("Escolha não valida!")

