import pygame

pygame.init()

size=32

# C= coin , S = Spikes, #=platform , P = Player

levels=[
    ["........................................",
     "........................................",
     "..................C.....................",
     "...............S...S....................",
     "..............#######...................",
     "..P............................###.......",
     "..#######.............................E.",
     "........................................",
     "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS",
    ]
]


blocks=[]
spikes=[]
coins=[]
rot=False

screen= pygame.display.set_mode((800,450))

game_running=True

player = pygame.Rect(80,300,32,32)

player_img= pygame.image.load("images/Main Characters\minja Frog\Idle (32x32).png").convert_alpha()
player_img = pygame.transform.scale(player_img,(32,32))

running=True

levelno=0

clock = pygame.time.Clock()

def load(levelno):
    platform , spikes,coin,start,exit=[],[],[],(80,300),(700,350)
    for y,line in enumerate(levels):
        for x,c in enumerate(line):
            if c=="#":
                blocks.append(pygame.Rect(x*size,y*size,size,size))
            if c=="S":
                spikes.append(pygame.Rect(x*size,y*size,size,size))            
            if c=="C":
                coins.append(pygame.Rect(x*size,y*size,size,size))


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    press=pygame.key.get_pressed()
    if press[pygame.K_w]:
        player.y-=15    

    if press[pygame.K_a]:
        if not rot:
            player_img=pygame.transform.flip(player_img,True,False)
            
            rot=True
        player.x-=15    
    if press[pygame.K_d]:
        player.x+=15
        if rot:
            player_img=pygame.transform.flip(player_img,True,False)
            rot=False
    

    screen.fill((20,20,40))
    screen.blit(player_img,player)
    for b in blocks:
        pygame.draw.rect(screen,(255,255,255),(b.w,b.h))

    pygame.display.flip()
    clock.tick(20)
pygame.quit()