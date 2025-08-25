'''
Peça a idade de uma pessoa e diga se ela pode votar.
'''

idade=int(input("Qual sua idade? "))

if idade>=18 and idade<70:
    print(f"{idade} anos. Voto obrigatório!")
elif (idade>=16 and idade<18) or (idade>=70):
    print(f"{idade} anos. Voto não obrigatório")
else:
    print(f"{idade} anos. Não vota!")