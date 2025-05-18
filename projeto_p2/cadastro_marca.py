import os

if not os.path.exists("banco_de_dados"): #verifica se o diretorio não existe  
    os.makedirs("banco_de_dados")

marcas=[]
while True:
    opcao=int(input("Adicionar uma marca 0 - sair 1: "))
    
    if opcao==1:
        print("Sistema encerrado")
        break
    
    qtd_marcas=int(input("Quantas marcas deseja adicionar? "))
    for _ in range(0, qtd_marcas):
        marca=input("Qual a marca? ")

        qtd_produtos=int(input("Quantos produtos dessa marca deseja adicionar? "))
        produtos=[]
        for i in range(0, qtd_produtos):   
            produtos.append(input("Qual o produto"))
        marcas.append({"marca":marca, "produtos":produtos})
    

    




with open("banco_de_dados/marcas.txt", "a+") as arquivo:
    for indice_marca, marca in enumerate(marcas): #percorre a lista de usuarios 
        print(marca["marca"])
        for indice_produto, produto in enumerate(marcas[indice_marca]["produtos"]):
            print(produto)

            arquivo.write(marca["marca"] + ":" +produto+"\n") #escreve o usuario




    # for marca in range(0, qtd_marca):
    # marcas.append(input("Qual marca gostaria de adicionar: "))

    
# qtd_marca=int(input("Quantas marcas deseja cadastrar: "))