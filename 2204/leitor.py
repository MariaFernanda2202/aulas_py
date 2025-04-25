import os#importação do lib sistema operacional para ver se arquivo existe 


caminho_arquivo="../arquivos/senhas.txt" #..volta e verifica se o arquivo escolhido existe


if os.path.exists(caminho_arquivo):#verifica se o diretório esta correto 
    print("arquivo existe")      #r de read
    with open(caminho_arquivo, "r")  as arquivo:
        for indice, linha in enumerate(arquivo):
            usuario_arquivo = linha.split(":") [0]#split retorna uma lista em um input unico 
            senha_arquivo=linha.split(":")[1]
            print(f"Usuário nº {indice+1}: {usuario_arquivo} | {senha_arquivo}")
else: 
    print("não existe")