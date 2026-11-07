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
     ".........##..............###............",
     "."*40,
     "."*40,
     "."*40,
     "..P............................###......",
     "..#######.............................E.",
     "........................................",
     "."*40,
     "."*40,
     "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
    ]
]

in_air=False
blocks=[]
spikes=[]
coins=[]
rot=False

screen= pygame.display.set_mode((800,450))

game_running=True
jump=False

player_img= pygame.image.load("images/Main Characters\minja Frog\Idle (32x32).png").convert_alpha()
player_img = pygame.transform.scale(player_img,(32,32))

blockimg = pygame.image.load("images/Blocks/Idle.png").convert_alpha()
blockimg = pygame.transform.scale(blockimg,(20,20))


running=True

levelno=0

timer=0
g=5
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
        if not in_air:
            player.y-=10
            jump=True
            timer=0
            in_air=True
            g=0


    if press[pygame.K_a] or press[pygame.K_LEFT]:
        if not rot:
            player_img=pygame.transform.flip(player_img,True,False)
            
            rot=True
        player.x-=8
    if press[pygame.K_d] or press[pygame.K_RIGHT]:
        player.x+=8
        if rot:
            player_img=pygame.transform.flip(player_img,True,False)
            rot=False
    
    player.y+=g
    g+=0.1

    screen.fill((20,20,40))

    screen.blit(player_img,player)

    for b in blocks:
        screen.blit(blockimg,b)        
        if player.colliderect((b.x,b.y,b.h,b.w)):
            if player.bottom<=b.top+20 and player.left<=b.right+20 and player.right>=b.left-20:
                g=0
                player.bottom=b.top+1
                jump=False
                in_air=False
            else:
                g=2
                player.y+=(10-g*5)+8

    if jump:
        player.y-=(10-g*5)


    pygame.display.flip()
    clock.tick(20)
pygame.quit()