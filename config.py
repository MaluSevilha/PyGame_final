# Importando bibliotecas usadas
from os import path

# Estabelece o caminho que contem as figuras, sons e fontes
CENARIOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Cenários')
PEIXES_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Peixes')
OBJETOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Objetos')
JOGADOR_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Jogador')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fonte')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'sons')
ANIM_DIR = path.join(path.dirname(__file__), 'assets','imagens', 'Animacao')

# Dados gerais do jogo.
WIDTH = 500 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define velocidades
VEL_JOGADOR = 8

# Define Velocidade das animações
VEL_ANIMA = 0.1

# Define tamanhos
PEIXES_WIDTH = 150
PEIXES_HEIGHT = 100

JOGADOR_WIDTH = 35
JOGADOR_HEIGHT = HEIGHT

BARRIL_WIDTH = 50
BARRIL_HEIGHT = 100

VIDA_TAM = 60       # É um 'quadrado'

AGUA_VIVA_TAM = 70  # É um 'quadrado'

#Cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Estados para controle do fluxo da aplicação
MORTO = -1
INICIO = 0
FECHAR = 1
JOGANDO = 2