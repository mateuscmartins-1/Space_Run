#Importar o pygames
import pygame 
import random

from pygame.constants import KEYUP

pygame.init()
pygame.mixer.init()


WIDTH = 1252
HEIGHT = 556
tela = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Run')

PLANETA_WIDTH = 480 #Largura do Planeta

PLANETA_HEIGHT = 360 #Altura do Planeta

NAVE_WIDTH = 80 #Largura da nave

NAVE_HEIGHT = 90 #Altura do nave

TIRO_WIDTH = 30 #Largura dos tiros

TIRO_HEIGHT = 30 #Altura dos tiros

assets = {}
#Imagens 
assets["planeta1_fundo"] = pygame.image.load('imgs/Fundo1.png').convert_alpha()
assets["planeta1_fundo"] = pygame.transform.scale(assets["planeta1_fundo"], (WIDTH, HEIGHT))
assets["planeta2_fundo"] = pygame.image.load('imgs/Fundo2.png').convert_alpha()
assets["planeta2_fundo"] = pygame.transform.scale(assets["planeta2_fundo"], (WIDTH, HEIGHT))
assets["planeta3_fundo"] = pygame.image.load('imgs/Fundo3.png').convert_alpha()
assets["planeta3_fundo"] = pygame.transform.scale (assets["planeta3_fundo"], (WIDTH, HEIGHT))
assets["planeta1"] = pygame.image.load ('imgs/Planeta1.png').convert_alpha()
assets["planeta1"] = pygame.transform.scale (assets["planeta1"], (WIDTH,HEIGHT))
assets["planeta1_rect"] = assets["planeta1"].get_rect()
assets["planeta2"] = pygame.image.load ('imgs/Planeta2.png').convert_alpha()
assets["planeta2"] = pygame.transform.scale (assets["planeta2"], (WIDTH,HEIGHT))
assets["planeta2_rect"] = assets["planeta2"].get_rect()
assets["planeta3"] = pygame.image.load ('imgs/Planeta3.png').convert_alpha()
assets["planeta3"] = pygame.transform.scale (assets["planeta3"], (WIDTH,HEIGHT))
assets["planeta3_rect"] = assets["planeta3"].get_rect()
assets["naveaamiga"] = pygame.image.load ('imgs/Nave_amiga.png').convert_alpha()
assets["naveaamiga"] = pygame.transform.scale (assets["naveaamiga"], (NAVE_WIDTH, NAVE_HEIGHT))
assets["naveinimiga"] = pygame.image.load ('imgs/Nave_inimiga.png').convert_alpha()
assets["naveinimiga"] = pygame.transform.scale (assets["naveinimiga"], (NAVE_WIDTH, NAVE_HEIGHT))
assets["tiro_amigo"] = pygame.image.load ('imgs/Tiro amigo.png').convert_alpha() 
assets["tiro_amigo"] = pygame.transform.scale (assets["tiro_amigo"], (TIRO_WIDTH, TIRO_HEIGHT))
assets["tiro_inimigo"] = pygame.image.load ('imgs/Tiro inimigo.png').convert_alpha() 
assets["tiro_inimigo"] = pygame.transform.scale (assets["tiro_inimigo"], (TIRO_WIDTH, TIRO_HEIGHT)) 
assets["tela_estrelas"] = pygame.image.load ('imgs/tela_fundo.png').convert()
assets["tela_estrelas"] = pygame.transform.scale(assets["tela_estrelas"], (WIDTH,HEIGHT))
assets["tela_estrelas_rect"] = assets["tela_estrelas"].get_rect()
assets["tela_instrucoes"] = pygame.image.load('imgs/tela_instrucoes.jpg').convert()
assets["tela_instrucoes"] = pygame.transform.scale(assets["tela_instrucoes"], (WIDTH,HEIGHT))
assets["tela_instrucoes_rect"] = assets["tela_instrucoes"].get_rect()
# Fontes
assets["pontuação"] = pygame.font.Font('fontes/PressStart2P.ttf', 25)
assets["game_over_screen"] = pygame.font.Font('fontes/PressStart2P.ttf', 55)

# Sons
assets["musica"] = pygame.mixer.music.load('sons/Musica-pygame.ogg')
pygame.mixer.music.set_volume(0.4)
assets["game_over"] = pygame.mixer.Sound('sons/Game-over.wav')
assets['proxima_fase'] = pygame.mixer.Sound('sons/Próxima fase.wav')
assets['tiro_acertado'] = pygame.mixer.Sound('sons/Tiro-acertado.wav')
assets['tiro_da_nave'] = pygame.mixer.Sound('sons/Tiro-da-nave.wav')
assets['you_lose'] = pygame.mixer.Sound('sons/you_lose.wav')
assets['you_win'] = pygame.mixer.Sound('sons/you_win.wav')
assets['musica_entrada'] = pygame.mixer.Sound('sons/musica_entrada.wav')
assets['musica_transicao'] = pygame.mixer.Sound('sons/musica_transicao.wav')

