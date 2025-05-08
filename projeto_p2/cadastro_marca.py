import os

if not os.path.exists("banco_de_dados"): #verifica se o diretorio não existe  
    os.makedirs("banco_de_dados")

marcas=[]
produto=[]
while True:
    marcas=int(input("Adicionar uma marca 1 - não 0: "))
    qtd_produtos=int(input("Quantos produtos deseja adiconar: "))
    for _ in range(0, qtd_produtos):
        produto.append(input("Qual o produto: "))
     
    if marcas==0:
        print("Sistema encerrado")
        break




with open("banco_de_dados/marcas.txt", "a+") as arquivo:
    for indice, marcas in enumerate(marcas): #percorre a lista de usuarios 
        arquivo.write(marcas + ":" + produto[indice]+"\n") #escreve o usuario

    # for marca in range(0, qtd_marca):
    # marcas.append(input("Qual marca gostaria de adicionar: "))

    
# qtd_marca=int(input("Quantas marcas deseja cadastrar: "))