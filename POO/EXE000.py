class Pessoa:
    total_pessoas = 0  # atributo de classe que conta todos os objetos criados

    # construtor
    def __init__(self, nome, idade, email):
        self.nome = nome
        self._idade = idade  # atributo privado
        self._email = email  # atributo privado
        Pessoa.total_pessoas += 1

    # método para pedir informações do usuário
    def pegar_informacoes(self):
        self.nome = input("Informe seu nome: ")
        self.idade = int(input("Informe sua idade: "))
        self.email = input("Informe seu email: ")

    # método para mostrar informações
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Email: {self.email}")

    # ---------------- property e setter ----------------
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self._idade = valor
        else:
            print("Idade inválida! Mantendo a idade anterior.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" in valor:  # simples validação de email
            self._email = valor
        else:
            print("Email inválido! Mantendo o email anterior.")

    # ---------------- classmethod ----------------
    @classmethod
    def criar_com_nome(cls, nome):
        # cria pessoa com idade padrão 18 e email vazio
        return cls(nome, idade=int(input("informe idade: ")), email=input("infrome email: "))

    # ---------------- staticmethod ----------------
    @staticmethod
    def mostrar_total_pessoas():
        print(f"Total de pessoas criadas: {Pessoa.total_pessoas}")


# criando uma pessoa pedindo todas as informações
p1 = Pessoa(nome="", idade="", email="")
p1.pegar_informacoes()
p1.mostrar_informacoes()

# alterando atributos usando setters
p1.idade = int(input("informe nova idade: "))
p1.email = input("informe novo email: ")
p1.mostrar_informacoes()

# criando uma pessoa com construtor alternativo (classmethod)
p2 = Pessoa.criar_com_nome(input("informe nome: "))
p2.mostrar_informacoes()

# mostrando total de pessoas (staticmethod)
Pessoa.mostrar_total_pessoas()
