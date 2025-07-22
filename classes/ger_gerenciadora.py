from abc import ABC
import random as rn
from os import path as pt

import classes as cl

class Gerenciadora(ABC):
    inimigos: dict[str, list[cl.Inimigo]] = {
        'Morcegos': [],
        'Serpentes': []
    }

    @staticmethod
    def setup(jogador_: cl.Jogador, cenario_: cl.Cenario):
        print('Inicializando. . .')
        cl.sleep(cl.random() + 0.5)

        global jogador; jogador = jogador_
        global cenario; cenario = cenario_

        jogador.adicionar_observador(cenario)

        print('Gerando cenário. . .')
        cl.sleep(cl.random() + 0.5)

        print('Tudo pronto!')
        cl.sleep(0.4)
        print('Começando em ', end='')
        for i in range(3, 0, -1):
            cl.sleep(0.28)
            print(f'{i}', end='', flush=True)
            for j in range(3, 0, -1):
                cl.sleep(0.2)
                print('.', end='', flush=True)
        
        cl.sleep(0.5)
    
    @staticmethod
    def update():
        cl.system('cls')

        cenario.atualizar(jogador)
        cenario.renderizar()
        jogador.mostrar_vida()
        
        if jogador.vida <= 0:
            print(f'Você perdeu, {jogador.nome}!')
            return False

        match input('Digite "i" para instruções \n>>>').strip().lower()[-1]:
            case 'd':
                if not jogador.movimentar(1, 0): cl.sleep(1)
            case 'a':
                if not jogador.movimentar(-1, 0): cl.sleep(1)
            case 'w':
                if not jogador.movimentar(0, -1): cl.sleep(1)
            case 's':
                if not jogador.movimentar(0, 1): cl.sleep(1)
            case 'e':
                temp = jogador.verificar_arredores(cenario.cenario)
                if temp:
                    for inimigo in Gerenciadora.inimigos['Morcegos']:
                        if inimigo.x == temp[0][1] and inimigo.y == temp[0][0]:
                            jogador.atacar(inimigo, True)
                    for inimigo in Gerenciadora.inimigos['Serpentes']:
                        if inimigo.x == temp[0][1] and inimigo.y == temp[0][0]:
                            jogador.atacar(inimigo, True)
                    cl.sleep(1)
            case 'q':
                jogador.curar()
                cl.sleep(0.6)
            case 'i':
                path = pt.abspath(pt.join(pt.dirname( __file__ ), '.', 'misc_instrucoes.txt'))
                with open(path, 'r', encoding='utf-8') as instrucoes:
                    for linha in instrucoes:
                        print(linha, end='')
                input('\nPressione ENTER para voltar. . .')
            case 'p':
                return False
            case _:
                print('\nNada aconteceu.')
                cl.sleep(1)
        
        Gerenciadora.atualizar_inimigos()
        
        return True
    

    @staticmethod
    def atualizar_inimigos():
        novo_inimigo = rn.choice([cl.Morcego.criar_morcego(), cl.Serpente.criar_serpente(), None, None, None, None, None])
        if isinstance(novo_inimigo, cl.Morcego):
            Gerenciadora.inimigos['Morcegos'].append(novo_inimigo)
            list(Gerenciadora.inimigos['Morcegos'])[-1].adicionar_observador(cenario)
        elif isinstance(novo_inimigo, cl.Serpente):
            Gerenciadora.inimigos['Serpentes'].append(novo_inimigo)
            list(Gerenciadora.inimigos['Serpentes'])[-1].adicionar_observador(cenario)
        else:
            del novo_inimigo
        
        for inimigo in Gerenciadora.inimigos['Morcegos']:
            if inimigo.vida <= 0:
                print(f'Você derrotou {inimigo.nome}!')
                cenario.cenario[inimigo.y][inimigo.x] = cenario.tiles['chao']
                cl.sleep(1)
                Gerenciadora.inimigos['Morcegos'].remove(inimigo)
            else:
                inimigo.mudar_posicao()
                if inimigo.atacar(jogador, inimigo.verificar_arredores(cenario.cenario)): cl.sleep(0.6)
        for inimigo in Gerenciadora.inimigos['Serpentes']:
            if inimigo.vida <= 0:
                print(f'Você derrotou {inimigo.nome}!')
                cenario.cenario[inimigo.y][inimigo.x] = cenario.tiles['chao']
                cl.sleep(1)
                Gerenciadora.inimigos['Serpentes'].remove(inimigo)
            else:
                inimigo.mudar_posicao()
                if inimigo.atacar(jogador, inimigo.verificar_arredores(cenario.cenario)): cl.sleep(0.6)

