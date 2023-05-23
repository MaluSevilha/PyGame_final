import random
import pygame
from config import WIDTH, HEIGHT, PEIXES_HEIGHT, PEIXES_WIDTH, VEL_PEIXES, VEL_JOGADOR, JOGADOR_WIDTH, JOGADOR_HEIGHT
from assets import VARA_IMG, LISTA_PEIXES

class Peixes(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Sorteia a imagem do peixe
        self.image = random.choice(assets[LISTA_PEIXES])
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(0, HEIGHT - PEIXES_HEIGHT)

        # Cria variáveis do peixe e grupos
        self.speedx = VEL_PEIXES
        self.assets = assets

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mata quando sai da sala
        if self.rect.right - 30 > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()
    
class Vara(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da vara
        self.image = assets[VARA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = JOGADOR_HEIGHT - 10

        # Cria variáveis da vara e grupos
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da nave
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.top + JOGADOR_HEIGHT - 10 < 0:
            self.rect.bottom = 10
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT