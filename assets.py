# Importando bibliotecas necessárias
import pygame
from os import path

# Importando tamanho da tela
from config import WIDTH, HEIGHT

# Importando caminhos
from config import BARRIL_HEIGHT,CENARIOS_DIR, PEIXES_DIR, OBJETOS_DIR, JOGADOR_DIR, FNT_DIR, SND_DIR, ANIM_DIR

# Importando tamanho dos objetos
from config import PEIXES_WIDTH, PEIXES_HEIGHT, JOGADOR_WIDTH, JOGADOR_HEIGHT, BARRIL_WIDTH, VIDA_TAM, AGUA_VIVA_TAM

# Definindo chaves do dicionário assets
# ---- Cenários
BACKGROUND = 'background'
BACKGROUND_INSTRU = 'background_instrucoes'
POUCOS_PEIXES = 'poucos_peixes'
MEDIO_PEIXES = 'médio_peixes'
CHEIO_PEIXES = 'cheio_peixes'

# ---- Imagens: Peixes
PEIXE_IMG = 'peixe_img'
PEIXE_LARANJA_IMG = 'peixe_laranja'
PEIXE_VERDE_IMG = 'peixe_verde'
PEIXE_AZUL_IMG = 'peixe_azul'

# ---- Imagens: Objetos
BARRIL_MARROM_IMG = 'barril_marrom'
BARRIL_LARANJA_IMG = 'barril_laranja'
VIDA_IMG = 'vida_img'
AGUA_VIVA_IMG = 'agua viva'

# ---- Imagens: jogador
VARA_IMG = 'vara_img'
LINHA_IMG = 'linha_img'
ANZOL_IMG = 'anzol_img'
ANZOL_PEIXE_VERDE_IMG = 'peixe_verde_anzol_img'
ANZOL_PEIXE_LARANJA_IMG = 'peixe_laranja_anzol_img'
ANZOL_PEIXE_AZUL_IMG = 'peixe_azul_anzol_img'
ANZOL_DANO_IMG = 'anzol_dano_img'
LINHA_DANO_IMG = 'linha_dano_img'

# ---- Fontes
SCORE_FONT = 'score_font'
SCORE_FONT_TABELA = 'score_font_tabela'

# ---- Sons
PESCOU_SOUND = 'pescou_sound'
PERDEU_ISCA_SOUND = 'perdeu_isca_sound'
JOGOU_VARA_SOUND = 'jogou_vara_sound'
BACKGROUND_SOUND = 'background_sound'
CHOQUE_SOUND = 'choque_sound'
CORACAO_SOUND = 'coracao_sound'

# ---- Lista de imagens de peixes e obstáculos
LISTA_OBSTACULOS = "imgs_barris"
LISTA_PEIXES = "imgs_peixes"

# ---- Animações
LINHA_ANIM = 'linha_anim'

