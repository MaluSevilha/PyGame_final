from os import path

# Estabelece o caminho que contem as figuras e sons.
CENARIOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Cenários')
PEIXES_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Peixes')
OBJETOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Objetos')
JOGADOR_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Jogador')

# Dados gerais do jogo.
WIDTH = 500 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define velocidades
VEL_PEIXES = 5
VEL_JOGADOR = 8

# Define tamanhos
PEIXES_WIDTH = 150
PEIXES_HEIGHT = 100

JOGADOR_WIDTH = 20
JOGADOR_HEIGHT = 750

BARRIL_WIDTH = 50
BARRIL_HEIGHT = 100


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
