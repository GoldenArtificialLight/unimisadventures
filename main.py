import classes as cl

if __name__ == '__main__':
    nome = input('Digite seu nome: ')
    cl.system('cls')

    try:
        cl.Gerenciadora.setup(cl.Jogador(nome, '§'), cl.Cenario())
    except Exception as error:
        print(f'Erro inesperado ao inicializar: ', error)
        cl.sleep(1)

    while True:
        try:
            if not cl.Gerenciadora.update(): break
        except Exception as error:
            print(f'Erro inesperado durante o jogo: ', error)
            cl.sleep(1)




