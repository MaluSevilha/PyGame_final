# Importando bibliotecas usadas
import pygame

# Importando variáveis e funções de outros arquivos
from config import WIDTH, HEIGHT, INICIO, FECHAR, MORTO, JOGANDO, SCORES_LISTA, INSTRUCAO
from tela_inicial import tela_inicial
from tela_jogo import game_screen
from game_over import game_over
from tela_instrucao import instrucao

# Iniciando o pygame
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fishing Fox')


# ----- Loop Principal
state = INICIO
while state != FECHAR:
    # Começa a tela de início
    if state == INICIO:
        state = tela_inicial(window)

    # Abre a tela de instruções
    elif state == INSTRUCAO:
        lista_return = instrucao(window)
        state = lista_return

    # Abre a tela do jogo
    elif state == JOGANDO:
        lista_return = game_screen(window)
        state = lista_return[0]
        score = lista_return[1]

    # Abre a tela de Game Over
    elif state == MORTO:
        lista_return = game_over(window, score, SCORES_LISTA)
        state = lista_return[0]
        SCORES_LISTA = lista_return[1]

    # Encerra o pygame
    else:
        state = FECHAR

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
