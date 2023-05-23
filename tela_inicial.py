import pygame
from os import path
from config import CENARIOS_DIR, PRETO, FPS, JOGANDO, FECHAR, WIDTH, HEIGHT


def tela_inicial(tela):
    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    background = pygame.image.load(path.join(CENARIOS_DIR, 'raposa normal.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
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

            rodando2 = True
            tempo_inicial = pygame.time.get_ticks()
            background = pygame.image.load(path.join(CENARIOS_DIR, 'raposa mergulhando.png')).convert()
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            background_rect = background.get_rect()

            while rodando2:
                sec = (pygame.time.get_ticks()-tempo_inicial)/1000
                if sec >= 1:
                    rodando2=False

                #Coloca a imagem seguinte da raposa pulando na água
                tela.blit(background,background_rect)

                #Inverte o display
                pygame.display.flip()


    return state

