num1=float(input("Digite um numero: "))
num2=float(input("Digite um numero: "))
operacao=input("Qual o peração você quer fazer 'soma', 'div', 'sub', 'mult':")

if operacao == ('soma'):
    print(f"{num1} + {num2}= {num1+num2}")
elif operacao == ("sub"):
     print(f"{num1} - {num2}= {num1-num2}")
elif operacao == ("div"):
      print(f"{num1} / {num2}= {num1/num2}")
elif operacao == ("mult"):
      print(f"{num1} x {num2}= {num1*num2}")
else: 
     print("operação incorreta")