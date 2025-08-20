'''
Determine se um triângulo é equilátero, isósceles ou escaleno
'''

lado_A=int(input("informe um dos lados do triângulo: "))
lado_B=int(input("Informe o segundo lado do triângulo: "))
lado_C=int((input("informe o terceiro lado do triângulo: ")))

print(f"\nSeu triangulo é formado pelos lados {lado_A}, {lado_B} e {lado_C}.\n")

if lado_A+lado_B>lado_C and lado_A+lado_C>lado_B and lado_C+lado_B>lado_A:
    print("Realmente é um triângulo")
    if lado_A == lado_B and lado_B==lado_C:
        print("É um triângulo equilátero!")
    elif lado_A==lado_B or lado_A==lado_C or lado_B==lado_C:
        print("É um triângulo isósceles!")
    else:
        print("É um triângulo escaleno!")
else:
    print("não é um triângulo!")
