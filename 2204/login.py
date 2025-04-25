#carregar arquivo de senha 
#pedir usuario e senha, digitar , getpass
# ler arquivo de senha 
# verificar se usuario e senha digitados existe no arquivo
# se sim logar
# se não falar que está errado usuario e senha 
                                    #usuario
                                    #senha

import os.path 
from getpass import getpass

caminho_arquivo="../arquivos/senhas.txt" #le o arquivo de senhas


usuarios=[]
senhas=[]

usuarios.append(input("Digite o login do suário: "))
senhas.append(getpass("Digite sua senha: "))
  
with open(caminho_arquivo, 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


    