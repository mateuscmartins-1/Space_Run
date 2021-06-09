import pygame 
import random 
from config import WIDTH, HEIGHT, NAVE_HEIGHT, NAVE_WIDTH, TIRO_HEIGHT, TIRO_WIDTH
from assets import SOM_TIRO
class amigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro,som_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = random.randint(139, 417)
        self.rect.left = 0
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 800
        self.som_tiro = som_tiro

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > WIDTH//2:
            self.rect.right = WIDTH//2
        if self.rect.left < 0:
            self.rect.left = 0
        if self.speedx > 0:
            self.speedx -= 1
        elif self.speedx < 0:
            self.speedx += 1
        if self.speedy > 0:
            self.speedy -= 1
        elif self.speedy < 0:
            self.speedy += 1
    def tiro(self):
        ticks = pygame.time.get_ticks()
        ticks_passados = ticks - self.ultimo_tiro
        if ticks_passados > self.intervalo_tiro:
            self.ultimo_tiro = ticks
            bala = Tiro_Amigo(self.tiro_img, self.rect.bottom, self.rect.centerx)
            self.all_sprites.add(bala)
            self.all_tiros.add(bala)
            self.som_tiro.play()
            
class inimigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0,HEIGHT-NAVE_HEIGHT)
        self.rect.x = WIDTH-NAVE_WIDTH
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.speedx = -3
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 10
        self.fases = 1 
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 1000:
            self.rect.x = 1000
        self.speedx = -3
        self.intervalo_tiro -= 1
        if self.intervalo_tiro <= 0:
            self.intervalo_tiro = 10 + random.randint(1,75)
            self.tiro()
    def tiro(self):
        ticks = pygame.time.get_ticks()
        ticks_passados = ticks - self.ultimo_tiro
        if ticks_passados > self.intervalo_tiro:
            self.ultimo_tiro = ticks
            bala = Tiro_Inimigo(self.tiro_img, self.rect.bottom, self.rect.centerx)
            self.all_sprites.add(bala)
            self.all_tiros.add(bala)

class Tiro_Amigo(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = 8  
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()

class Tiro_Inimigo(pygame.sprite.Sprite):
    def __init__(self, img, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH-TIRO_WIDTH 
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = -8  
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()
        self.speedx = -8