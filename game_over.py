import pygame
from os import path

from config import CENARIOS_DIR, PRETO, FPS, INICIO, FECHAR, WIDTH, HEIGHT


def game_over(tela):
    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    background = pygame.image.load(path.join(CENARIOS_DIR, 'GAME OVER.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    rodando = True
    while rodando:

        # Ajusta a velocidade do jogo.
        relogio.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = FECHAR
                rodando = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pos[0]>=155 and pos[0]<=331 and pos[1]>=408 and pos[1]<=493:
                    state = INICIO
                    rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


    return state