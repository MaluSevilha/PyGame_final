from os import path

# Estabelece o caminho que contem as figuras e sons.
CENARIOS_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Cenários')
PEIXES_DIR = path.join(path.dirname(__file__), 'assets', 'imagens', 'Peixes')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define velocidades
VEL_PEIXES = 5

# Define tamanhos
PEIXES_WIDTH = 100
PEIXES_HEIGHT = 50

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