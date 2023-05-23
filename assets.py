import pygame
import os
# from config import 


BACKGROUND_IMG = 'background'
PEIXE_IMG = 'peixe_img'
VARA_IMG = 'vara_img'
VARA_ANIM = 'vara_anim'
SCORE_FONT = 'score_font'
PESCOU_SOUND = 'pescou_sound'
PERDEU_ISCA_SOUND = 'perdeu_isca_sound'
JOGOU_VARA_SOUND = 'jogou_vara_sound'
BACKGROUND_SOUND = 'background_sound'


def load_assets():
    assets = {}
    assets[BACKGROUND_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'starfield.png')).convert()
    assets[PEIXE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'meteorBrown_med1.png')).convert_alpha()
    assets[VARA_IMG] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))

    eletrecuta_anim = []
    for i in range(9):
        # Os arquivos de animação são numerados de 00 a 08
        filename = os.path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
        img = pygame.image.load(filename).convert()
        img = pygame.transform.scale(img, (32, 32))
        eletrecuta_anim.append(img)
    assets[VARA_ANIM] = eletrecuta_anim
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[PESCOU_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[PERDEU_ISCA_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[JOGOU_VARA_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    assets[BACKGROUND_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets
