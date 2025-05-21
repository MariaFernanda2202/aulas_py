matriz_aluno_nota=[] #matriz

while True:
        nome_aluno = input("Digite o nome do aluno ou SAIR para sair: ").upper()
        if nome_aluno == "SAIR":
                break
        p1=float(input("Qual a nota de p1: "))
        p2=float(input("Qual a nota de p2: "))

        if ((p1+p2)/2)<7:
                print("Aluno está de exame")
                exame=float(input("Digite a nota do exame: "))
                if exame >= 7:
                        situacao = "Aprovado"
                else:
                        situacao = "Reprovado"
        else:
                exame = ''
                situacao = "Aprovado"
        
        matriz_aluno_nota.append([nome_aluno, p1, p2, exame, situacao])

for idx, aluno in enumerate(matriz_aluno_nota, 1):
        print(f"{idx} -> Nome: {aluno[0]}|  Nota p1: {aluno[1]}| Nota p2: {aluno[2]}| Exame: {aluno[3]}| Situação: {aluno[4]}")