# Fases
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
            if self.fases == 1:
                self.intervalo_tiro = 10 + random.randint(1,100)
                self.tiro()
            if self.fases == 2:
                self.intervalo_tiro = 10 + random.randint(1,50)
                self.tiro()
            if self.fases == 3:
                self.intervalo_tiro = 10 + random.randint(1,25)
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

def tela_inicial(janela):
    clock = pygame.time.Clock()
    tela_de_inicio = pygame.image.load('imgs/Spacerun.png').convert()
    tela_de_inicio_rect = tela_de_inicio.get_rect()
    jogo = True
    pygame.mixer.music.stop()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = INTRODUCTION
                    jogo = False
        assets['musica_entrada'].play()
        janela.fill((0,0,0))
        janela.blit(tela_de_inicio, tela_de_inicio_rect)
        pygame.display.flip()
    return state


def tela_de_introducao(janela):
    clock = pygame.time.Clock()
    jogo = True
    pygame.mixer.music.stop()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = TRANSICAO1
                    jogo = False
        janela.fill((0,0,0))
        janela.blit(assets["tela_instrucoes"], assets["tela_instrucoes_rect"])
        pygame.display.flip()
    return state

def tela_troca_fase1(janela):
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
    assets['musica_entrada'].stop()
    assets['musica_transicao'].play()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    state = GAME
                    jogo = False
        janela.fill((0, 0, 0))  
        janela.blit(assets["planeta1"],assets["planeta1_rect"])
        pygame.display.flip()
    return state

def tela_troca_fase2(janela):
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
    pygame.mixer.music.stop()
    assets['musica_transicao'].play()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(loops= -1)
                    state = GAME2
                    jogo = False
        janela.fill((0, 0, 0))  
        janela.blit(assets["planeta2"],assets["planeta2_rect"])
        pygame.display.flip()
    return state

def tela_troca_fase3(janela):
    clock = pygame.time.Clock()
    jogo = True
    state = GAME
    pygame.mixer.music.stop()
    assets['musica_transicao'].play()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(loops= -1)
                    state = GAME3
                    jogo = False
        janela.fill((0, 0, 0))  
        janela.blit(assets["planeta3"],assets["planeta3_rect"])
        pygame.display.flip()
    return state


def tela_final1(janela):
    clock = pygame.time.Clock()
    jogo = True
    controle = True
    pygame.mixer.music.stop()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.play(loops= -1)
                    state= INIT
                    jogo = False
        if controle:
            assets['you_lose'].play()
            controle = False
        font = pygame.font.SysFont(None, 130)
        font2 = pygame.font.SysFont(None, 50)
        gameover = font.render('GAME OVER! YOU LOSE', True, (255, 0, 0))  
        jogue_novamente = font2.render("PARA JOGAR NOVAMENTE PRESSIONE [ENTER]",True, (255,255,255))
        janela.fill((0, 0, 0))  
        janela.blit(assets['tela_estrelas'], assets['tela_estrelas_rect'])
        janela.blit(gameover, (90 , 139))
        janela.blit(jogue_novamente,(200,400))
        pygame.display.flip()
    return state

def tela_final2(janela):
    clock = pygame.time.Clock()
    jogo = True
    state = END_SCREEN2
    controle = True
    pygame.mixer.music.stop()
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                jogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state= INIT
                    jogo = False
        if controle:
            assets['you_win'].play()
            controle = False
        font = pygame.font.SysFont(None, 130)
        font2 = pygame.font.SysFont(None, 50)
        gameover = font.render('GAME OVER! YOU WIN', True, (0, 255, 0))  
        jogue_novamente = font2.render("PARA JOGAR NOVAMENTE PRESSIONE [ENTER]",True, (255,255,255))
        janela.fill((0, 0, 0))  
        janela.blit(assets['tela_estrelas'], assets['tela_estrelas_rect'])
        janela.blit(gameover, (90 , 139))
        janela.blit(jogue_novamente,(200,400))
        pygame.display.flip()
    return state


