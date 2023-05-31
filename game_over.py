# Importando bibliotecas usadas
import pygame
from os import path

# Importando variáveis de outros arquivos
from config import CENARIOS_DIR, PRETO, FPS, INICIO, FECHAR, WIDTH, HEIGHT, BRANCO, ALFABETO, MORTO, NOMES_PONTUACAO
from assets import load_assets, SCORE_FONT, SCORE_FONT_TABELA, toca_musica 

# Criando função da tela de game over
def game_over(tela, score, SCORES_LISTA):
    
    assets = load_assets()
    state = MORTO
    
    # Toca música do game over
    toca_musica('assets/sons/som_game_over.mp3')

    # Armazena o score, caso ele esteja no top 5
    if score > min(SCORES_LISTA):

        # Atualizando lista de scores
        SCORES_LISTA.append(score)
        SCORES_LISTA = sorted(SCORES_LISTA)
        SCORES_LISTA = SCORES_LISTA[::-1] # Invertendo ela para posições
        SCORES_LISTA.remove(min(SCORES_LISTA))

        # Definindo background para inserir o nome
        background = pygame.image.load(path.join(CENARIOS_DIR, 'colocar_nome.png')).convert()
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        background_rect = background.get_rect()

        # Colocando background
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

        #Cria variável para o nome
        nome = ''

        # Define variável para quando jogador está digitando
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
                        NOMES_PONTUACAO[nome] = score
                        colocar_nome = False
                    
                    # Se clicou backspace
                    elif event.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]
                    
                    # Se clicou qualquer outra tecla
                    else:
                        # Se essa tecla for uma letra
                        if event.key >= 97 and event.key <= 122:
                            nome += ALFABETO[event.key - 97]
                        
                        # Se essa tecla for um espaço
                        elif event.key == pygame.K_SPACE:
                            nome += ' '
                        
                        # Se essa tecla for um número
                        elif 48 <= event.key <= 57:
                            nome += str(event.key - 48) 
                    
                    # Se não tiver dado enter
                    if colocar_nome:
                        # Atualiza nome do jogador na tela (letra por letra)
                        tela.fill(PRETO)
                        tela.blit(background, background_rect)
                        text_surface = assets[SCORE_FONT].render("{0}".format(nome), True, BRANCO)
                        text_rect = text_surface.get_rect()
                        text_rect.midtop = (238,  278)
                        tela.blit(text_surface, text_rect)

                        pygame.display.flip()
        
        # Lista com as linhas modificadas do score
        novas_linhas = []

        # Listas com todos os scores dos jogadores e nomes
        todos_scores = list(NOMES_PONTUACAO.values())
        todos_nomes = list(NOMES_PONTUACAO.keys())
        ## Orientação pelo índice

        # Lista com os nomes dos 5 melhores jogadores
        nomes_pontuadores = []
        
        # Passando pelas melhores pontuações
        index_score = 0
        while index_score < len(SCORES_LISTA):
            score = SCORES_LISTA[index_score]

            # Se tiver um empate no meio
            if SCORES_LISTA.count(score) >= 2 and score != 0:
                index_ini = todos_scores.index(score)
                index_fim = len(todos_scores) - (todos_scores[::-1].index(score))

                # Quem jogou primeio fica mais bem colocado
                for index_nome in range(index_ini, index_fim): 
                    nome = todos_nomes[index_nome]

                    # Guarda o nome do jogador na lista
                    nomes_pontuadores.append(nome)
                    index_score += 1

            else:
                nome = todos_nomes[todos_scores.index(score)]

                # Guarda o nome do jogador na lista
                nomes_pontuadores.append(nome)
                index_score += 1

        # Reescrevendo o arquivo da tabela
        with open('tabela_score.txt', 'w') as arquivo:
            posicao = 1

            # Escrevendo cada linha
            for nome in nomes_pontuadores:
                # Pegando o nome de cada um
                index_pontuacao = todos_nomes.index(nome)
                score = todos_scores[index_pontuacao]

                # Refazendo a linha
                linha = '{0}º - {1} [{2}] \n'.format(posicao, nome, score)

                # Guardando numa lista a linha
                novas_linhas.append(linha)

                # Indo para o próximo jogador
                posicao += 1
            
            # Escrvendo as linhas no arquivo
            arquivo.writelines(novas_linhas)
        
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
                if 169 <= pos[0] <= 322 and 489 <= pos[1] <= 556:
                    state = INICIO
                    rodando = False

        
        # A cada loop, redesenha o fundo e os sprites
        tela.fill(PRETO)
        tela.blit(background, background_rect)

        # Abertura da tabela para escrever cada linha
        with open('tabela_score.txt', 'r') as arquivo:
            # Fazendo todas as linhas
            linhas = arquivo.readlines()

            # Definindo espaçamento entre as linhas
            pulando_linha = 0

            # Passando por cada linha
            for linha in linhas:
                # Retirando o /n
                linha = linha[:-1]

                # Escrevendo cada uma das pontuações
                text_surface = assets[SCORE_FONT_TABELA].render(linha, True, BRANCO)

                # Retângulo do texto
                text_rect = text_surface.get_rect()

                # Definindo posição do texto                           
                text_rect.midtop = (261,  204 + pulando_linha)   

                # Escrevendo na tela               
                tela.blit(text_surface, text_rect)

                # Aumentando o espaço entre as linhas
                pulando_linha += 30

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