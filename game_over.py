# Importando bibliotecas usadas
import pygame
from os import path

# Importando variáveis de outros arquivos
from config import CENARIOS_DIR, PRETO, FPS, INICIO, FECHAR, WIDTH, HEIGHT

# Criando função da tela de game over
def game_over(tela, score, SCORES_LISTA):

    # Armazena o score, caso ele esteja no top 5
    if score > min(SCORES_LISTA):
        SCORES_LISTA.append(score)
        SCORES_LISTA = sorted(SCORES_LISTA)
        SCORES_LISTA.pop(0)
    
    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    background = pygame.image.load(path.join(CENARIOS_DIR, 'GAME OVER.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # ----- Loop principal 
    rodando = True
    while rodando:

        # Ajusta a velocidade do jogo.
        relogio.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc)
        for event in pygame.event.get():
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                state = FECHAR
                rodando = False

            # Verifica se clicou com o mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Encontra a posição que clicou
                pos = pygame.mouse.get_pos()

                # Verificando se clicou no botão de restart
                if pos[0]>=155 and pos[0]<=331 and pos[1]>=408 and pos[1]<=493:
                    state = INICIO
                    rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    # Retornando o estado
    return [state, SCORES_LISTA]