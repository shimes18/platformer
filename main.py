import pygame

pygame.init()

screen= pygame.display.set_mode((800,450))

player = pygame.Rect(80,300,32,32)

player_img= pygame.image.load("Main Characters\minja Frog\Idle (32x32).png").convert_alpha()
player_img = pygame.transform.scale(player_img,(32,32))

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill((20,20,40))
    screen.blit(player_img,player)

    pygame.display.flip()
pygame.quit()