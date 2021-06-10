import pygame 
from config import GAME,END_SCREEN,END_SCREEN2,QUIT,WIDTH,HEIGHT,TRANSICAO2,TRANSICAO3,GAME2,GAME3
from sprites import amigo,inimigo
from assets import load_assets,MUSICA_TRANSICAO, TIRO_INIMIGO, TIRO_AMIGO,PLANETA1_FUNDO,PLANETA2_FUNDO,PLANETA3_FUNDO,NAVE_AMIGA,NAVE_INIMIGA,TIRO_ACERTADO,TIRO_DA_NAVE,SOM_TIRO,MUSICA,PROXIMA_FASE,YOU_LOSE,YOU_WIN,PONTUACAO

def tela_do_jogo(janela):
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_tiros2 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiros'] = all_tiros
    groups['all_inimigos'] = all_inimigos
    groups['all_tiros2'] = all_tiros2

    	
    player_nave = amigo(assets[NAVE_AMIGA], groups['all_sprites'], groups['all_tiros'], assets[TIRO_AMIGO])
    all_sprites.add(player_nave)
    pygame.mixer.stop()
    pygame.mixer.music.play()
    kills = 0       # Eliminações do player
    vidas = 3       # Vidas da Nave
    pontuacao = 0   # Pontuação do player
    velocidade = 10 # Velocidade 

    for i in range(2):
        i = inimigo(assets[NAVE_INIMIGA],groups['all_sprites'],groups['all_tiros2'],assets[TIRO_INIMIGO])
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)
    
    controle = True
    jogo = True
    state = GAME
    FPS = 30
    clock = pygame.time.Clock()

    fases = assets[PLANETA1_FUNDO]


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
                        assets[SOM_TIRO].play()
 

        all_sprites.update()
        danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True, pygame.sprite.collide_mask)
        danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True, pygame.sprite.collide_mask)
        
        for Enemy in danos:
            i = inimigo(assets[NAVE_INIMIGA],groups['all_sprites'],groups['all_tiros2'],assets[TIRO_INIMIGO])
            all_sprites.add(i)
            all_inimigos.add(i)
            all_tiros2.add(i)
            kills += 1 
            pontuacao += 5
        if kills == 5 and controle:
            if controle:
                assets[PROXIMA_FASE].play()
                controle = False 
            state = TRANSICAO2
            jogo = False
      
            
        if danos:
            assets[TIRO_ACERTADO].play()
        if danos2:
            vidas-= 1
            if vidas != 0:
                player_nave.kill()
                player_nave = amigo(assets[NAVE_AMIGA], groups['all_sprites'], groups['all_tiros'], assets[TIRO_AMIGO])
                all_sprites.add(player_nave)
        if vidas == 0:
            state = END_SCREEN
            jogo = False
            
 
        janela.fill((0,0,0))
        janela.blit(fases, (0, 0))
        all_sprites.draw(janela)

       

        # Colocando a Pontuação
        pontuacao_tela = assets[PONTUACAO].render("{:03d}".format(pontuacao), True, (0, 255, 0))
        text_rect = pontuacao_tela.get_rect()
        text_rect.midtop = (WIDTH/2 ,  10)
        janela.blit(pontuacao_tela, text_rect)

        # Colocando as vidas
        vida_tela = assets[PONTUACAO].render(chr(9827) * vidas, True, (255, 0, 0))
        text_rect = vida_tela.get_rect()
        text_rect.bottomright = (WIDTH, HEIGHT - 10)
        janela.blit(vida_tela, text_rect)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
    return state
