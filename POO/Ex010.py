'''
Modifique a classe para incluir um atributo de classe total_pessoas que conte quantos objetos foram instanciados.
'''

class Pessoa:
    total_pessoas = 0

    def __init__(self, nome="", idade=0, email=""):
        self.nome = nome
        self._idade = idade
        self._email = email
        Pessoa.total_pessoas += 1
    
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
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("idade menor que zero?! Acho que não")

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email
    
    @classmethod
    def nova_pessoa(cls):
        nome = input("informe nome: ")
        idade = 18
        return cls(nome, idade)
    
    @staticmethod
    def quantidade_pessoas():
        return Pessoa.total_pessoas
        

pessoa1 = Pessoa()
pessoa2 = Pessoa()
pessoa3 = Pessoa.nova_pessoa()

'''pessoa1.pegar_informacoes()
pessoa1.mostrar_informacoes()
pessoa1.trocar_email()
pessoa1.mostrar_informacoes()
pessoa1.falar()
pessoa1.aniversario()
'''

'''
pessoa2.idade = 29
pessoa2.email = "casca@berserk.com"
print(pessoa2.idade)
print(pessoa2.email)'''

'''print(pessoa3.nome, pessoa3.idade)'''

'''print(f"Total de pessoas criadas (método estático): {Pessoa.quantidade_pessoas()}")'''
print(f"Total de pessoas criadas (atributo de classe): {Pessoa.total_pessoas}")