def tela_do_jogo(janela):
    all_sprites = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_tiros2 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiros'] = all_tiros
    groups['all_inimigos'] = all_inimigos
    groups['all_tiros2'] = all_tiros2


    player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
    all_sprites.add(player_nave)

    pygame.mixer.music.play(loops=-1)
    kills = 0       # Eliminações do player
    vidas = 3       # Vidas da Nave
    pontuacao = 0   # Pontuação do player
    velocidade = 10 # Velocidade 

    for i in range(2):
        i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)
    
    controle = True
    jogo = True
    state = GAME
    FPS = 30
    clock = pygame.time.Clock()

    fases = assets["planeta1_fundo"]


    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                state = QUIT
            if state == GAME:
                assets['musica_transicao'].stop() 
                if event.type == pygame.KEYDOWN:
                    # Ao pressionar alguma dessas teclas o player se movimenta
                    if event.key == pygame.K_w:
                        player_nave.speedy -= velocidade
                    if event.key == pygame.K_a:
                        player_nave.speedx -= velocidade
                    if event.key == pygame.K_s:
                        player_nave.speedy += velocidade
                    if event.key == pygame.K_d:
                        player_nave.speedx += velocidade
                    # Ao pressionar a barra de espaço o player realiza o disparo
                    if event.key == pygame.K_SPACE:
                        player_nave.tiro()
 

        all_sprites.update()
        danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True, pygame.sprite.collide_mask)
        danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True, pygame.sprite.collide_mask)
        
        for Enemy in danos:
            i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
            all_sprites.add(i)
            all_inimigos.add(i)
            all_tiros2.add(i)
            kills += 1 
            pontuacao += 5
        if kills == 5 and controle:
            if controle:
                assets['proxima_fase'].play()
                controle = False 
            state = TRANSICAO2
            jogo = False
      
            
        if danos:
            assets['tiro_acertado'].play()
        if danos2:
            vidas-= 1
            if vidas != 0:
                player_nave.kill()
                player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
                all_sprites.add(player_nave)
        if vidas == 0:
            state = END_SCREEN
            jogo = False
            
 
        janela.fill((0,0,0))
        janela.blit(fases, (0, 0))
        all_sprites.draw(janela)

       

        # Colocando a Pontuação
        pontuacao_tela = assets['pontuação'].render("{:03d}".format(pontuacao), True, (0, 255, 0))
        text_rect = pontuacao_tela.get_rect()
        text_rect.midtop = (WIDTH/2 ,  10)
        janela.blit(pontuacao_tela, text_rect)

        # Colocando as vidas
        vida_tela = assets['pontuação'].render(chr(9827) * vidas, True, (255, 0, 0))
        text_rect = vida_tela.get_rect()
        text_rect.bottomright = (WIDTH, HEIGHT - 10)
        janela.blit(vida_tela, text_rect)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
    return state
def tela_do_jogo2(janela):
    all_sprites = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_tiros2 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiros'] = all_tiros
    groups['all_inimigos'] = all_inimigos
    groups['all_tiros2'] = all_tiros2


    player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
    all_sprites.add(player_nave)

    pygame.mixer.music.play(loops=-1)
    kills = 0       # Eliminações do player
    vidas = 3       # Vidas da Nave
    pontuacao = 0   # Pontuação do player
    velocidade = 10 # Velocidade 
    

    for i in range(3):
        i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)

    controle = True
    jogo = True
    state = GAME2
    FPS = 30
    clock = pygame.time.Clock()

    fases = assets["planeta2_fundo"]


    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                state = QUIT
            if state == GAME2:
                assets['musica_transicao'].stop() 
                if event.type == pygame.KEYDOWN:
                    # Ao pressionar alguma dessas teclas o player se movimenta
                    if event.key == pygame.K_w:
                        player_nave.speedy -= velocidade
                    if event.key == pygame.K_a:
                        player_nave.speedx -= velocidade
                    if event.key == pygame.K_s:
                        player_nave.speedy += velocidade
                    if event.key == pygame.K_d:
                        player_nave.speedx += velocidade
                    # Ao pressionar a barra de espaço o player realiza o disparo
                    if event.key == pygame.K_SPACE:
                        player_nave.tiro()
        all_sprites.update()
        danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True, pygame.sprite.collide_mask)
        danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True, pygame.sprite.collide_mask)
        for Enemy in danos:
            i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
            all_sprites.add(i)
            all_inimigos.add(i)
            all_tiros2.add(i)
            kills += 1 
            pontuacao += 5
        if kills == 8 and controle:
            if controle:
                assets['proxima_fase'].play()
                controle = False 
            state = TRANSICAO3
            jogo = False
        if danos:
            assets['tiro_acertado'].play()
        if danos2:
            vidas-= 1
            if vidas != 0:
                player_nave.kill()
                player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
                all_sprites.add(player_nave)
        if vidas == 0:
            state = END_SCREEN
            jogo = False
        
 
        janela.fill((0,0,0))
        janela.blit(fases, (0, 0))
        all_sprites.draw(janela)

       

        # Colocando a Pontuação
        pontuacao_tela = assets['pontuação'].render("{:03d}".format(pontuacao), True, (0, 255, 0))
        text_rect = pontuacao_tela.get_rect()
        text_rect.midtop = (WIDTH/2 ,  10)
        janela.blit(pontuacao_tela, text_rect)

        # Colocando as vidas
        vida_tela = assets['pontuação'].render(chr(9827) * vidas, True, (255, 0, 0))
        text_rect = vida_tela.get_rect()
        text_rect.bottomright = (WIDTH, HEIGHT - 10)
        janela.blit(vida_tela, text_rect)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
    return state