# Função que cria o dicionário assets
def load_assets():
    
    # Criando o dicionário assets e adicionando as imagens à ele
    assets = {}

    assets[LINHA_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'linha.png')).convert_alpha()
    assets[LINHA_IMG] = pygame.transform.scale(assets[LINHA_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[ANZOL_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'anzol.png')).convert_alpha()
    assets[ANZOL_IMG] = pygame.transform.scale(assets[ANZOL_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[ANZOL_DANO_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'anzol_dano.png')).convert_alpha()
    assets[ANZOL_DANO_IMG] = pygame.transform.scale(assets[ANZOL_DANO_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[LINHA_DANO_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'linha_dano.png')).convert_alpha()
    assets[LINHA_DANO_IMG] = pygame.transform.scale(assets[LINHA_DANO_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[ANZOL_PEIXE_VERDE_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'anzol_peixe_verde.png')).convert_alpha()
    assets[ANZOL_PEIXE_VERDE_IMG] = pygame.transform.scale(assets[ANZOL_PEIXE_VERDE_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[ANZOL_PEIXE_LARANJA_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'anzol_peixe_laranja.png')).convert_alpha()
    assets[ANZOL_PEIXE_LARANJA_IMG] = pygame.transform.scale(assets[ANZOL_PEIXE_LARANJA_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[ANZOL_PEIXE_AZUL_IMG] = pygame.image.load(path.join(JOGADOR_DIR,'anzol_peixe_azul.png')).convert_alpha()
    assets[ANZOL_PEIXE_AZUL_IMG] = pygame.transform.scale(assets[ANZOL_PEIXE_AZUL_IMG], (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))

    assets[BACKGROUND] = pygame.image.load(path.join(CENARIOS_DIR, 'fundo_do_mar.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))

    assets[BACKGROUND_INSTRU] = pygame.image.load(path.join(CENARIOS_DIR, 'fundo_do_mar_instrucoes_1.png')).convert()
    assets[BACKGROUND_INSTRU] = pygame.transform.scale(assets[BACKGROUND_INSTRU], (WIDTH, HEIGHT))

    assets[POUCOS_PEIXES] = pygame.image.load(path.join(CENARIOS_DIR, 'fundo_do_mar_peixe1.png')).convert()
    assets[POUCOS_PEIXES] = pygame.transform.scale(assets[POUCOS_PEIXES], (WIDTH, HEIGHT))

    assets[MEDIO_PEIXES] = pygame.image.load(path.join(CENARIOS_DIR, 'fundo_do_mar_peixe2.png')).convert()
    assets[MEDIO_PEIXES] = pygame.transform.scale(assets[MEDIO_PEIXES], (WIDTH, HEIGHT))

    assets[CHEIO_PEIXES] = pygame.image.load(path.join(CENARIOS_DIR, 'fundo_do_mar_peixe3.png')).convert()
    assets[CHEIO_PEIXES] = pygame.transform.scale(assets[CHEIO_PEIXES], (WIDTH, HEIGHT))

    assets[PEIXE_LARANJA_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_laranja.png')).convert_alpha()
    assets[PEIXE_LARANJA_IMG] = pygame.transform.scale(assets[PEIXE_LARANJA_IMG],(PEIXES_WIDTH,PEIXES_HEIGHT))

    assets[PEIXE_VERDE_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_verde.png')).convert_alpha()
    assets[PEIXE_VERDE_IMG] = pygame.transform.scale(assets[PEIXE_VERDE_IMG],(PEIXES_WIDTH,PEIXES_HEIGHT))

    assets[PEIXE_AZUL_IMG] = pygame.image.load(path.join(PEIXES_DIR, 'peixe_azul.png')).convert_alpha()
    assets[PEIXE_AZUL_IMG] = pygame.transform.scale(assets[PEIXE_AZUL_IMG],(PEIXES_WIDTH-70,PEIXES_HEIGHT-45))

    assets[BARRIL_MARROM_IMG] = pygame.image.load(path.join(OBJETOS_DIR, 'barril_marrom.png')).convert_alpha()
    assets[BARRIL_MARROM_IMG] = pygame.transform.scale(assets[BARRIL_MARROM_IMG],(BARRIL_WIDTH,BARRIL_HEIGHT))

    assets[BARRIL_LARANJA_IMG] = pygame.image.load(path.join(OBJETOS_DIR, 'barril_laranja.png')).convert_alpha()
    assets[BARRIL_LARANJA_IMG] = pygame.transform.scale(assets[BARRIL_LARANJA_IMG],(BARRIL_WIDTH,BARRIL_HEIGHT))

    assets[VIDA_IMG] = pygame.image.load(path.join(OBJETOS_DIR, 'coracao.png')).convert_alpha()
    assets[VIDA_IMG] = pygame.transform.scale(assets[VIDA_IMG],(VIDA_TAM, VIDA_TAM))

    assets[AGUA_VIVA_IMG] = pygame.image.load(path.join(OBJETOS_DIR, 'agua viva.png')).convert_alpha()
    assets[AGUA_VIVA_IMG] = pygame.transform.scale(assets[AGUA_VIVA_IMG],(AGUA_VIVA_TAM,AGUA_VIVA_TAM))

    # Juntando as imagens dos peixes em uma lista
    IMGS_PEIXES = [assets[PEIXE_LARANJA_IMG], assets[PEIXE_VERDE_IMG],assets[PEIXE_AZUL_IMG]]
    assets[LISTA_PEIXES] = IMGS_PEIXES

    # Juntando as imagens dos barris em uma lista
    IMGS_BARRIS = [assets[BARRIL_LARANJA_IMG], assets[BARRIL_MARROM_IMG]]
    assets[LISTA_OBSTACULOS] = IMGS_BARRIS
    
    # Juntando a fonte do score à ele
    assets[SCORE_FONT] = pygame.font.Font(path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    assets[SCORE_FONT_TABELA] = pygame.font.Font(path.join(FNT_DIR, 'PressStart2P.ttf'), 16)

    # Juntando as animações do choque em uma lista
    # eletrecuta_anim = []
    #for i in range(1, 5):
        # Os arquivos de animação são numerados de 1 a 7
    #    filename = path.join(ANIM_DIR, 'animação frame {0}.png'.format(i))
    #    img = pygame.image.load(filename).convert_alpha()
    #    img = pygame.transform.scale(img, (JOGADOR_WIDTH, JOGADOR_HEIGHT - 50))
    #    eletrecuta_anim.append(img)
    #assets[LINHA_ANIM] = eletrecuta_anim

    # Carrega os sons do jogo
    assets[CHOQUE_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'choque.mp3'))
    assets[PESCOU_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'som_pegou_peixe.mp3'))
    assets[PERDEU_ISCA_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'som_dano.mp3'))
    assets[JOGOU_VARA_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'som_jogou_vara.mp3'))
    assets[CORACAO_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'som_pegou_coracao.mp3'))
    # assets[BACKGROUND_SOUND] = pygame.mixer.Sound(path.join(SND_DIR, 'pew.wav'))

    return assets

def toca_musica(file, volume = 0.5, loop = -1):
    pygame.mixer.music.load(path.join(file))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)
