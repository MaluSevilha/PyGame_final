# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, INICIO, FECHAR, MORTO, JOGANDO
from tela_inicial import tela_inicial
from tela_jogo import game_screen
from game_over import game_over
from assets import toca_musica
# from os import path
# from assets import BACKGROUND

pygame.init()
pygame.mixer.init()


# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fishing Fox')

toca_musica('assets/sons/Club Penguin Music - Ice Fishing.mp3')

state = INICIO
while state != FECHAR:
    if state == INICIO:
        state = tela_inicial(window)
    elif state == JOGANDO:
         state = game_screen(window)
    elif state == MORTO:
        state = game_over(window)
    else:
        state = FECHAR

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

