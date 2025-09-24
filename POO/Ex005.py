'''
Crie um método aniversario() que aumenta a idade da pessoa em 1 ano.
'''

class Pessoa:
    def __init__(self, nome="", idade=0, email=""):
        self.nome = nome
        self.idade = idade
        self.email = email
    
    def pegar_informacoes(self):
        self.nome = input("Informe seu nome: ")
        self.idade = int(input("Informe sua idade: "))
        self.email = input("Informe seu email: ")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Email: {self.email}")
    
    def trocar_email(self):
        while True:
            novo_email = input("informe o novo email: ")
            if novo_email == self.email:
                print(f"email é o mesmo!")
            else:
                self.email = novo_email
                print(f"O email atualizado com sucesso!\nSeu novo email é {self.email}")
                break
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome}")
    
    def aniversario(self):
        self.idade+=1

        print(f"Fiz aniversário e agora tenho {self.idade} anos.")

pessoa1 = Pessoa()
pessoa1.pegar_informacoes()
pessoa1.mostrar_informacoes()
pessoa1.trocar_email()
pessoa1.mostrar_informacoes()
pessoa1.falar()
pessoa1.aniversario()
