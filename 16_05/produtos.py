def mostramenu(matriz:list):
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
        break
    print(f"Seleciona uma quantidade para o produto {produtos[opcao]}")
    qtd=int(input())
    carrinho.append([opcao,qtd])

for idx, escolhausu in enumerate(carrinho):
    print(f"{idx} -> {produtos[escolhausu[0]][0]}| quantidade: {escolhausu[1]}")