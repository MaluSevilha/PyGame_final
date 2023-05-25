# Importando bibliotecas
import pygame

# Importando arquivos
from config import HEIGHT ,WIDTH, FPS,  VEL_JOGADOR, JOGANDO, FECHAR, MORTO, PRETO, AMARELO, VERMELHO
from assets import load_assets, BACKGROUND, SCORE_FONT, POUCOS_PEIXES, MEDIO_PEIXES, CHEIO_PEIXES
from assets import PEIXE_AZUL_IMG, PEIXE_VERDE_IMG, ANZOL_PEIXE_AZUL_IMG, ANZOL_PEIXE_LARANJA_IMG, ANZOL_PEIXE_VERDE_IMG, ANZOL_IMG
from sprites import Peixes, Anzol, Linha, Obstaculos, Vida, Aguaviva

# Fazendo a função da tela do jogo
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carregando o dicionário assets
    assets = load_assets()

    #Criando imagem do anzol
    IMAGEM_ANZOL = assets[ANZOL_IMG]

    # Criando grupos
    all_sprites = pygame.sprite.Group()
    all_obstaculos = pygame.sprite.Group()
    all_vidas = pygame.sprite.Group()
    all_aguaviva = pygame.sprite.Group()

    # Criando grupos de peixes
    all_fish = pygame.sprite.Group()
    all_orange_fish = pygame.sprite.Group()
    all_blue_fish = pygame.sprite.Group()
    all_green_fish = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_obstaculos'] = all_obstaculos
    groups['all_vidas'] = all_vidas
    groups['all_agua_vivas'] = all_aguaviva

    # Adicionando os grupos de peixes
    groups['all_fish'] = all_fish
    groups['all_green_fish'] = all_green_fish
    groups['all_blue_fish'] = all_blue_fish
    groups['all_orange_fish'] = all_orange_fish

    # Peixes pescados de cada cor
    pescados_azul = 0
    pescados_laranja = 0
    pescados_verde = 0


    # Criando o jogador
    player = Anzol(groups, assets)
    all_sprites.add(player)

    # Criando a Linha
    linha = Linha(groups, assets)
    all_sprites.add(linha)

    # Nível mais difícil
    level = False

    # Nível máximo
    level2 = False

    # Criando os peixes
    for i in range(3):
        peixe = Peixes(assets)

        #Conferindo cor do peixe e o adicionando ao grupo
        imagem_peixe = peixe.image
        if imagem_peixe == assets[PEIXE_AZUL_IMG]:
            all_blue_fish.add(peixe)
        elif imagem_peixe == assets[PEIXE_VERDE_IMG]:
            all_green_fish.add(peixe)
        else:
            all_orange_fish.add(peixe)

        # Adcionando aos demais grupos
        all_sprites.add(peixe)
        all_fish.add(peixe)
    
    # Criando obstáculos
    for i in range (2):
        obstaculo = Obstaculos(assets)

        # Adicionado aos grupos
        all_sprites.add(obstaculo)
        all_obstaculos.add(obstaculo)

    # Variaáveis que serão utilizadas
    keys_down = {}          # Teclas pressionadas
    score = 0               # Score do jogador (quantos peixes foram pescados)
    vidas = 3               # Vidas do jogados
    state = JOGANDO         # Estado do jogo

    # Estado do peixe pescado
    peixe_pescado = False

    # ===== Loop principal =====
    # pygame.mixer.music.play(loops=-1)
    while state != FECHAR and state != MORTO:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = FECHAR

            # Só verifica o teclado se está no estado de jogo
            if state == JOGANDO:

                # Verifica se apertou alguma tecla
                if event.type == pygame.KEYDOWN:

                    # Dependendo da tecla, altera a velocidade do anzol e da linha
                    keys_down[event.key] = True     # Adiciona ao dicio de teclas

                    # Verificando a tecla apertada
                    if event.key == pygame.K_UP:
                        player.speedy -= VEL_JOGADOR
                        linha.speedy -= VEL_JOGADOR
                    if event.key == pygame.K_DOWN:
                        player.speedy += VEL_JOGADOR
                        linha.speedy += VEL_JOGADOR
                    
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:

                    # Dependendo da tecla, altera a velocidade do anzol e da linha
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_UP:
                            player.speedy += VEL_JOGADOR
                            linha.speedy += VEL_JOGADOR
                        if event.key == pygame.K_DOWN:
                            player.speedy -= VEL_JOGADOR
                            linha.speedy -= VEL_JOGADOR
                        
    
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos sprites
        all_sprites.update(level, level2)

        if state == JOGANDO:
            
            # ----- GRAUS DE DIFICULDADE
            # Define se aumenta o nível para a velocidade do barril (2 níveis de dificuldade)
            if score>= 15:
                level = True    # Nível mais difícil
            else: 
                level = False

            if score >= 45:
                level2 = True   # Nível impossível
            else:
                level2 = False

            # Aumenta número de obstáculos a partir de determinada pontuação
            if score >= 20:
                if len(all_obstaculos) <= 2:
                    barril = Obstaculos(assets)
                    all_obstaculos.add(barril)
                    all_sprites.add(barril)

            if score >= 30:
                # Adiciona água viva no nível mais alto
                if len(all_aguaviva) <= 1:
                    if score % 2 == 0:
                        aguaviva = Aguaviva(assets)
                        all_sprites.add(aguaviva)
                        all_aguaviva.add(aguaviva)
            
            # Se não tiver pescado um peixe
            if peixe_pescado == False:
                #Lista de colisão com peixes de determinadas cores
                pescou_azul = pygame.sprite.spritecollide(player, all_blue_fish, False, pygame.sprite.collide_mask)
                pescou_verde = pygame.sprite.spritecollide(player, all_green_fish, False, pygame.sprite.collide_mask)
                pescou_laranja = pygame.sprite.spritecollide(player, all_orange_fish, False, pygame.sprite.collide_mask)

                #Lista de colisão com todos os peixes
                pescou = pygame.sprite.spritecollide(player, all_fish, True, pygame.sprite.collide_mask)

                #Para cada peixe pescado
                for peixe in pescou:
                    # Barulho do peixe sendo pescado

                    # Muda a variável do peixe pescado
                    peixe_pescado = True

                    # Confere a cor do peixe pescado
                    if (len(pescou_azul) != 0 and pescados_azul == 0) or (len(pescou_azul) - pescados_azul != 0):
                        IMAGEM_ANZOL = assets[ANZOL_PEIXE_AZUL_IMG]
                        pescados_azul += 1
                    elif (len(pescou_verde) != 0 and pescados_verde == 0) or (len(pescou_verde) - pescados_verde != 0):
                        IMAGEM_ANZOL = assets[ANZOL_PEIXE_VERDE_IMG]
                        pescados_verde += 1
                    else:
                        IMAGEM_ANZOL = assets[ANZOL_PEIXE_LARANJA_IMG]
                        pescados_laranja += 1

                    # Atualiza a imagem do azol com o peixe da cor que pescou
                    player.update2(peixe_pescado, IMAGEM_ANZOL, assets)

                    # Delimita que um peixe pode ser pescado por vez
                    pescou = []
                    pescou_laranja = []
                    pescou_verde = []
                    pescou_azul = []
                
                    # Repondo os peixes pescados
                    peixe_novo = Peixes(assets)

                    #Conferindo cor do peixe novo e o adicionando ao grupo
                    imagem_peixe = peixe.image
                    if peixe.image == assets[PEIXE_AZUL_IMG]:
                        all_blue_fish.add(peixe)
                    elif peixe.image == assets[PEIXE_VERDE_IMG]:
                        all_green_fish.add(peixe)
                    else:
                        all_orange_fish.add(peixe)

                    # Adicionando-o aos outros grupos
                    all_sprites.add(peixe_novo)
                    all_fish.add(peixe_novo)
                
                # Se Pontuação divisível por 10: +1 vida passa
                if score % 10 == 0 and vidas <= 3 and score > 0:
                    vida_nova = Vida(assets)

                    # Adicionando aos grupos
                    all_sprites.add(vida_nova)
                    all_vidas.add(vida_nova)
            
            # Lista com colisões do player com os obstáculos
            atingiu = pygame.sprite.spritecollide(player, all_obstaculos, True, pygame.sprite.collide_mask)

            for hit in atingiu:
                # Barulho de barril quebrando

                # Se peixe estiver no anzol 
                if peixe_pescado == True:
                    # Perde o peixe, mas não uma vida
                    peixe_pescado = False
                    IMAGEM_ANZOL = assets[ANZOL_IMG]
                    player.update2(peixe_pescado, IMAGEM_ANZOL, assets)
                else:
                    # Perde uma vida
                    vidas -= 1

                # Repondo os barris colididos
                barril_novo = Obstaculos(assets)

                # Adicionando-o aos grupos
                all_sprites.add(barril_novo)
                all_obstaculos.add(barril_novo)

            # Listacom colisões com água vivas
            choque = pygame.sprite.spritecollide(player, all_aguaviva, True, pygame.sprite.collide_mask)
            
            for choq in choque:
                # Barulho de choque 

                # Animação

                # Se peixe estiver no anzol 
                if peixe_pescado == True:
                    # Perde o peixe, mas não a vida
                    peixe_pescado = False
                    IMAGEM_ANZOL = assets[ANZOL_IMG]
                    player.update2(peixe_pescado, IMAGEM_ANZOL, assets)
                else:
                    # Perde duas vidas
                    vidas -= 2

                # Repondo as águas vivas colididas
                aguaviva_nova = Aguaviva(assets)
                all_sprites.add(aguaviva_nova)
                all_obstaculos.add(aguaviva_nova)
            
            # Lista de colisões do player com vidas
            pegou_vida = pygame.sprite.spritecollide(player, all_vidas, True, pygame.sprite.collide_mask)

            # Se pegou uma vida
            for vida_pega in pegou_vida:
                vidas += 1
            
            # Se tiver pescado um peixe
            if peixe_pescado == True:
                # Se tiver levado-o para a rede
                if player.rect.y<-400:
                    score += 1

                    # Atualiza a imagem para o anzol vazio
                    peixe_pescado = False
                    IMAGEM_ANZOL = assets[ANZOL_IMG]
                    player.update2(peixe_pescado, IMAGEM_ANZOL, assets)
            

        # Confere se morreu
        if vidas == 0:
            state = MORTO   

        # ----- Gera saídas
        window.fill(PRETO)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))

        # Altera o fundo dependendo do score 
        if score>=5:
            window.blit(assets[POUCOS_PEIXES], (0,0))
        if score>= 15:
            window.blit(assets[MEDIO_PEIXES], (0,0))
        if score>= 30:
            window.blit(assets[CHEIO_PEIXES],(0,0))

        # Desenhando peixes
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:03d}".format(score), True, AMARELO)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * vidas, True, VERMELHO)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state