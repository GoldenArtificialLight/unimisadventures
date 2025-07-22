from .inm_inimigo import Inimigo
from random import randint as ri

class Serpente(Inimigo):
    quant_serpentes = 0

    def __init__(self, nome, simbolo, ataque):
        super().__init__(nome, simbolo, ataque, ri(1, 20), ri(1, 9), 3)
    
    def receber_dano(self, dano):
        return super().receber_dano(dano)
    
    @classmethod
    def criar_serpente(cls):
        cls.quant_serpentes += 1
        return Serpente('Serpente', '~', 3)
    
    def __str__(self):
        return self.nome
    
    
    