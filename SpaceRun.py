#Importar o pygame
import pygame 
import random

pygame.init()
pygame.mixer.init()


WIDTH = 1252
HEIGHT = 556
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Run')

PLANETA_WIDTH = 480 #Largura do Planeta

PLANETA_HEIGHT = 360 #Altura do Planeta

NAVE_WIDTH = 130 #Largura da nave

NAVE_HEIGHT = 140 #Altura do nave

TIRO_WIDTH = 50 #Largura dos tiros

TIRO_HEIGHT = 50 #Altura dos tiros

assets = {}
#Imagens 
assets["planeta1_fundo"] = pygame.image.load('imgs/Fundo1.png').convert_alpha()
assets["planeta1_fundo"] = pygame.transform.scale(assets["planeta1_fundo"], (WIDTH, HEIGHT))
assets["planeta2_fundo"] = pygame.image.load('imgs/Fundo2.png').convert_alpha()
assets["planeta2_fundo"] = pygame.transform.scale(assets["planeta2_fundo"], (WIDTH, HEIGHT))
assets["planeta3_fundo"] = pygame.image.load('imgs/Fundo3.png').convert_alpha()
assets["planeta3_fundo"] = pygame.transform.scale (assets["planeta3_fundo"], (WIDTH, HEIGHT))
assets["planeta1"] = pygame.image.load ('imgs/Planeta1.png').convert_alpha()
assets["planeta1"] = pygame.transform.scale (assets["planeta1"], (PLANETA_WIDTH,PLANETA_HEIGHT))
assets["planeta2"] = pygame.image.load ('imgs/Planeta2.png').convert_alpha()
assets["planeta2"] = pygame.transform.scale (assets["planeta2"], (PLANETA_WIDTH, PLANETA_HEIGHT))
assets["planeta3"] = pygame.image.load ('imgs/Planeta3.png').convert_alpha()
assets["planeta3"] = pygame.transform.scale (assets["planeta3"], (PLANETA_WIDTH, PLANETA_HEIGHT))
assets["naveaamiga"] = pygame.image.load ('imgs/Nave_amiga.png').convert_alpha()
assets["naveaamiga"] = pygame.transform.scale (assets["naveaamiga"], (NAVE_WIDTH, NAVE_HEIGHT))
assets["naveinimiga"] = pygame.image.load ('imgs/Nave_inimiga.png').convert_alpha()
assets["naveinimiga"] = pygame.transform.scale (assets["naveinimiga"], (NAVE_WIDTH, NAVE_HEIGHT))
assets["tiro_amigo"] = pygame.image.load ('imgs/Tiro amigo.png').convert_alpha() 
assets["tiro_amigo"] = pygame.transform.scale (assets["tiro_amigo"], (TIRO_WIDTH, TIRO_HEIGHT))
assets["tiro_inimigo"] = pygame.image.load ('imgs/Tiro inimigo.png').convert_alpha() 
assets["tiro_inimigo"] = pygame.transform.scale (assets["tiro_inimigo"], (TIRO_WIDTH, TIRO_HEIGHT)) 

#Sons
assets["musica"] = pygame.mixer.music.load('sons/Musica-pygame.ogg')
pygame.mixer.music.set_volume(0.4)
assets["game_over"] = pygame.mixer.Sound('sons/Game-over.wav')
assets['proxima_fase'] = pygame.mixer.Sound('sons/Próxima fase.wav')
assets['tiro_acertado'] = pygame.mixer.Sound('sons/Tiro-acertado.wav')
assets['tiro_da_nave'] = pygame.mixer.Sound('sons/Tiro-da-nave.wav')


class amigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2
        self.rect.left = 0
        self.speedx = 0
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 800

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


class inimigo(pygame.sprite.Sprite):
    def __init__(self,img,all_sprites,all_tiros,img_tiro):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0,HEIGHT-NAVE_HEIGHT)
        self.rect.x = WIDTH-NAVE_WIDTH
        self.all_sprites = all_sprites
        self.all_tiros = all_tiros
        self.tiro_img = img_tiro
        self.speedx = -3
        self.ultimo_tiro = pygame.time.get_ticks()
        self.intervalo_tiro = 10
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left < 1000:
            self.rect.x = 1000
        self.speedx = -3
        self.intervalo_tiro -= 1
        if self.intervalo_tiro <= 0:
            self.intervalo_tiro = 10 + random.randint(1,100)
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

all_sprites = pygame.sprite.Group()
all_tiros = pygame.sprite.Group()
all_inimigos = pygame.sprite.Group()
all_tiros2 = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
groups['all_sprites'] = all_tiros
groups['all_sprites'] = all_inimigos
groups['all_sprites'] = all_tiros2


player_nave = amigo(assets['naveaamiga'], all_sprites, all_tiros, assets['tiro_amigo'])
all_sprites.add(player_nave)

for i in range(2):
    inimigo_nave = inimigo(assets['naveinimiga'],all_sprites,all_tiros2,assets['tiro_inimigo'])
    all_sprites.add(inimigo_nave)
    all_inimigos.add(inimigo_nave)
    all_tiros2.add(inimigo_nave)
pontuacao = 0
vidas = 3 #Vidas da Nave
velocidade = 10 #Velocidade 
game = True
FPS = 30
clock = pygame.time.Clock()

pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_nave.speedy += velocidade
            if event.key == pygame.K_UP:
                player_nave.speedy -= velocidade
            if event.key == pygame.K_RIGHT:
                player_nave.speedx += velocidade
            if event.key == pygame.K_LEFT:
                player_nave.speedx -= velocidade
            if event.key == pygame.K_SPACE:
                player_nave.tiro()
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_DOWN:
        #         player_nave.speedy = 0
        #     if event.key == pygame.K_UP:
        #         player_nave.speedy = 0
        #     if event.key == pygame.K_RIGHT:
        #         player_nave.speedx = 0
        #     if event.key == pygame.K_LEFT:
        #         player_nave.speedx = 0

    all_sprites.update()
    danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True)
    danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True)
    for Enemy in danos:
        i = inimigo(assets["naveinimiga"],all_sprites,all_tiros2,assets['tiro_inimigo'])
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)
        pontuacao += 100
    
    if danos2:
        vidas-= 1
        if vidas ==0:
            game = False

    tela.blit(assets["planeta1_fundo"], (0, 0))
    all_sprites.draw(tela)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados