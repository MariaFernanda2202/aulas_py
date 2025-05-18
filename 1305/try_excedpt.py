#ZeroDividionError -> erro de divisão por zero
#ValueError -> Erro de input de valor (conversão)
#IndexError -> Erro de indice (lista de laço de repetição
#FileNotFoundError -> arquivo não encontrado (with open())
#KeyboardInterrupt -> usuario interrompeu a execução


# try: #tentar executar algum codigo
#     resultado=10/0
# except:
#     print("Não é possível dirvir por zero")
# print("Teste")



def simula_erros(opcao:int):
    deu_erro=False
    if opcao==1:
        print("Simulação do erro por zero")
        try:
            #tenta executar (tipo o if)
            10/int(input("Digite um numero"))
            deu_erro=False
        except Exception as erro:
            #caso de erro ele executa esse aqui
            print("O código não funcionou, leia o erro abaixo")
            print(f"Seu erro foi {erro}")
            deu_erro=True
        finally: #fecha conexão em um banco de dados, executa dando erro ou não
            return deu_erro
        
    elif opcao==2:
        print("Simulação de ValueError")
        try: 
            int(input("Digite um número inteiro: "))
            deu_erro:False
        except Exception as erro:
            print("O código não funcionou, leia o erro abaixo")
            print(f"o erro foi: {erro}")
            deu_erro:True
        finally: 
            return deu_erro
    elif opcao==3:
        print("simulação IndexError")
        try:
            teste=[1,2,3,4]
            entrada=teste[input("Digite um numero: ")*0]
            print(f"A sua escolha foi {entrada}")
            deu_erro:False
        except Exception as erro:
            print("O código não funcionou, leia o erro abaixo")
            print(f"o erro foi: {erro}")
            deu_erro:True
        finally: 
            return deu_erro
    elif opcao==4: ##ver isso
        print("Simulação Arquivo não encontrado")
        caminho_arquivo="../arquivos/não tem.txt"
        try:
            caminho_arquivo[str(input("Digite o nome do arquivo "))] 
            deu_erro: False
        except Exception as erro:
            print("O código não funcionou, leia o erro abaixo")
            print(f"o erro foi: {erro}")
            deu_erro:True
        finally: 
            return deu_erro
            
if simula_erros(int(input("Digie qual erro quer simular: "))):
    print("Não deu erro")
else:
    print("Deu erro")



#objetico de escrever log quando algo dar erro
                #nome da funcao variavel do erro
def escreve_log(funcao: str, erro:str):
    with open("log.txt", "a+")as arquivo_erro:
        arquivo_erro.white("Erro da duncao "+funcao+" Erro foi: "+ str(erro))
    print(f"Erro na execução, verifique o arquivo de log")

def cadastra_produto(qtd:int):
    for i in range(0, qtd):
        nome=input("Digite o nome do produto: ")
        try: 
            preco=float(input("Digite o preco do produto: "))
            with open("Poduros.txt", "a+") as arquivo:
                arquivo.write(nome+str(preco)+"\n")
            deu_erro=True
        except Exception as erro:
            escreve_log("cadastra_produto", erro)
            deu_erro=True
        finally:
            return deu_erro