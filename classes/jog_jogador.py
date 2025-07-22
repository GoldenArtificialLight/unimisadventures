import random as rn
import classes as cl

class Jogador(cl.Entidade):
    def __init__(self, nome, simbolo):
        super().__init__(nome, simbolo)

        self.__vida = 10
        self.__barra_de_vida = cl.BarraDeVida(nome)

        self.__posicao = [1, 1]
    
    @property
    def vida(self):
        return self.__vida
    
    def atacar(self, inimigo, esta_proximo):
        if esta_proximo:
            inimigo.receber_dano(rn.randint(3, 5))
            print(f'{self.nome} atacou {inimigo}!')
        else:
            print('Não há nada para atacar.')
    
    def verificar_arredores(self, cenario):
        for i in range(self.y - 1, self.y + 2):
            for j in range(self.x - 1, self.x + 2):
                if cenario[i][j] == '^' or cenario[i][j] == '~':
                    return [i, j], True
        return False
    
    def curar(self):
        self.__vida = min(self.__vida + 5, 10)
        self.__barra_de_vida.atualizar(self.__vida)
        print('Curado!')

    def receber_dano(self, dano):
        self.__vida = max(self.__vida - dano, 0)
        self.__barra_de_vida.atualizar(self.__vida)
    
    def mostrar_vida(self):
        self.__barra_de_vida.mostrar()
    
    def __str__(self) -> str:
        return self.nome
