qtde_notas = int(input("Quantas notas você quer incluir?"))
notas = []
for nota in range(0, qtde_notas):
    notas.append(int(input("Digite a sua nota: ")))

soma = 0
for notas_inform in notas: #vezes que vai rodar, valores a ser alimentado
  soma += notas_inform #soma das notas que foram informadas 

print(f"A médias das notas são: {round(soma / len(notas), 2)} ")