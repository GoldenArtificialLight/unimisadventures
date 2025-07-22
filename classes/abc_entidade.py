from abc import ABC

import classes as cl

class Entidade(ABC):
    observadores = []

    def __init__(self, nome: str, simbolo: str):
        self.__nome: str = nome
        self.__SIMBOLO: str = simbolo
        self.__posicao = [1, 1]
        self.__prev_y = self.__posicao[0]
        self.__prev_x = self.__posicao[1]
        
    
    @property
    def x(self):
        return self.__posicao[1]
    
    @property
    def y(self):
        return self.__posicao[0]
    
    @property
    def simbolo(self):
        return self.__SIMBOLO
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def prev_x(self):
        return self.__prev_x
    
    @property
    def prev_y(self):
        return self.__prev_y
    
    def movimentar(self, x, y):
        if 0 < self.__posicao[0] + y < 10 and 0 < self.__posicao[1] + x < 21:
            self.__posicao[0] += y # linha
            self.__posicao[1] += x # coluna

            self.notificar()

            self.__prev_y = self.__posicao[0]
            self.__prev_x = self.__posicao[1]

            return True
        else:
            print('\nHá uma parede aqui.') if type(self) == cl.Jogador else None
            return False
    
    def atacar(self):
        pass
    
    def receber_dano(self):
        pass

    def adicionar_observador(self, observador):
        Entidade.observadores.append(observador)

    def notificar(self):
        for observador in self.observadores:
            observador.atualizar(self)

