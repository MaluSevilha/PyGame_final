import pygame
from config import FPS, WIDTH, HEIGHT, JOGANDO, FECHAR, MORTO
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Ship, Meteor, Bullet, Explosion


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_fish = pygame.sprite.Group()
    all_obstaculos = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_fish'] = all_fish
    groups['all_obstaculos'] = all_obstaculos

    # Criando o jogador
    player = Ship(groups, assets)
    all_sprites.add(player)
    # Criando os meteoros
    for i in range(8):
        fish = Meteor(assets)
        all_sprites.add(meteor)
        all_fish.add(meteor)

    keys_down = {}
    score = 0
    lives = 3
    state = JOGANDO
    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
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
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_SPACE:
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        # ----- Gera saídas
        window.fill(PRETO)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        
        # Desenhando meteoros
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state