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


def qtd_input(qtd_info):
    informada=[]
    qtd_informada=int(input("Quantas infotmações deseja adicionar: "))
    for indice in range(0, qtd_informada):
        informada.append(input(f"Informação {indice+1}:"))
        print(informada)

def calculadora_imc(qtd_informada: int): #quando for passar para o local desejado, vc coloca 
    resultados=[]
    for indice in range(0, qtd_informada):
        peso=int(input("Peso: "))
        altura=float(input("Informe sua altura: "))

        imc=(peso/(altura**altura))
        resultados.append(round(imc,2)) #append adiciona as informações na lista vazia 
    print(f"Seu imc é {resultados}")
    #quando passa um return ele encerra a função e pode ser manipulavel no print que vai colocar onde quer chamar
    #já o print não deixa manipular a informação, ex: quero só o imc 2, em return dá em print não.