def tela_do_jogo3(janela):
    all_sprites = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_tiros2 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiros'] = all_tiros
    groups['all_inimigos'] = all_inimigos
    groups['all_tiros2'] = all_tiros2


    player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
    all_sprites.add(player_nave)

    pygame.mixer.music.play(loops=-1)
    kills = 0       # Eliminações do player
    vidas = 3       # Vidas da Nave
    pontuacao = 0   # Pontuação do player
    velocidade = 10 # Velocidade 
    

    for i in range(4):
        i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)

    jogo = True
    state = GAME3
    FPS = 30
    clock = pygame.time.Clock()

    fases = assets["planeta3_fundo"]
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                state = QUIT
            if state == GAME3:
                assets['musica_transicao'].stop() 
                if event.type == pygame.KEYDOWN:
                    # Ao pressionar alguma dessas teclas o player se movimenta
                    if event.key == pygame.K_w:
                        player_nave.speedy -= velocidade
                    if event.key == pygame.K_a:
                        player_nave.speedx -= velocidade
                    if event.key == pygame.K_s:
                        player_nave.speedy += velocidade
                    if event.key == pygame.K_d:
                        player_nave.speedx += velocidade
                    # Ao pressionar a barra de espaço o player realiza o disparo
                    if event.key == pygame.K_SPACE:
                        player_nave.tiro()
        all_sprites.update()
        danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True, pygame.sprite.collide_mask)
        danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True, pygame.sprite.collide_mask)
        for Enemy in danos:
            i = inimigo(assets['naveinimiga'],groups['all_sprites'],groups['all_tiros2'],assets['tiro_inimigo'])
            all_sprites.add(i)
            all_inimigos.add(i)
            all_tiros2.add(i)
            kills += 1 
            pontuacao += 5
        if danos:
            assets['tiro_acertado'].play()
        if kills == 10:
            state = END_SCREEN2
            jogo = False
        if danos2:
            vidas-= 1
            if vidas != 0:
                player_nave.kill()
                player_nave = amigo(assets['naveaamiga'], groups['all_sprites'], groups['all_tiros'], assets['tiro_amigo'], assets['tiro_da_nave'])
                all_sprites.add(player_nave)
        if vidas == 0:
            state = END_SCREEN
            jogo = False
            
 
        janela.fill((0,0,0))
        janela.blit(fases, (0, 0))
        all_sprites.draw(janela)

       

        # Colocando a Pontuação
        pontuacao_tela = assets['pontuação'].render("{:03d}".format(pontuacao), True, (0, 255, 0))
        text_rect = pontuacao_tela.get_rect()
        text_rect.midtop = (WIDTH/2 ,  10)
        janela.blit(pontuacao_tela, text_rect)

        # Colocando as vidas
        vida_tela = assets['pontuação'].render(chr(9827) * vidas, True, (255, 0, 0))
        text_rect = vida_tela.get_rect()
        text_rect.bottomright = (WIDTH, HEIGHT - 10)
        janela.blit(vida_tela, text_rect)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
    return state
            
INIT = 0 
GAME = 1 
QUIT = 2 
END_SCREEN = 3
END_SCREEN2 = 4
INTRODUCTION = 5
TRANSICAO1 = 6
TRANSICAO2 = 7
TRANSICAO3 = 8
GAME2 = 9
GAME3 = 10
FPS = 30

state = INIT

while state != QUIT:
    if state == INIT:
        state = tela_inicial(tela)
    elif state == INTRODUCTION:
        state = tela_de_introducao(tela)
    elif state == TRANSICAO1:
        state = tela_troca_fase1(tela)
    elif state == TRANSICAO2:
        state = tela_troca_fase2(tela)
    elif state == TRANSICAO3:
        state = tela_troca_fase3(tela)
    elif state == GAME:
        state = tela_do_jogo(tela)
    elif state == GAME2:
        state = tela_do_jogo2(tela)
    elif state == GAME3:
        state = tela_do_jogo3(tela)
    elif state == END_SCREEN:
        state = tela_final1(tela)
    elif state == END_SCREEN2:
        state = tela_final2(tela)
    else:
        state = QUIT

# ===== Finalização ===== #
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
