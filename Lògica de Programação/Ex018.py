'''
Calcule o IMC e classifique o peso.
'''

#vamos criar a variável que recebe o peso e a altura
peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em m: "))

#calculando o IMC
imc = peso/(altura**2)

#validando as condições de acordo com a tabela do imc
if imc < 18.5:
    print(f" seu imc é de {imc}. Baixo peso")
elif imc >= 18.5 and imc <= 24.9:
    print(f"seu imc é de {imc}. Peso Normal")
elif imc >= 25 and imc <= 29.9:
    print(f"seu imc é de {imc}. Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print(f"seu imc é de {imc}. Obesidade grau 1")
elif imc >= 35 and imc <= 39.9:
    print(f"seu imc é de {imc}. Obesidade grau 2")
else:
    print(f"seu imc é de {imc}. Obesidade grau 3")
