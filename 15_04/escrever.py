import os #importação da bivlioteca do sistema operacional
from getpass import getpass #biblioteca que esconde senha 

if not os.path.exists("arquivos"): #verifica se o diretorio não existe  
    os.makedirs("arquivos") #se não, criar

# ---------------------------------------

usuarios=[]
senhas=[]
while True:
    usuarios.append(input("Digite o login do suário: "))
    senhas.append(getpass("Digite sua senha: "))
    opcao=int(input("Digite 1 para continuiar e 0 para sair. "))
    
    # if opcao == 0


print("Gravando informações: ")
                            #não apaga as demais senhas 
    #abrir  #diretorio+nome  #append(acrecentar)
with open("arquivos/senhas.txt", "a+") as arquivo: #arquivo é uma variável de contexto, não importa muito
    for indice, usuario in enumerate(usuarios): #percorre a lista de usuarios 
        arquivo.write(usuario + ":" + senhas[indice]+"\n") #escreve o usuario

        print("Arquivos gravados")