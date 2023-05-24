# Importando bibliotecas necessárias
import pygame
from os import path

# Importando tamanho da tela
from config import WIDTH, HEIGHT

# Importando caminhos
from config import BARRIL_HEIGHT,CENARIOS_DIR, PEIXES_DIR, OBJETOS_DIR, JOGADOR_DIR, FNT_DIR

# Importando tamanho dos objetos
from config import PEIXES_WIDTH, PEIXES_HEIGHT, JOGADOR_WIDTH, JOGADOR_HEIGHT, BARRIL_WIDTH, VIDA_TAM

# Definindo chaves do dicionário assets
# ---- Cenários
BACKGROUND = 'background'

# ---- Imagens: Peixes
PEIXE_IMG = 'peixe_img'
PEIXE_LARANJA_IMG = 'peixe_laranja'
PEIXE_VERDE_IMG = 'peixe_verde'
PEIXE_AZUL_IMG = 'peixe_azul'

# ---- Imagens: Objetos
BARRIL_MARROM_IMG = 'barril_marrom'
BARRIL_LARANJA_IMG = 'barril_laranja'
VIDA_IMG = 'vida_img'

# ---- Imagens: jogador
VARA_IMG = 'vara_img'
LINHA_IMG = 'linha_img'
ANZOL_IMG = 'anzol_img'

# ---- Animação: Jogador
VARA_ANIM = 'vara_anim'

# ---- Fontes
SCORE_FONT = 'score_font'

# ---- Sons
PESCOU_SOUND = 'pescou_sound'
PERDEU_ISCA_SOUND = 'perdeu_isca_sound'
JOGOU_VARA_SOUND = 'jogou_vara_sound'
BACKGROUND_SOUND = 'background_sound'

# ---- Lista de imagens de peixes e obstáculos
LISTA_OBSTACULOS = "imgs_barris"
LISTA_PEIXES = "imgs_peixes"

def load_assets():
    # Criando o dicionário assets e adicionando as imagens à ele
    assets = {}

    assets[LINHA_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'linha.png')).convert_alpha()
    assets[LINHA_IMG] = pygame.transform.scale(assets[LINHA_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[ANZOL_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'anzol.png')).convert_alpha()
    assets[ANZOL_IMG] = pygame.transform.scale(assets[ANZOL_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[BACKGROUND] = pygame.image.load(path.join(CENARIOS_DIR, 'fundo_do_mar.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[PEIXE_LARANJA_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_laranja.png')).convert_alpha()
    assets[PEIXE_LARANJA_IMG] = pygame.transform.scale(assets[PEIXE_LARANJA_IMG],(PEIXES_WIDTH,PEIXES_HEIGHT))

    assets[PEIXE_VERDE_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_verde.png')).convert_alpha()
    assets[PEIXE_VERDE_IMG] = pygame.transform.scale(assets[PEIXE_VERDE_IMG],(PEIXES_WIDTH,PEIXES_HEIGHT))

    assets[PEIXE_AZUL_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_azul.png')).convert_alpha()
    assets[PEIXE_AZUL_IMG] = pygame.transform.scale(assets[PEIXE_AZUL_IMG],(PEIXES_WIDTH,PEIXES_HEIGHT))

    assets[BARRIL_MARROM_IMG] = pygame.image.load(path.join(OBJETOS_DIR, 'barril_marrom.png')).convert_alpha()
    assets[BARRIL_MARROM_IMG] = pygame.transform.scale(assets[BARRIL_MARROM_IMG],(BARRIL_WIDTH,BARRIL_HEIGHT))

    assets[BARRIL_LARANJA_IMG] = pygame.image.load(path.join(OBJETOS_DIR, 'barril_laranja.png')).convert_alpha()
    assets[BARRIL_LARANJA_IMG] = pygame.transform.scale(assets[BARRIL_LARANJA_IMG],(BARRIL_WIDTH,BARRIL_HEIGHT))

    assets[VIDA_IMG] = pygame.image.load(path.join(OBJETOS_DIR, 'coracao.png')).convert_alpha()
    assets[VIDA_IMG] = pygame.transform.scale(assets[VIDA_IMG],(VIDA_TAM, VIDA_TAM))

    # Juntando as imagens dos peixes em uma lista
    IMGS_PEIXES = [assets[PEIXE_LARANJA_IMG], assets[PEIXE_VERDE_IMG],assets[PEIXE_AZUL_IMG]]
    assets[LISTA_PEIXES] = IMGS_PEIXES

    # Juntando as imagens dos barris em uma lista
    IMGS_BARRIS = [assets[BARRIL_LARANJA_IMG], assets[BARRIL_MARROM_IMG]]
    assets[LISTA_OBSTACULOS] = IMGS_BARRIS
    
    #Juntando a fonte do score à ele
    assets[SCORE_FONT] = pygame.font.Font(path.join(FNT_DIR, 'PressStart2P.ttf'), 28)

    # eletrecuta_anim = []
    # for i in range(9):
    #     # Os arquivos de animação são numerados de 00 a 08
    #     filename = path.join(IMG_DIR, 'regularExplosion0{}.png'.format(i))
    #     img = pygame.image.load(filename).convert()
    #     img = pygame.transform.scale(img, (32, 32))
    #     eletrecuta_anim.append(img)
    # assets[VARA_ANIM] = eletrecuta_anim

    # # Carrega os sons do jogo
    # pygame.mixer.music.load(path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    # pygame.mixer.music.set_volume(0.4)
    # assets[PESCOU_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'expl3.wav'))
    # assets[PERDEU_ISCA_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'expl6.wav'))
    # assets[JOGOU_VARA_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'pew.wav'))
    # assets[BACKGROUND_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'pew.wav'))

    return assets



