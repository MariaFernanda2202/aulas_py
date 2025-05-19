import os

if not os.path.exists("banco_de_dados"): #verifica se o diretorio não existe  
    os.makedirs("banco_de_dados")

marcas=[]


# MOSTRA O TXT
with open("banco_de_dados/marcas.txt", "r") as arquivo:
        marcas_e_produtos=arquivo.read()
        

#ADICONANDO NO ESTOQUE
while True:
    print("Bem vindo ao estoque")
    print(f"Situação atual do estoque: \n{marcas_e_produtos}")
    print("Digite 1: Para adicionar uma marca e seus produtos")
    print("Digite 2: Para remover uma marca ou um produto de uma marca")
    print("Digite 0: Para sair")
    opcao=int(input("Qual sua escolha? "))
    
    if opcao==0:
        print("Sistema encerrado")
        break
    if opcao==1:
        qtd_marcas=int(input("Quantas marcas deseja adicionar? "))
        for _ in range(0, qtd_marcas):
            marca=input("Qual a marca? ")

            qtd_produtos=int(input("Quantos produtos dessa marca deseja adicionar? "))
            produtos=[]
            valor=[]
            qtd_em_estoque=[]
            for i in range(0, qtd_produtos):   
                produtos.append(input("Qual o produto: "))
                valor.append(float(input("Qual o valor do produto?")))  
                qtd_em_estoque.append(int(input("Quantos produtos dessa marca com esse preço deseja adicionar? ")))
            marcas.append({"marca":marca, "produtos":produtos, "valores":valor, "qtd_produto_estoque":qtd_em_estoque})
        

        # RESGISTRANDO NO TXT
        with open("banco_de_dados/marcas.txt", "a+") as arquivo:
            for marca in marcas:
                for i in range(len(marca["produtos"])):
                    linha = f"{marca['marca']}: {marca['produtos'][i]} - R$ {marca['valores'][i]:.2f}: Quantidade em estoque: {marca['qtd_produto_estoque'][i]}"
                    arquivo.write(linha + "\n")
                    print(f"A atualização do seu estoque já foi salva: ")

 

    # if opcao==2:
    #     marca_excluir=input("Qual marca deseja excluir: ")


#MOSTRANDO O ESTOQUE ATUALIZADO
print(f"Segue a nova planilha: ")
print(marcas_e_produtos)
