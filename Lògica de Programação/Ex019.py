'''
Peça um valor e verifique se ele é um número primo.
'''

numero_primo = int(input("informe um número inteiro qualquer maior que 1: "))

if numero_primo <= 1:
    print("Não é primo")
elif numero_primo % 2 == 0 and numero_primo != 2:
    print("Não é primo")
elif numero_primo % 3 == 0 and numero_primo != 3:
    print("Não é primo")
elif numero_primo % 5 == 0 and numero_primo != 5:
    print("Não é primo")
elif numero_primo % 7 == 0 and numero_primo != 7:
    print("Não é primo")
else:
    print("é primo")