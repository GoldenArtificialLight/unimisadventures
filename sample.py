# teste para display de cenario

from os import system
from time import sleep

import numpy as np

PLAYER = '§'
TILE = '.'
TRAIL = '~'

TRAILSIZE_LIMIT = 3
trailsize = 0
trail_pos = []

posicao = []
cenario = np.empty([9, 9], str)
cenario.fill(TILE)
print(cenario)
cenario[4][4] = PLAYER


for i in range(cenario.shape[0]):
    for j in range(cenario.shape[1]):
        if cenario[i][j] == PLAYER:
            posicao = [i, j]

def mostrar_cenário():
    for row in cenario:
        print(*row)


def atualizar_posicao(y, x):
    cenario[posicao[0]][posicao[1]] = TRAIL

    trail_pos.append([posicao[0], posicao[1]])
    global trailsize; trailsize += 1
    if trailsize >= TRAILSIZE_LIMIT:
        last_trail = trail_pos.pop(0)
        cenario[last_trail[0]][last_trail[1]] = TILE

    posicao[0] += y # linha
    posicao[1] += x # coluna

    cenario[posicao[0]][posicao[1]] = PLAYER

system('color 0f')

while True:
    system('cls')
    mostrar_cenário()
    match input('\nd -> direita \ne -> esquerda \nc -> acima \nb -> abaixo \n>>>'):
        case 'd':
            atualizar_posicao(0, 1)
        case 'e':
            atualizar_posicao(0, -1)
        case 'c':
            atualizar_posicao(-1, 0)
        case 'b':
            atualizar_posicao(1, 0)
        case 's':
            break
        case _:
            print('No no')
            sleep(1)
            system('cls')



