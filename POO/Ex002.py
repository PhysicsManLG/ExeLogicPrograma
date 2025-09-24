'''
Instancie objetos da classe Pessoa e teste a impressão dos dados.
'''
class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade
    
    def pegar_informacoes(self):
        self.nome = input("informe o seu nome: ")
        self.idade = int(input("informe a sua idade: "))

    def mostrar_informacoes(self):
        print(f"Olá, me chamo {self.nome}, e tenho {self.idade} anos.")


pessoa1 = Pessoa()
pessoa1.pegar_informacoes()
pessoa1.mostrar_informacoes()