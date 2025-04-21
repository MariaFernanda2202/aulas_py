from os import remove

while True:
    print("Escolha um número para ser executado")
    print("1.	Imprimir os números de 1 a 10 usando um loop.")
    print("2.	Imprimir os números pares de 0 a 20 usando um loop")
    print("3.	Imprimir a soma dos números de 1 a 100 usando um loop.")
    print("4.	Imprimir os números de 1 a 10 em ordem reversa usando um loop.")
    print("5.	Imprimir os números ímpares de 1 a 20 usando um loop.")
    print("6.	Imprimir os números ímpares da lista [2, 5, 8, 11, 14]")
    print("7.	Imprimir os números de 1 a 100 que são divisíveis por 3 usando um loop.")
    print("8.	Gravador de nomes")
    print("9.   Lista de compras")
    print("10.  Lista de jogos")
    escolha=int(input("Digite o número da escolha desejada"))

    if escolha==1:
        for numeros in range(1, 11): #cria uma lista fake
            print(numeros)
        
    elif escolha==2:
        tabuada = 2
        for numero in range(0, 10): #criar uma lista fake
            print(tabuada * (numero+1))

    elif escolha==3:
        contador =0
        soma=0

        for contador in range(1, 101):
          soma+= contador
          contador= contador +1
          print(soma)

    elif escolha==4:
        for numeros in range(10, 0, -1):
         print(numeros)

    elif escolha==5:
        for impar in range(1, 21):
            if impar%2>0:
                print(impar)

    elif escolha==6:
        lista_numeros = [2, 5, 8, 11, 14]
        print(lista_numeros)
        for indice, numero in enumerate(lista_numeros):
            if numero %2>0:
                print(f"Posição do Número: {indice+1} = {numero}")

    elif escolha==7:
        for numero in range(1, 101):
            if (numero %3) ==0:
                print(f"numeros de 1 a 100, diviões exatas por 3 = {numero}")

    elif escolha==8:
        lista_nomes = []

        for qtd_nomes in range(0, 10):
            lista_nomes.append(input("Digite o seu nome: "))

        for indice, nome in enumerate(lista_nomes):
            print(f"{indice+1}. {nome}") 

    elif escolha==9:
        lista_compras = []

        for qtd_compras in range(0, 10):
            lista_compras.append(input("Digite o produto que deseja comprara: "))

        for indice, nome in enumerate(lista_compras):
            print(f"{indice+1}. {nome}")

        for compras in range(0, len(lista_compras)):
            if lista_compras != 0:
                oq_compra=input("O que está comprando? ")
                lista_compras.remove(oq_compra)
                print(lista_compras)
            else:
                print("Não existe esse item na lista ou a lista")

    elif escolha==10:
        quantidadeItens = int(input('Digite a quantidade de itens: '))
        listaJogo = []
        listaPreco = []
        listaNota = []

        for contador in range(1, (quantidadeItens + 1)):
            listaJogo.append(input(f'{contador}º Digite o nome do jogo: '))
            listaPreco.append(float(input(f'{contador}º Digite o preço do jogo: ')))
            listaNota.append(float(input(f'{contador}º Digite a nota do jogo (1 - 10): ')))

            indiceMelhor = 0
            indicePior = 0
            indiceMaisCaro = 0
            indiceMaisBarato = 0

            for i in range(1, quantidadeItens):
                if listaNota[i] > listaNota[indiceMelhor]:
                    indiceMelhor = i
                if listaNota[i] < listaNota[indicePior]:
                    indicePior = i
                if listaPreco[i] > listaPreco[indiceMaisCaro]:
                    indiceMaisCaro = i
                if listaPreco[i] < listaPreco[indiceMaisBarato]:
                    indiceMaisBarato = i

            print("\nJogo melhor avaliado:")
            print(f'Nome: {listaJogo[indiceMelhor]}, Preço: {listaPreco[indiceMelhor]}, Nota: {listaNota[indiceMelhor]}')

            print("\nJogo pior avaliado:")
            print(f'Nome: {listaJogo[indicePior]}, Preço: {listaPreco[indicePior]}, Nota: {listaNota[indicePior]}')

            print("\nJogo mais caro:")
            print(f'Nome: {listaJogo[indiceMaisCaro]}, Preço: {listaPreco[indiceMaisCaro]}, Nota: {listaNota[indiceMaisCaro]}')

            print("\nJogo mais barato:")
            print(f'Nome: {listaJogo[indiceMaisBarato]}, Preço: {listaPreco[indiceMaisBarato]}, Nota: {listaNota[indiceMaisBarato]}')

            print("\nTodos os jogos cadastrados:")
            for i in range(quantidadeItens):
             print(f'Nome: {listaJogo[i]}, Preço: {listaPreco[i]}, Nota: {listaNota[i]}')

        else:
            print("Escolha não reconhecida")