import numpy as np

# from .inter_observador import Observador
import classes.inter_observador as i

class Cenario(i.Observador):
    def __init__(self):
        self.__tiles = {
            'chao': '.',
            'parede_v': '|', # parede vertical (laterais)
            'parede_h': '—' # parede horizontal
        }

        # cria o cenário e o preenche com o chão
        self.__cenario = np.empty([11, 22], str)
        self.__cenario.fill(self.__tiles['chao'])
        # faz as duas paredes: a inferior e a superior
        self.__cenario[0], = self.__tiles['parede_h']
        self.__cenario[-1] = self.__tiles['parede_h']

        self.__num_linhas = self.__cenario.shape[0]
        self.__num_colunas = self.__cenario.shape[1]
        for i in range(self.__num_linhas):
            for j in range(self.__num_colunas):
                if (j == 0 or j == (self.__num_colunas - 1)) and (0 < i < (self.__num_linhas -1)):
                    self.__cenario[i][j] = self.__tiles['parede_v']
    
    @property
    def tiles(self):
        return self.__tiles

    @property
    def cenario(self):
        return self.__cenario
    
    def renderizar(self) -> None:
        for row in self.__cenario:
            print(*row)
        
    
    def atualizar(self, *entidade):
        for ent in entidade:
            self.__cenario[ent.prev_y][ent.prev_x] = self.__tiles['chao']
            self.__cenario[ent.y][ent.x] = ent.simbolo


if __name__ == '__main__':
    import jog_jogador as j

    jogador = j.Jogador('A', '§')
    cenario = Cenario()

    jogador.adicionar_observador(cenario)

    cenario.atualizar(jogador)
    cenario.renderizar()
    jogador.movimentar(1, 0)
    cenario.renderizar()
    jogador.movimentar(1, 0)
    cenario.renderizar()
    jogador.movimentar(0, 1)
    cenario.renderizar()

