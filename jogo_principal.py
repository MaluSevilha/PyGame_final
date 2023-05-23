# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, INICIO, FECHAR, MORTO, FPS, PRETO
from tela_inicial import tela_inicial
# from game_screen import game_screen
from game_over import game_over
# from os import path
# from assets import BACKGROUND

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fishing Fox')

state = INICIO
while state != FECHAR:
    if state == INICIO:
        state = tela_inicial(window)
    # elif state == GAME:
    #     state = game_screen(window)
    # elif state == DEAD:
    #     state = game_over(window)
    else:
        state = FECHAR

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

