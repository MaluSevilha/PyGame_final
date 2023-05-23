import random
import pygame
from config import WIDTH, HEIGHT, PEIXES_HEIGHT, PEIXES_WIDTH, VEL_PEIXES
from assets import SHIP_IMG, PEW_SOUND, METEOR_IMG, BULLET_IMG, EXPLOSION_ANIM

class Peixes(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Sorteia a imagem do peixe
        self.image = random.choice(assets['imgs_peixes'])
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()
        self.rect.centerx = PEIXES_WIDTH / 2
        self.rect.bottom = PEIXES_HEIGHT - 10

        # Cria variáveis do peixe e grupos
        self.speedx = VEL_PEIXES
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.kill()
        if self.rect.left < 0:
            self.kill()