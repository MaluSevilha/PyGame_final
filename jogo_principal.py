# Importando bibliotecas usadas
import pygame

# Importando variáveis e funções de outros arquivos
from config import WIDTH, HEIGHT, INICIO, FECHAR, MORTO, JOGANDO
from tela_inicial import tela_inicial
from tela_jogo import game_screen
from game_over import game_over
# from assets import toca_musica
# from os import path
# from assets import BACKGROUND

# Iniciando o pygame
pygame.init()
#pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fishing Fox')

#toca_musica('assets/sons/Club Penguin Music - Ice Fishing.mp3')

# ----- Loop Principal
state = INICIO
while state != FECHAR:
    # Abre a tela de início
    if state == INICIO:
        state = tela_inicial(window)
    # Abre a tela do jogo
    elif state == JOGANDO:
         state = game_screen(window)
    # Abre a tela de Game Over
    elif state == MORTO:
        state = game_over(window)
    # Encerra o pygame
    else:
        state = FECHAR

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
