import os 

def mostramenu(matriz:list):
    os.system('cls')
    print("Bem vindo a nossa loja! Esses são nossos produtos")
    for idx, produto in enumerate(produtos):
        print(f"{idx} -> {produto[0]}|  R$ {produto[1]:.2f}")

produtos=[
    ["RAM 16gb", 10.99],
    ["monitor", 100],
    ["mouse", 30],
    ["teclado", 50]
]

carrinho=[] #matriz de produtos escolhindos pelos usuarios 
while True:
    mostramenu(produtos)
    opcao=int(input("Qual opçao voce gostaria de comprar: "))
    if opcao == 4:
        print("*** SAINDO DO MENU ***")
        break                                           #linha      coluna
    print(f"Seleciona uma quantidade para o produto {produtos[opcao][0]}")
    qtd=int(input())
    carrinho.append([opcao,qtd])#dentro da matriz precisamos cadastrar lista 

os.system('cls')
valorPedido=0
for idx, escolhausu in enumerate(carrinho):
    valorUnitario=escolhausu[1]*produtos[escolhausu[0]][1]
    valorPedido+=valorUnitario
    print(f"{idx} -> {produtos[escolhausu[0]][0]}| quantidade: {escolhausu[1]}| Preço unitário:{produtos[escolhausu[0]][1]} | Preço total: {valorUnitario}")
print(f"Valor final: {valorPedido:.2f}")



# matriz = nome aluno, p1, p2
#  se p1 + p2 <7:
#     matriz =exame
#     se exame<7:
#       matriz reprovado
#     else
#       matriz=aprovado