from abc import ABC
import random as rn

import classes as cl

class Inimigo(cl.Entidade, ABC):
    def __init__(self, nome, simbolo, ataque, x, y, vida):
        super().__init__(nome, simbolo)
        self.__vida = vida
        self.__ataque = ataque
        self.__posicao = [y, x]
    
    @property
    def vida(self):
        return self.__vida
    
    def verificar_arredores(self, cenario):
        for i in range(self.y - 1, self.y + 2):
            for j in range(self.x - 1, self.x + 2):
                if cenario[i][j] == '§':
                    return True
        return False

    def atacar(self, jogador, esta_proximo):
        if esta_proximo:
            jogador.receber_dano(self.__ataque)
            print(f'{self.nome} atacou {jogador}!')
            return True
        return False
    
    def __str__(self):
        return self.nome
    
    def receber_dano(self, dano):
        self.__vida -= dano

    def mudar_posicao(self):
        self.movimentar(rn.randint(-1, 1), rn.randint(-1, 1))


