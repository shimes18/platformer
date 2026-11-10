import pygame

pygame.init()

size=20

font = pygame.font.Font(None,32)

# C= coin , S = Spikes, #=platform , P = Player

levels=[
    ["."*40,
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B.................C....................B",
     "B"+"."*38+"B",
     "B..............S..S....................B",
     "B.............#######..................B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B.........S................S...........B",
     "B........###.............###...........B",
     "B........ss............................B",
     "B"+"."*38+"B",
     "B...............................S......B",
     "B.P...S........................###.....B",
     "B.#####...............................EB",
     "B....................................S.B",
     "B"+"."*38+"B",
     "BSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSB",
     "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    ],
    ["."*40,
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B.................C....................B",
     "B"+"."*38+"B",
     "B..............S..S....................B",
     "B..P..........#######..................B",
     "B.#####..............................S.B",
     "B"+"."*38+"B",
     "B"+"."*38+"B",
     "B.........S................S...........B",
     "B........###.............###...........B",
     "B........ss............................B",
     "B"+"."*38+"B",
     "B...............................S.....EB",
     "B.....S........................###.....B",
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
rot="Temp"
rspikes=[]
end=[]
border=[]
hp=1

screen= pygame.display.set_mode((800,450))

bgtext=[]

game_running=True
jump=False

player_img= pygame.image.load("images/Main Characters\Idle (32x32).png").convert_alpha()
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

hpimg = pygame.image.load("images/Items/heart.png").convert_alpha()
hpimg = pygame.transform.scale(hpimg,(15.75,13.5))

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
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
     "#"+"C"*38+"#",
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
level_finish=True
fps=20
playerreturnx=0
playerreturny=0

def load(levelno):
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
                    player=pygame.Rect(x*size,y*size,23,26)
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
            if c=="C":
                bgtext.append(pygame.Rect(x*size,y*size,size,size))


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if level_finish and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                level_finish=False
            if event.key==pygame.K_n:
                levelno+=1
                level_finish=False
            if event.unicode.isdigit():
                    levelno= int(event.unicode)-1
                    level_finish=False
                    player=pygame.Rect(playerreturnx,playerreturny-10,23,26)
                    load(levelno)
            print(levelno)
        

    timer+=1
    screen.fill((20,20,40))
    screen.blit(bg,(0,0))
    screen.blit(bg2,(0,0))

    if not level_finish:
        press=pygame.key.get_pressed()
        if press[pygame.K_w] or press[pygame.K_UP]:
            if not in_air and not death:
                player.y-=10
                jump=True
                timer=0
                in_air=True
                g=0
                jumpsound.play()


        if press[pygame.K_a] or press[pygame.K_LEFT]:
            if not death:
                rot="True"
                player.x-=9
        if press[pygame.K_d] or press[pygame.K_RIGHT]:
            if not death:
                rot="False"
                player.x+=9
        
        player.y+=g
        g+=0.8

        if rot=="True":
            img=pygame.transform.flip(player_img,True,False)
        else:
            img= player_img


        screen.blit(img,player)

        in_air=True
        for b in blocks:
            screen.blit(blockimg,b)        
            if player.colliderect((b.x,b.y,b.h,b.w)):
                if player.bottom<=b.top+20 and player.left<=b.right+20 and player.right>=b.left-20:
                    g=0
                    player.bottom=b.top+1
                    jump=False
                    in_air=False
                    img= pygame.image.load("images/Main Characters/Idle (32x32).png").convert_alpha()

                else:
                    g=0
                    player.y+=(40-g*5)+8

        if jump:
            if (40-g*5)>0:
                img= pygame.image.load("images/Main Characters\minja Frog\Jump (32x32).png").convert_alpha()
            elif (40-g*5)<0:
                img= pygame.image.load("images/Main Characters\minja Frog\Fall (32x32).png").convert_alpha()

            player.y-=(40-g*5)

        for s in spikes:
            screen.blit(spikeimg,s)
            pygame.draw.rect(screen,(0,0,0),s,2)
            if player.colliderect(s) and not death:
                player.y-=75
                g=2
                timer=0
                deathsfx.play()
                player.y+=(55+g*5)
                hp-=1
                


        for rs in rspikes:
            screen.blit(rspikeimg,rs)
            if player.colliderect(rs) and not death:
                g=2
                timer=0
                deathsfx.play()
                player.y+=(55+g*5)
                hp-=1

        if hp<=0:
            death=True
        
        if timer>0.8*fps and death:
            revivesfx.play()

        if timer>fps*1.5 and death:
            g=0
            player=pygame.Rect(playerreturnx,playerreturny-10,23,26)
            hp+=1
            g=0
            death=False



        for st in start:
            screen.blit(startimg,st)

        for c in coins:
            screen.blit(coinimg,(c.x-10,c.y,c.h,c.w))
            if player.colliderect(c):
                print("TRUE")
                c.x=1000
                hp+=1

        for e in end:
            screen.blit(endimg,e)
            if player.colliderect(e):
                level_finish=True

        for b in border:
            screen.blit(borderimg,b)
            if player.colliderect(b):
                if player.x>300: 
                    player.x-=5
                elif player.x<200:
                    player.x+=5
                elif player.y<200:
                    player.y+=5

        if player.y>2050:
            death=True


        pygame.draw.rect(screen,(0,0,0),player,2)

        for i in range(hp):
            screen.blit(hpimg,(i*20+1,0,20,20))
        

    if level_finish:
        lft= font.render("Level "+ str(levelno+1) + " complete",True,(0,0,0))
        nlt= font.render("Press N to go to next level",True,(0,0,0))
        rlt= font.render("Press R to Replay level",True,(0,0,0))
        clt= font.render("Press the level you want to go to on keyboard (1-9)",True,(0,0,0))
        rspikes.clear()
        blocks.clear()
        end.clear()
        border.clear()
        coins.clear()
        start.clear()
        player.clear()

        for lf in tblocks:
            screen.blit(blockimg,lf)    
        for C in bgtext:
            pygame.draw.rect(screen,(255,255,255),C)  
        screen.blit(lft,(290,130))
        screen.blit(nlt,(250,180))
        screen.blit(rlt,(265,230))
        screen.blit(clt,(130,280))

    pygame.display.flip()
    clock.tick(20)
pygame.quit()