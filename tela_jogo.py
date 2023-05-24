import pygame
from config import HEIGHT ,WIDTH, FPS,  VEL_JOGADOR, JOGANDO, FECHAR, MORTO, PRETO, AMARELO, VERMELHO
from assets import load_assets, BACKGROUND, SCORE_FONT, POUCOS_PEIXES,MEDIO_PEIXES,CHEIO_PEIXES
from sprites import Peixes, Anzol, Linha, Obstaculos, Vida


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando grupos
    all_sprites = pygame.sprite.Group()
    all_fish = pygame.sprite.Group()
    all_obstaculos = pygame.sprite.Group()
    all_vidas = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_fish'] = all_fish
    groups['all_obstaculos'] = all_obstaculos
    groups['all_vidas'] = all_vidas

    # Criando o jogador
    player = Anzol(groups, assets)
    all_sprites.add(player)

    # Criando a Linha
    linha = Linha(groups, assets)
    all_sprites.add(linha)

    # Criando os peixes
    for i in range(3):
        peixe = Peixes(assets)
        all_sprites.add(peixe)
        all_fish.add(peixe)
    
    for i in range (2):
        obstaculo = Obstaculos(assets)
        all_sprites.add(obstaculo)
        all_obstaculos.add(obstaculo)

    keys_down = {}
    score = 0
    vidas = 3
    state = JOGANDO

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

                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:

                    # Dependendo da tecla, altera a velocidade do anzol e da linha.
                    keys_down[event.key] = True
                    if event.key == pygame.K_UP:
                        player.speedy -= VEL_JOGADOR
                        linha.speedy -= VEL_JOGADOR
                    if event.key == pygame.K_DOWN:
                        player.speedy += VEL_JOGADOR
                        linha.speedy += VEL_JOGADOR
                    
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:

                    # Dependendo da tecla, altera a velocidade do anzol e da linha.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_UP:
                            player.speedy += VEL_JOGADOR
                            linha.speedy += VEL_JOGADOR
                        if event.key == pygame.K_DOWN:
                            player.speedy -= VEL_JOGADOR
                            linha.speedy -= VEL_JOGADOR

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        if state == JOGANDO:
            if peixe_pescado==False:
                pescou = pygame.sprite.spritecollide(player, all_fish, True, pygame.sprite.collide_mask)

            for peixe in pescou:
                # Barulho do peixe sendo pescado

                # Animação

                # Muda a variável do peixe pescado
                peixe_pescado = True
                player.update2(peixe_pescado,assets)
                
                # Repondo os peixes pescados
                peixe_novo = Peixes(assets)
                all_sprites.add(peixe_novo)
                all_fish.add(peixe_novo)
            
                score += 1

                if score % 10 == 0 and vidas<=3:
                    vida_nova = Vida(assets)
                    all_sprites.add(vida_nova)
                    all_vidas.add(vida_nova)
            
            atingiu = pygame.sprite.spritecollide(player, all_obstaculos, True, pygame.sprite.collide_mask)

            for hit in atingiu:
                # Barulho de barril quebrando

                # Se peixe estiver no anzol 
                if peixe_pescado == True:
                    peixe_pescado = False
                    player.update2(peixe_pescado,assets)
                else:
                    vidas -= 1

                # Repondo os barris atingidos
                barril_novo = Obstaculos(assets)
                all_sprites.add(barril_novo)
                all_obstaculos.add(barril_novo)
        
            
            pegou_vida = pygame.sprite.spritecollide(player, all_vidas, True, pygame.sprite.collide_mask)

            for vida_pega in pegou_vida:
                vidas += 1

        if peixe_pescado == True:
            if player.rect.y>=96:
                peixe_pescado = False
                player.update2(peixe_pescado,assets)
                score += 1 
            

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

        #   Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * vidas, True, VERMELHO)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state