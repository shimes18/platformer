import pygame

pygame.init()

size=20

# C= coin , S = Spikes, #=platform , P = Player

levels=[
    ["B"*40,
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B.................C....................B",
     "B"+"."*38+"B",
     "B..............SSSS....................B",
     "B.............#######..................B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B.........S................S...........B",
     "B........###.............###...........B",
     "B.........s............................B",
     "B"+"."*38+"B",
     "B...............................S......B",
     "B.P...S........................###.....B",
     "B.#######............................SEB",
     "B......................................B",
     "B"+"."*38+"B",
     "BSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSB",
     "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
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
border=[]

screen= pygame.display.set_mode((800,450))

game_running=True
jump=False

player_img= pygame.image.load("images/Main Characters\minja Frog\Idle (32x32).png").convert_alpha()
player_img = pygame.transform.scale(player_img,(23,26))

bg= pygame.image.load("images/Background/bg2.png").convert_alpha()
bg = pygame.transform.scale(bg,(800,450))

bg2= pygame.image.load("images/Background/bg.png").convert_alpha()
bg2 = pygame.transform.scale(bg2,(800,450))

blockimg = pygame.image.load("images/Blocks/Idle.png").convert_alpha()
blockimg = pygame.transform.scale(blockimg,(20,20))

borderimg = pygame.image.load("images/Blocks/border.png").convert_alpha()
borderimg = pygame.transform.scale(borderimg,(20,20))

borderimg=pygame.transform.rotate(borderimg,90)


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

textbg=["."*40,
     "."*40,
     "."*40,
     "."*40,
     "."*40,
     "########################################",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "#"+"."*38+"#",
     "########################################",
     "."*40,
     "."*40,
     "."*40,
     "."*40,
     "."*40,
    ]

running=True

death=False
levelno=0

tblocks=[]
timer=0
g=5
clock = pygame.time.Clock()
level_finish=False
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
                player=pygame.Rect(x*size,y*size,32,32)
                start.append(pygame.Rect(x*size,y*size-20,size,size))
            elif c=="s":
                rspikes.append(pygame.Rect(x*size,y*size,size,size))
            elif c=="E":
                end.append(pygame.Rect(x*size,y*size-20,size,size))
            elif c=="B":
                border.append(pygame.Rect(x*size,y*size,size,size))

for y,line in enumerate(textbg):
    for x,c in enumerate(line):
        if c=="#":
            tblocks.append(pygame.Rect(x*size,y*size,size,size))


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    timer+=1
    screen.fill((20,20,40))
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))

    screen.blit(player_img,player)
    if not level_finish:
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


        in_air=True
        for b in blocks:
            screen.blit(blockimg,b)        
            if player.colliderect((b.x,b.y,b.h,b.w)):
                if player.bottom<=b.top+20 and player.left<=b.right+20 and player.right>=b.left-20:
                    g=0
                    player.bottom=b.top+1
                    jump=False
                    in_air=False
                    player_img= pygame.image.load("images/Main Characters/Idle (32x32).png").convert_alpha()

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
                g=2
                death=True
                timer=0
                deathsfx.play()
                player.y+=(15+g*5)
                g=0

        for rs in rspikes:
            screen.blit(rspikeimg,rs)
            if player.colliderect(rs) and not death:
                timer=0
                death=True
                player.y+=(15+g*5)
                g=0
                deathsfx.play()
        
        if timer>fps and death:
            revivesfx.play()

        if timer>fps*1.5 and death:
            g=0


            player=pygame.Rect(playerreturnx,playerreturny,32,32)
            death=False



        for st in start:
            screen.blit(startimg,st)

        for c in coins:
            screen.blit(coinimg,(c.x-10,c.y,c.h,c.w))
            if player.colliderect(c):
                print("TRUE")

        for e in end:
            screen.blit(endimg,e)
            if player.colliderect(e):
                level_finish=True

        for b in border:
            screen.blit(borderimg,b)

        if (player.x>780):
            player.x=780
        if (player.x<20):
            player.x=20
        if (player.y<=20):
            g=0
            player.y=30

        if (player.y>430):
            player=pygame.Rect(playerreturnx,playerreturny,32,32)


    if level_finish:
        for lf in tblocks:
            screen.blit(blockimg,lf)        

    pygame.display.flip()
    clock.tick(20)
pygame.quit()