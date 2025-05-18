#carregar arquivo de senha 
#pedir usuario e senha, digitar , getpass
# ler arquivo de senha 
# verificar se usuario e senha digitados existe no arquivo
# se sim logar
# se não falar que está errado usuario e senha 
                                    #usuario
                                    #senha

import os
from getpass import getpass

caminho_arquivo="../arquivos/senhas.txt" #le o arquivo de senhas


usuarios=[]
senhas=[]


login=(input("Digite o login do suário: "))
senha=(getpass("Digite sua senha: "))
  
while True:
    with open(caminho_arquivo, 'r') as arquivo: #abre o senhas.txt e lê ele e adiciona essa informação para o nome arquivo
        conteudo = arquivo.read() #atribui a leitura dos dados do arquivo para conteudo
        print("verificando senha")
        if login in conteudo: #se a avariavel login estiver em conteudo
            #o if lê se esta e se sim cai pro if de baixo 
            print("Verificando senha")
            if senha in conteudo:  #se senha esta em conteudo
                print("Login") #se sim o login é feito
                break
        else: #se qualquer informação estiver errada ele cai no else
            print(f"O usuário {login} e sua senha não exitem, por favor, cadastre-os: ")
            usuarios.append(input("Digite o login do suário: "))
            senhas.append(getpass("Digite sua senha: "))
            
                #abrir  #diretorio+nome  #append(acrecentar)
            with open(caminho_arquivo, "a+") as arquivo: #arquivo é uma variável de contexto, não importa muito
                for indice, usuario in enumerate(usuarios): #percorre a lista de usuarios 
                    arquivo.write(usuario + ":" + senhas[indice]+"\n") #escreve o usuario

                print("Cadastrado com sucesso!!")

    if not senha in conteudo:   
        opcao=int(input("Deseja se logar? Se NÃO escolha a opção 0, se sim digite 1: "))     
        if opcao== 0:       
            print("Ok")
            break
        else:
            print("Usuário logado")
    



#     estoque de mercado 
# -> gravação vai funcionar como bd 
# cadastro de marca: nome da marca
# cad produtos: nome, preço, marca(pega o nome da marca), data de valiade,qtd estoque 
# visualização dos produtos
# compra: escolhe o produto e qtd 
# quando comprar subtrair do estoque existente
# tenho 10, comprou 3, aparece 7 
 
