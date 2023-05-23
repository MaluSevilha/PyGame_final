import pygame
from os import path
from config import PEIXES_WIDTH, PEIXES_HEIGHT, CENARIOS_DIR, PEIXES_DIR
# from config import 


BACKGROUND = 'background'
PEIXE_IMG = 'peixe_img'
VARA_IMG = 'vara_img'
VARA_ANIM = 'vara_anim'
SCORE_FONT = 'score_font'
PESCOU_SOUND = 'pescou_sound'
PERDEU_ISCA_SOUND = 'perdeu_isca_sound'
JOGOU_VARA_SOUND = 'jogou_vara_sound'
BACKGROUND_SOUND = 'background_sound'
PEIXE_LARANJA_IMG = 'peixe_laranja'
PEIXE_VERDE_IMG = 'peixe_verde'


def load_assets():
    #Criando o dicionário assets e adicionando as imagens à ele
    assets = {}

    assets[VARA_IMG] = pygame.transform.scale(assets['meteor_img'], (METEOR_WIDTH, METEOR_HEIGHT))

    assets[BACKGROUND] = pygame.image.load(path.join(CENARIOS_DIR, 'Fundo_do_mar.jpg')).convert()

    assets[PEIXE_LARANJA_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_laranja.jpg')).convert()
    assets[PEIXE_LARANJA_IMG] = pygame.transform.scale(assets[PEIXE_LARANJA_IMG],(PEIXES_WIDTH,PEIXES_HEIGHT))

    assets[PEIXE_VERDE_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_verde.jpg')).convert()
    assets[PEIXE_VERDE_IMG] = pygame.transform.scale(assets[PEIXE_LARANJA_IMG],(PEIXES_WIDTH,PEIXES_HEIGHT))

    #juntando as imagens dos peixes em uma lista
    IMGS_PEIXES = [assets[PEIXE_LARANJA_IMG], assets[PEIXE_VERDE_IMG]]
    assets["imgs_peixes"] = IMGS_PEIXES

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
    pygame.mixer.music.load(path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[PESCOU_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'expl3.wav'))
    assets[PERDEU_ISCA_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'expl6.wav'))
    assets[JOGOU_VARA_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'pew.wav'))
    assets[BACKGROUND_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'pew.wav'))

    return assets
