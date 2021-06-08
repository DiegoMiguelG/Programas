import pygame, sys, os

#const

WIDTH = 800
HIGH = 600
COLOR = (138,34,174)
player_size = [20,20]
player_pos = [WIDTH / 2 , HIGH - player_size[0] * 2]
enemies_pos = [WIDTH /2, HIGH - 200]
black_color = (0,0,0)
blue_color = (0,0,255)

#window
os.environ['SDL_VIDEO_CENTERED'] = '1'
window = pygame.display.set_mode((WIDTH,HIGH))

game_over = False

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size[0]
        
            if event.key == pygame.K_RIGHT:
                x += player_size[0]
            if event.key == pygame.K_DOWN:
                y += player_size[0]
            if event.key == pygame.K_UP:
                y -= player_size[0]
            
            player_pos[0] = x
            player_pos[1] = y

    window.fill(black_color)
    #Player
    pygame.draw.rect(
        window, 
        COLOR, 
        (
            player_pos[0], 
            player_pos[1], 
            player_size[0], 
            player_size[1]
            )
        )
    pygame.display.update()

    #enemies
    pygame.draw.rect(
        window,
        blue_color,
        (
            enemies_pos
        )
    )
