'''
Modifique a classe para que o atributo idade seja privado e acessado via métodos.
'''

class Pessoa:
    def __init__(self, nome, idade=31):
        self.nome = nome
        self.__idade = idade
    
    def mostrar_idade(self):
        return self.__idade
    
pessoa = Pessoa(nome="Guts")

print(pessoa.nome)
print(pessoa.mostrar_idade())