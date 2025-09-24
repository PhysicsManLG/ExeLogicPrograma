from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome=nome
        self.idade=idade
        self.comendo=comendo
        self.falando=falando

    #verificar se está comendo
    def verificar_comer(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo")
        else:
            print(f"{self.nome} está comendo")
    
    #verificar se está falando
    def verificar_falar(self):
        if self.falando == False:
            print(f"{self.nome} não está falando")
        else:
            print(f"{self.nome} está falando")
    
    #começar a comer
    def comer(self):
        if self.falando:
            print(f"{self.nome} está falando, não pode comer agora.")
            return
        
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return
        
        print(f"agora {self.nome} começou a comer")
        self.comendo = True

    #parar de comer
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo. Poder falar agora")
            return
        
        print(f"{self.nome} parou de comer")
        self.comendo = False
    
    #começar a falar
    def falar(self):
        if self.comendo:
            print(f"{self.nome} está comendo, não pode falar agora")
            return
        
        if self.falando:
            print(f"{self.nome} já está falando")
            return
        
        self.falando = True
        print(f"Agora {self.nome} começou a falar")
    
    #parar de falar
    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando. Pode comer agora")
            return
        
        print(f"{self.nome} parou de falar")
        self.falando = False
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


pessoa1 = Pessoa('Guts', 31)
pessoa2 = Pessoa('casca', 29)