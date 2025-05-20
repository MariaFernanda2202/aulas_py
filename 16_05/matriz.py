#crinado uma matriz
matriz=[
            ["Caio",34,1.83],["Rafael",35,1.85],["Henrique",28,1.82]
        ]

#print(matriz)
#print((type(matriz)))

#como mostrar algo dentro dessa matriz
##print(matriz[1][1])#sempre começa do zero 
#primeiro sempre a linha depois a coluna

for idx, linha in enumerate(matriz, 1):
    print(f"{idx}-> {linha}")
    for idx, coluna in enumerate(linha):
        print(f"{idx}-> {coluna}")