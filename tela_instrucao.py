# Importando bibliotecas
import pygame

# Importando arquivos
from config import HEIGHT ,WIDTH, FPS,  VEL_JOGADOR, JOGANDO, FECHAR, MORTO, PRETO, AMARELO, VERMELHO, INSTRUCAO, SCORE_INICIO
from assets import load_assets, BACKGROUND, SCORE_FONT, POUCOS_PEIXES, MEDIO_PEIXES, CHEIO_PEIXES, ANZOL_IMG,BACKGROUND_INSTRU
from assets import PEIXE_AZUL_IMG, PEIXE_VERDE_IMG, ANZOL_PEIXE_AZUL_IMG, ANZOL_PEIXE_VERDE_IMG, ANZOL_PEIXE_LARANJA_IMG
from assets import PERDEU_ISCA_SOUND, PESCOU_SOUND, CHOQUE_SOUND
from sprites import Peixes, Anzol, Linha, Obstaculos, Vida, Aguaviva

# Fazendo a função da tela do jogo
def instrucao(window):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carregando o dicionário assets
    assets = load_assets()

    # Criando grupos
    all_sprites = pygame.sprite.Group()
    all_obstaculos = pygame.sprite.Group()
    all_vidas = pygame.sprite.Group()
    all_aguaviva = pygame.sprite.Group()
    all_fish = pygame.sprite.Group()

    # Adicionando ao dicionário groups
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_obstaculos'] = all_obstaculos
    groups['all_vidas'] = all_vidas
    groups['all_agua_vivas'] = all_aguaviva
    groups['all_fish'] = all_fish


    # Criando o jogador
    player = Anzol(groups, assets)
    all_sprites.add(player)

    # Criando a Linha
    linha = Linha(groups, assets)
    all_sprites.add(linha)

    # Nível instrução
    level0 = True

    # Nível mais difícil
    level = False

    # Nível máximo
    level2 = False

    # Criando os peixes
    for i in range(2):
        peixe = Peixes(assets)

        # Adcionando aos grupos
        all_sprites.add(peixe)
        all_fish.add(peixe)
    
    for i in range (1):
        obstaculo = Obstaculos(assets)
        all_sprites.add(obstaculo)
        all_obstaculos.add(obstaculo)


    keys_down = {}
    score = 0
    vidas = 3
    state = INSTRUCAO

    # Estado do peixe pescado
    peixe_pescado = False

    # ===== Loop principal =====
    while state != FECHAR and state != MORTO and state!= JOGANDO:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = FECHAR

            # Só verifica o teclado se está no estado de jogo
            if state == INSTRUCAO:

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
        all_sprites.update(level0, level, level2)

        if state == INSTRUCAO:

            if score>=30:
                # Adiciona água viva no nível mais alto
                if len(all_aguaviva) <= 1:
                    if score % 2 == 0:
                        aguaviva = Aguaviva(assets)
                        all_sprites.add(aguaviva)
                        all_aguaviva.add(aguaviva)
            
            # Confere se algum peixe foi pescado
            if peixe_pescado == False:
                pescou = pygame.sprite.spritecollide(player, all_fish, True, pygame.sprite.collide_mask)

            # Passa pelos peixes pescados
            for peixe in pescou:
                # Som de pescou
                assets[PESCOU_SOUND].play()

                # Checando a imagem ligada ao sprite do peixe pescado
                imagem_peixe = peixe.image

                # Alterando a imagem do anzol de acordo com essa
                if peixe.image == assets[PEIXE_AZUL_IMG]:
                    IMAGEM_ANZOL = assets[ANZOL_PEIXE_AZUL_IMG]
                elif peixe.image == assets[PEIXE_VERDE_IMG]:
                    IMAGEM_ANZOL = assets[ANZOL_PEIXE_VERDE_IMG]
                else:
                    IMAGEM_ANZOL = assets[ANZOL_PEIXE_LARANJA_IMG]
                
                # Barulho do peixe sendo pescado

                # Muda a variável do peixe pescado
                peixe_pescado = True
                player.update2(peixe_pescado, IMAGEM_ANZOL, assets)

                # Garante que só um peixe seja pescado por vez
                pescou = []
                
                # Repondo os peixes pescados
                peixe_novo = Peixes(assets)
                all_sprites.add(peixe_novo)
                all_fish.add(peixe_novo)
            
            # Cria lista com colisões com barril
            atingiu = pygame.sprite.spritecollide(player, all_obstaculos, True, pygame.sprite.collide_mask)

            # Passa por cada hit com barril
            for hit in atingiu:
                # Anzol Pisca Dano
                player.animate()

                # Barulho de barril quebrando
                assets[PERDEU_ISCA_SOUND].play()

                # Se peixe estiver no anzol
                if peixe_pescado == True:
                    # Não perde uma vida, mas perde o peixe
                    peixe_pescado = False
                    IMAGEM_ANZOL = assets[ANZOL_IMG]
                    player.update2(peixe_pescado, IMAGEM_ANZOL, assets)
                else:
                    # Perde uma vida
                    vidas -= 1

                # Repondo os barris atingidos
                barril_novo = Obstaculos(assets)
                all_sprites.add(barril_novo)
                all_obstaculos.add(barril_novo)

            # Confere choques com águas vivas
            choque = pygame.sprite.spritecollide(player, all_aguaviva, True, pygame.sprite.collide_mask)

            # Confere cada contato com águas vivas
            for agua_viva in choque:
                # Barulho de choque 
                assets[CHOQUE_SOUND].play()
                # Animação
                linha.animate()
                
                # Se peixe estiver no anzol 
                if peixe_pescado == True:
                    # Não perde duas vidas, mas perde o peixe
                    peixe_pescado = False
                    IMAGEM_ANZOL = assets[ANZOL_IMG]
                    player.update2(peixe_pescado, IMAGEM_ANZOL, assets)
                else:
                    # Perde duas vidas
                    vidas -= 2

                # Repondo as águas vivas atingidas
                aguaviva_nova = Aguaviva(assets)
                all_sprites.add(aguaviva_nova)
                all_obstaculos.add(aguaviva_nova)
            
            # Confere se o jogador pegou uma vida
            pegou_vida = pygame.sprite.spritecollide(player, all_vidas, True, pygame.sprite.collide_mask)

            # Adiciona cada vida pega as vidas do jogador
            for vida_pega in pegou_vida:
                vidas += 1
            
            # Se tiver pego um peixe
            if peixe_pescado == True:
                # Confere se deixou na rede de pesca
                if player.rect.y < -400:
                    score += 1
                    # Atualiza imagem do jogador
                    peixe_pescado = False
                    IMAGEM_ANZOL = assets[ANZOL_IMG]
                    player.update2(peixe_pescado, IMAGEM_ANZOL, assets)

        # ----- Gera saídas
        window.fill(PRETO)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))

        
        window.blit(assets[BACKGROUND_INSTRU], (0,0))
            
        # Desenhando peixes
        all_sprites.draw(window)

        # Desenhando o score
        #text_surface = assets[SCORE_FONT].render("{:03d}".format(score), True, AMARELO)
        #text_rect = text_surface.get_rect()
        #text_rect.midtop = (WIDTH / 2,  10)
        #window.blit(text_surface, text_rect)

        # Desenhando as vidas
        #text_surface = assets[SCORE_FONT].render(chr(9829) * vidas, True, VERMELHO)
        #text_rect = text_surface.get_rect()
        #text_rect.bottomleft = (10, HEIGHT - 10)
        #window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

        # Verifica se já fez o score necessário para iniciar o jo
        if score == SCORE_INICIO:
            state = JOGANDO

    return state