def tela_do_jogo2(janela):
    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_tiros2 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiros'] = all_tiros
    groups['all_inimigos'] = all_inimigos
    groups['all_tiros2'] = all_tiros2


    player_nave = amigo(assets[NAVE_AMIGA], groups['all_sprites'], groups['all_tiros'], assets[TIRO_AMIGO])
    all_sprites.add(player_nave)
    pygame.mixer.stop()
    pygame.mixer.music.play()
    kills = 0       # Eliminações do player
    vidas = 3       # Vidas da Nave
    pontuacao = 0   # Pontuação do player
    velocidade = 10 # Velocidade 
    

    for i in range(3):
        i = inimigo(assets[NAVE_INIMIGA],groups['all_sprites'],groups['all_tiros2'],assets[TIRO_INIMIGO])
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)

    controle = True
    jogo = True
    state = GAME2
    FPS = 30
    clock = pygame.time.Clock()

    fases = assets[PLANETA2_FUNDO]

    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                state = QUIT
            if state == GAME2:
                assets[MUSICA_TRANSICAO].stop() 
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
                        assets[SOM_TIRO].play()
        all_sprites.update()
        danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True, pygame.sprite.collide_mask)
        danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True, pygame.sprite.collide_mask)
        for Enemy in danos:
            i = inimigo(assets[NAVE_INIMIGA],groups['all_sprites'],groups['all_tiros2'],assets[TIRO_INIMIGO])
            all_sprites.add(i)
            all_inimigos.add(i)
            all_tiros2.add(i)
            kills += 1 
            pontuacao += 5
        if kills == 8 and controle:
            if controle:
                assets[PROXIMA_FASE].play()
                controle = False 
            state = TRANSICAO3
            jogo = False
        if danos:
            assets[TIRO_ACERTADO].play()
        if danos2:
            vidas-= 1
            if vidas != 0:
                player_nave.kill()
                player_nave = amigo(assets[NAVE_AMIGA], groups['all_sprites'], groups['all_tiros'], assets[TIRO_AMIGO])
                all_sprites.add(player_nave)
        if vidas == 0:
            state = END_SCREEN
            jogo = False
        
 
        janela.fill((0,0,0))
        janela.blit(fases, (0, 0))
        all_sprites.draw(janela)

       

        # Colocando a Pontuação
        pontuacao_tela = assets[PONTUACAO].render("{:03d}".format(pontuacao), True, (0, 255, 0))
        text_rect = pontuacao_tela.get_rect()
        text_rect.midtop = (WIDTH/2 ,  10)
        janela.blit(pontuacao_tela, text_rect)

        # Colocando as vidas
        vida_tela = assets[PONTUACAO].render(chr(9827) * vidas, True, (255, 0, 0))
        text_rect = vida_tela.get_rect()
        text_rect.bottomright = (WIDTH, HEIGHT - 10)
        janela.blit(vida_tela, text_rect)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
    return state

def tela_do_jogo3(janela):
    assets = load_assets()
    all_sprites = pygame.sprite.Group()
    all_tiros = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_tiros2 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_tiros'] = all_tiros
    groups['all_inimigos'] = all_inimigos
    groups['all_tiros2'] = all_tiros2


    player_nave = amigo(assets[NAVE_AMIGA], groups['all_sprites'], groups['all_tiros'], assets[TIRO_AMIGO])
    all_sprites.add(player_nave)
    pygame.mixer.stop()
    pygame.mixer.music.play()
    kills = 0       # Eliminações do player
    vidas = 3       # Vidas da Nave
    pontuacao = 0   # Pontuação do player
    velocidade = 10 # Velocidade 
    

    for i in range(4):
        i = inimigo(assets[NAVE_INIMIGA],groups['all_sprites'],groups['all_tiros2'],assets[TIRO_INIMIGO])
        all_sprites.add(i)
        all_inimigos.add(i)
        all_tiros2.add(i)

    jogo = True
    state = GAME3
    FPS = 30
    clock = pygame.time.Clock()

    fases = assets[PLANETA3_FUNDO]
    while jogo:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                state = QUIT
            if state == GAME3:
                assets[MUSICA_TRANSICAO].stop() 
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
                        assets[SOM_TIRO].play()
        all_sprites.update()
        danos = pygame.sprite.groupcollide(all_inimigos, all_tiros, True, True, pygame.sprite.collide_mask)
        danos2 = pygame.sprite.spritecollide(player_nave, all_tiros2, True, pygame.sprite.collide_mask)
        for Enemy in danos:
            i = inimigo(assets[NAVE_INIMIGA],groups['all_sprites'],groups['all_tiros2'],assets[TIRO_INIMIGO])
            all_sprites.add(i)
            all_inimigos.add(i)
            all_tiros2.add(i)
            kills += 1 
            pontuacao += 5
        if danos:
            assets[TIRO_ACERTADO].play()
        if kills == 10:
            state = END_SCREEN2
            jogo = False
        if danos2:
            vidas-= 1
            if vidas != 0:
                player_nave.kill()
                player_nave = amigo(assets[NAVE_AMIGA], groups['all_sprites'], groups['all_tiros'], assets[TIRO_AMIGO])
                all_sprites.add(player_nave)
        if vidas == 0:
            state = END_SCREEN
            jogo = False
            
 
        janela.fill((0,0,0))
        janela.blit(fases, (0, 0))
        all_sprites.draw(janela)

       

        # Colocando a Pontuação
        pontuacao_tela = assets[PONTUACAO].render("{:03d}".format(pontuacao), True, (0, 255, 0))
        text_rect = pontuacao_tela.get_rect()
        text_rect.midtop = (WIDTH/2 ,  10)
        janela.blit(pontuacao_tela, text_rect)

        # Colocando as vidas
        vida_tela = assets[PONTUACAO].render(chr(9827) * vidas, True, (255, 0, 0))
        text_rect = vida_tela.get_rect()
        text_rect.bottomright = (WIDTH, HEIGHT - 10)
        janela.blit(vida_tela, text_rect)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        pygame.display.flip()
    return state