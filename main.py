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
     "...................C....................",
     "."*40,
     "...............S...S....................",
     "..............#######...................",
     "."*40,
     "."*40,
     "..........S................S............",
     ".........###.............###............",
     "..........s.............................",
     "."*40,
     "................................S.......",
     "..P...S........................###......",
     "..#######.............................SE",
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
start=[]
rot=False
rspikes=[]
end=[]

screen= pygame.display.set_mode((800,450))

game_running=True
jump=False

player_img= pygame.image.load("images/Main Characters\minja Frog\Idle (32x32).png").convert_alpha()
player_img = pygame.transform.scale(player_img,(32,32))

bg= pygame.image.load("images/Background/bg2.png").convert_alpha()
bg = pygame.transform.scale(bg,(800,450))

bg2= pygame.image.load("images/Background/bg.png").convert_alpha()
bg2 = pygame.transform.scale(bg2,(800,450))

blockimg = pygame.image.load("images/Blocks/Idle.png").convert_alpha()
blockimg = pygame.transform.scale(blockimg,(20,20))

spikeimg = pygame.image.load("images/Blocks/spike.png").convert_alpha()
spikeimg = pygame.transform.scale(spikeimg,(20,20))

rspikeimg = pygame.transform.flip(spikeimg,False,True)

startimg = pygame.image.load("images/Blocks/Start.png").convert_alpha()
startimg = pygame.transform.scale(startimg,(40,40))


coinimg = pygame.image.load("images/Items/Apple.png").convert_alpha()
coinimg = pygame.transform.scale(coinimg,(40,40))

endimg= pygame.image.load("images/Blocks/End.png").convert_alpha()
endimg = pygame.transform.scale(endimg,(40,40))

bgsound= pygame.mixer.Sound("sounds/bg.ogg")
bgsound.set_volume(0.6)
jumpsound= pygame.mixer.Sound("sounds/jump.ogg")
jumpsound.set_volume(0.8)

deathsfx= pygame.mixer.Sound("sounds/death1.ogg")
deathsfx.set_volume(0.8)
revivesfx= pygame.mixer.Sound("sounds/revive.ogg")
revivesfx.set_volume(0.8)

bgsound.play(-1)

running=True

death=False
levelno=0

timer=0
g=5
clock = pygame.time.Clock()
fps=20

for y,line in enumerate(levels[levelno]):
        for x,c in enumerate(line):
            if c=="#":
                blocks.append(pygame.Rect(x*size,y*size,size,size))
            elif c=="S":
                spikes.append(pygame.Rect(x*size,y*size,size,size))            
            elif c=="C":
                coins.append(pygame.Rect(x*size,y*size,size,size))
            elif c=="P":
                playerreturnx=x*size
                playerreturny=y*size
                player=pygame.Rect(x*size,y*size-15,32,32)
                start.append(pygame.Rect(x*size,y*size-20,size,size))
            elif c=="s":
                rspikes.append(pygame.Rect(x*size,y*size,size,size))
            elif c=="E":
                end.append(pygame.Rect(x*size,y*size-20
                                       ,size,size))


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    timer+=1

    press=pygame.key.get_pressed()
    if press[pygame.K_w] or press[pygame.K_UP]:
        if not in_air:
            player.y-=10
            jump=True
            timer=0
            in_air=True
            g=0
            jumpsound.play()

    if not rot:
        player_img=pygame.transform.flip(player_img,False,False)
    else:
        player_img=pygame.transform.flip(player_img,True,False)

    if press[pygame.K_a] or press[pygame.K_LEFT]:
        rot=True
        player.x-=9
    if press[pygame.K_d] or press[pygame.K_RIGHT]:
        player.x+=9
        rot=False
    
    player.y+=g
    g+=0.8

    screen.fill((20,20,40))
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))

    screen.blit(player_img,player)
    in_air=True
    for b in blocks:
        screen.blit(blockimg,b)        
        if player.colliderect((b.x,b.y,b.h,b.w)):
            if player.bottom<=b.top+20 and player.left<=b.right+20 and player.right>=b.left-20:
                g=0
                player.bottom=b.top+1
                jump=False
                in_air=False
                player_img= pygame.image.load("images/Main Characters\minja Frog\Idle (32x32).png").convert_alpha()

            else:
                g=0
                player.y+=(40-g*5)+8

    if jump:
        if (40-g*5)>0:
            player_img= pygame.image.load("images/Main Characters\minja Frog\Jump (32x32).png").convert_alpha()
        elif (40-g*5)<0:
            player_img= pygame.image.load("images/Main Characters\minja Frog\Fall (32x32).png").convert_alpha()

        player.y-=(40-g*5)

    for s in spikes:
        screen.blit(spikeimg,s)
        if player.colliderect(s):
            death=True
            timer=0
            deathsfx.play()
            player.y-=(10000+g*5)
            g=0

    for rs in rspikes:
        screen.blit(rspikeimg,rs)
        if player.colliderect(rs) and not death:
            timer=0
            death=True
            player.y-=(10000+g*5)
            g=0
            deathsfx.play()

    if timer>fps*1.5 and death:
        g=0
        revivesfx.play()
        death=False
        player=pygame.Rect(playerreturnx,playerreturny,32,32)


    for st in start:
        screen.blit(startimg,st)

    for c in coins:
        screen.blit(coinimg,(c.x-10,c.y,c.h,c.w))
        if player.colliderect(c):
            print("TRUE")

    for e in end:
        screen.blit(endimg,e)

    if (player.x>800):
        player.x=780
    if (player.x<0):
        player.x=10

    pygame.display.flip()
    clock.tick(20)
pygame.quit()