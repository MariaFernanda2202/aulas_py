# def - definição -> abre função
# exemplo de função

def soma_dois_numeros(numero1, numero2):
    resultado= numero1+numero2
    return resultado #retorna o valor para fora da função

#print(f"Resultado da função: {soma_dois_numeros(10, 20)}")


def par_ou_impar(numero : int): #essa função se chama procedural
    if numero%2==0:
        print("Numero é par")
    else:
        print("Numero é impar")

#par_ou_impar(int(input("Digite um número inteiro: ")))
# par_ou_impar(5) = se quiser mostrar um numero sem fazer um input



def cad_lista(qtd_list:int):
    lista=[]
    for _ in range(qtd_list):
        lista.append(input("Digite a informação a ser cadastrada: "))
    return lista


def par_ou_impar_retorno(numero : int): #essa função se chama procedural
    return numero%2==0
