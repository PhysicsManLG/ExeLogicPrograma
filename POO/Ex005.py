'''
Crie um método aniversario() que aumenta a idade da pessoa em 1 ano.
'''

class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def pegar_informacoes(self):
        self.nome=input("Olá, como se chama? ")
        self.idade=int(input(f"Muito bem {self.nome}, e qual sua idade? "))
    
    def mostrar_informacoes(self):
        print(f"Olá, me chamo {self.nome} e tenho {self.idade} anos.")
    
    def aniversario(self):
        self.idade+=1

        print(f"Fiz aniversário e agora tenho {self.idade} anos.")

pessoa1 = Pessoa()
pessoa1.pegando_informacoes()
pessoa1.mostrando_informacoes()
pessoa1.aniversario()