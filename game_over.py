# Importando bibliotecas usadas
import pygame
from os import path

# Importando variáveis de outros arquivos
from config import CENARIOS_DIR, PRETO, FPS, INICIO, FECHAR, WIDTH, HEIGHT, BRANCO, ALFABETO, MORTO, NOMES_PONTUACAO
from assets import load_assets, SCORE_FONT

# Criando função da tela de game over
def game_over(tela, score, SCORES_LISTA):
    
    assets = load_assets()
    state = MORTO

    # Armazena o score, caso ele esteja no top 5
    if score > min(SCORES_LISTA):

        # Atualizando lista de scores
        SCORES_LISTA.append(score)
        SCORES_LISTA = sorted(SCORES_LISTA)
        SCORES_LISTA = SCORES_LISTA[::-1] # Invertendo ela para posições
        SCORES_LISTA.pop(0)

        # Definindo background para inserir o nome
        background = pygame.image.load(path.join(CENARIOS_DIR, 'colocar_nome.png')).convert()
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        background_rect = background.get_rect()

        # Colocando background
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        nome = ''
        colocar_nome = True
        while colocar_nome:
            for event in pygame.event.get():
                # Verifica se foi fechado
                if event.type == pygame.QUIT:
                    state = FECHAR
                    colocar_nome = False

                # Verifica se clicou com o mouse
                if event.type == pygame.KEYDOWN:
                    # Se clicou enter  
                    if event.key == pygame.K_RETURN:
                        colocar_nome = False
                    elif event.key == pygame.K_BACKSPACE:
                        NOMES_PONTUACAO[nome] = score
                        nome = nome[:-1]
                    else:
                        print(event.key)
                        if event.key >= 97 and event.key <= 122:
                            nome += ALFABETO[event.key - 97]
                    
                    if colocar_nome:
                        tela.fill(PRETO)
                        tela.blit(background, background_rect)
                        text_surface = assets[SCORE_FONT].render("{0}".format(nome), True, BRANCO)
                        text_rect = text_surface.get_rect()
                        text_rect.midtop = (238,  278)
                        tela.blit(text_surface, text_rect)

                        pygame.display.flip()
        
        # Abrindo o  arquivo txt com os scores
        with open('tabela_score.txt', 'a') as arquivo:
            # Lendo cada uma das linhas
            linhas = arquivo.readlines()

            # Separando as informações das linhas
            for linha in linhas:
                linha = linha.split(' - ')
                num = linha[0]

                if num == (SCORES_LISTA.index(score) + 1):
                    # Mudando o nome da pessoa para sua posição na lista
                    linha[1] = '{0} [{1}]'.format(nome, score)             
    
    # Variável para o ajuste de velocidade
    relogio = pygame.time.Clock()

    # Background da tela inicial
    background = pygame.image.load(path.join(CENARIOS_DIR, 'GAME OVER.png')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # ----- Loop principal 
    rodando = True
    while rodando and state != FECHAR:

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
                if 169 <= pos[0] <=322 and 489 <= pos[1] <= 556:
                    state = INICIO
                    rodando = False

        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    # Retornando o estado
    return [state, SCORES_LISTA]

# quadrado para score
# canto superior esquerdo = (74, 134)
# canto inferior direito = (442, 426)

# text_surface = assets[SCORE_FONT].render("{:03d}".format(score), True, AMARELO)
#         text_rect = text_surface.get_rect()
#         text_rect.midtop = (WIDTH / 2,  10)
#         window.blit(text_surface, text_rect)