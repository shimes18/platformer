import pygame

pygame.init()

size=20

# C= coin , S = Spikes, #=platform , P = Player

levels=[
    ["."*40,
     "."*40,
     "."*40,
     "."*40,
     "."*40,
     "..................C.....................",
     "."*40,
     "...............S...S....................",
     "..............#######...................",
     "."*40,
     "."*40,
     ".........S..............................",
     ".........##.............................",
     "."*40,
     "."*40,
     "."*40,
     "..P............................###.......",
     "..#######.............................E.",
     "........................................",
     "."*40,
     "."*40,
     "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
    ]
]


blocks=[]
spikes=[]
coins=[]
rot=False

screen= pygame.display.set_mode((800,450))

game_running=True


player_img= pygame.image.load("images/Main Characters\minja Frog\Idle (32x32).png").convert_alpha()
player_img = pygame.transform.scale(player_img,(32,32))

running=True

levelno=0

clock = pygame.time.Clock()


for y,line in enumerate(levels[levelno]):
        for x,c in enumerate(line):
            if c=="#":
                blocks.append(pygame.Rect(x*size,y*size,size,size))
            elif c=="S":
                spikes.append(pygame.Rect(x*size,y*size,size,size))            
            elif c=="C":
                coins.append(pygame.Rect(x*size,y*size,size,size))
            elif c=="P":
                player=pygame.Rect(x*size,y*size-15,32,32)


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    press=pygame.key.get_pressed()
    if press[pygame.K_w] or press[pygame.K_UP]:
        player.y-=45    

    if press[pygame.K_a] or press[pygame.K_LEFT]:
        if not rot:
            player_img=pygame.transform.flip(player_img,True,False)
            
            rot=True
        player.x-=15    
    if press[pygame.K_d] or press[pygame.K_RIGHT]:
        player.x+=15
        if rot:
            player_img=pygame.transform.flip(player_img,True,False)
            rot=False
    
    player.y+=10

    screen.fill((20,20,40))

    screen.blit(player_img,player)

    for b in blocks:
        pygame.draw.rect(screen,(255,255,255),b)
        if player.colliderect((b.x,b.y-10,b.h,b.w)):
            player.y-=10

    pygame.display.flip()
    clock.tick(20)
pygame.quit()