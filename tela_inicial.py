# Importando bibliotecas necessárias
import pygame
from os import path

# Importando variáveis de outros arquivo
from config import CENARIOS_DIR, PRETO, FPS, JOGANDO, FECHAR, WIDTH, HEIGHT, SND_DIR, INSTRUCAO
from assets import toca_musica

# Função principal
def tela_inicial(tela):
    # Toca a música inicial
    toca_musica('assets/sons/Club Penguin Music - Ice Fishing.mp3')

    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    background = pygame.image.load(path.join(CENARIOS_DIR, 'raposa normal.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # ----- Loop principal
    pygame.mixer.music.play(loops = -1)
    
    rodando = True
    while rodando:
        # Define um estado inicial 
        state = FECHAR

        # Ajusta a velocidade do jogo.
        relogio.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = FECHAR
                rodando = False
            
            # Verifica se uma tecla foi pressionada
            if event.type == pygame.KEYUP:
                state = INSTRUCAO
                rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        # Confere se é para mudar de tela
        if state == INSTRUCAO:

            rodando2 = True
            tempo_inicial = pygame.time.get_ticks()
            background = pygame.image.load(path.join(CENARIOS_DIR, 'raposa mergulhando.png')).convert()
            background = pygame.transform.scale(background, (WIDTH + 20, HEIGHT - 12))
            background_rect = background.get_rect()

            # Cria um loop para rodar segunda tela de início
            while rodando2:
                # Tempo de espera
                sec = (pygame.time.get_ticks()-tempo_inicial)/1000

                # Quando passa o tempo
                if sec >= 1:
                    rodando2 = False

                # Coloca a imagem seguinte da raposa pulando na água
                tela.blit(background,background_rect)

                # Inverte o display
                pygame.display.flip()

    # Retorna o estado
    return state
