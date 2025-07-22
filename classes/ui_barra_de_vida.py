class BarraDeVida():
    def __init__(self, nome):
        self.__nome = nome
        self.__barra = ('< ' + ('# ' * 10) + '>').split(' ')

    def mostrar(self):
        print(f'Vida ({self.__nome}): ', *self.__barra)
    
    def atualizar(self, vida):
        temp = vida - (len(self.__barra) - 2)

        for i in range(-1, temp - 1, -1):
            self.__barra[i-1] = '-'
        for i in range(1, vida + 1):
            self.__barra[i] = '#'
        
        del temp

if __name__ == '__main__':
    barra = BarraDeVida('Player')

    barra.mostrar()
    barra.atualizar(9)
    barra.mostrar()
    barra.atualizar(4)
    barra.mostrar()
    barra.atualizar(10)
    barra.mostrar()
    barra.atualizar(8)
    barra.mostrar()
    barra.atualizar(9)
    barra.mostrar()
