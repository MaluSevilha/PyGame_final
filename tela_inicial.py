import pygame
from os import path

from config import CENARIOS_DIR, PRETO, FPS, JOGANDO, FECHAR


def tela_inicial(tela):
    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    background = pygame.image.load(path.join(CENARIOS_DIR, 'raposa normal.png')).convert()
    background = pygame.transform.scale2x(background)
    background_rect = background.get_rect()

    rodando = True
    while rodando:
        #Define um estado inicial 
        state = FECHAR

        # Ajusta a velocidade do jogo.
        relogio.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = FECHAR
                rodando = False

            if event.type == pygame.KEYUP:
                state = JOGANDO
                rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        if state == JOGANDO:

            #Coloca a imagem seguinte da raposa pulando na água
            background = pygame.image.load(path.join(CENARIOS_DIR, 'raposa mergulhando.png')).convert()
            background_rect = background.get_rect()
            tela.blit(background,background_rect)

            #Inverte o display
            pygame.display.flip()


    return state

