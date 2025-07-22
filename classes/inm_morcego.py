from abc import ABCMeta
from typing import Any
from .inm_inimigo import Inimigo
from random import randint as ri

class Morcego(Inimigo):
    quant_morcegos = 0

    def __init__(self, nome, simbolo, ataque):
        super().__init__(nome, simbolo, ataque, ri(1, 20), ri(1, 9), 5)
    
    def receber_dano(self, dano):
        return super().receber_dano(dano)
    
    @classmethod
    def criar_morcego(cls):
        cls.quant_morcegos += 1
        return Morcego('Morcego', '^', 2)
    



