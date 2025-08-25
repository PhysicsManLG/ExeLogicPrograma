'''
Exiba a tabuada de um número fornecido pelo usuário
'''

numero = int(input("informe um número qualquer: "))
contador = 1
'''result = 1'''

for contador in range(1,10):
    print(f"{numero} X {contador} = {numero*contador}")

'''while contador <= 10:
    result = numero*contador
    print(f"{numero} x {contador} = {result}")
    contador+=1'''