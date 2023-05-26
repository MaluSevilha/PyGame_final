import random
import pygame
from config import WIDTH, HEIGHT, PEIXES_HEIGHT, PEIXES_WIDTH, JOGADOR_HEIGHT, BARRIL_HEIGHT, BARRIL_WIDTH, VIDA_TAM, AGUA_VIVA_TAM
from assets import LISTA_PEIXES, LISTA_OBSTACULOS, VIDA_IMG, ANZOL_IMG, LINHA_IMG, ANZOL_PEIXE_VERDE_IMG, AGUA_VIVA_IMG

# Classe dos peixes
class Peixes(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        # Sorteia a imagem do peixe
        self.image = random.choice(assets[LISTA_PEIXES])
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        self.rect = self.image.get_rect()
        self.rect.x = -PEIXES_WIDTH
        self.rect.y = random.randint(96, HEIGHT - PEIXES_HEIGHT)

        # Cria variáveis do peixe e grupos
        self.speedx = random.randint(2, 5)
        self.assets = assets

    def update(self,level,level2):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Recria quando sai da sala
        if self.rect.right - PEIXES_WIDTH > WIDTH:
            self.image = random.choice(self.assets[LISTA_PEIXES])
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = -PEIXES_WIDTH
            self.rect.y = random.randint(96, HEIGHT - PEIXES_HEIGHT)
            self.speedx = random.randint(2,5)

# Classe do ANzol (player)    
class Anzol(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da vara
        self.image = assets[ANZOL_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        # ---- Vara
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = JOGADOR_HEIGHT - 10

        # Cria variáveis da vara e grupos
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self,level,level2):
        # Atualização da posição da vara
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.top + JOGADOR_HEIGHT - 10 < 0:
            self.rect.bottom = 10
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    
    def update2(self,peixe_pescado,assets):
        # Muda a imagem se peixe estiver no anzol
        if peixe_pescado == True:
            self.image = assets[ANZOL_PEIXE_VERDE_IMG]
        else:
            self.image = assets[ANZOL_IMG]

# Classe da linha
class Linha(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        # Definindo a imagem da Linha
        self.image = assets[LINHA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Cria o retângulo de referência
        # ---- Linha
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = JOGADOR_HEIGHT - 10

        # Cria variáveis da vara e grupos
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self,level,level2):
        # Atualização da posição da vara
        self.rect.y += self.speedy

        # Mantem dentro da tela e ligada com o anzol
        if self.rect.top + JOGADOR_HEIGHT - 10 < 0:
            self.rect.bottom = 10
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT          

# Classe do barril
class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Definindo imagem
        self.image = random.choice(assets[LISTA_OBSTACULOS])
        self.mask = pygame.mask.from_surface(self.image)

        # Criando retângulode referência
        self.rect = self.image.get_rect()
        self.rect.x = -BARRIL_WIDTH
        self.rect.y = random.randint(96, HEIGHT - BARRIL_HEIGHT)
        self.speedx = random.randint(1,3)

        self.assets = assets

    def update(self,level,level2):
        # Atualizando a posição do obstáculo
        self.rect.x += self.speedx

        # Recria quando sai da sala
        if self.rect.right - BARRIL_WIDTH > WIDTH:
            self.image = random.choice(self.assets[LISTA_OBSTACULOS])
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.x = - BARRIL_WIDTH
            self.rect.y = random.randint(96, HEIGHT - BARRIL_HEIGHT)
        
        # Muda sua velocidade de acordo com o nível
        if level == False:
            self.speedx = random.randint(2,4)
        else:
            self.speedx = random.randint(2,7)

        if level2 == True:
            self.speedx = random.randint(10,15)

# Classe das vidas
class Vida(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Definindo imagem
        self.image = assets[VIDA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Criando retângulode referência
        self.rect = self.image.get_rect()
        self.rect.x = -VIDA_TAM
        self.rect.y = random.randint(96, HEIGHT - VIDA_TAM)

        # Definindo velocidades
        self.speedx = 3
        self.assets = assets

    def update(self,level,level2):
        # Atualizando a posição da vida
        self.rect.x += self.speedx

        # Mata quando sai da sala
        if self.rect.right - VIDA_TAM > WIDTH:
            self.kill()

# Classe da água viva
class Aguaviva(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Definindo imagem
        self.image = assets[AGUA_VIVA_IMG]
        self.mask = pygame.mask.from_surface(self.image)

        # Criando retângulode referência
        self.rect = self.image.get_rect()
        self.rect.x = -AGUA_VIVA_TAM
        self.rect.y = random.randint(96, HEIGHT - AGUA_VIVA_TAM)

        # Definindo velocidades
        self.speedx = random.randint(2,5)
        self.assets = assets

    def update(self,level,level2):
        # Atualizando a posição da água viva
        self.rect.x += self.speedx

        # Mata quando sai da sala
        if self.rect.right - AGUA_VIVA_TAM > WIDTH:
            self.kill()

        if level2 == True :
            self.speedx = random.randint(6,9)