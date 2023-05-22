import pygame

pygame.init()
#screen display
Screen_width=800
Screen_height=533
bg1=pygame.image.load("snakeimage/space.png")
game_display=pygame.display.set_mode((Screen_width,Screen_height))
game_display.blit(bg1,(0,0))
pygame.display.update()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakegreen = (35, 45, 40)


#Game condition
Game_Over=False

#SpaceShip coordinate
Space_x=350
Space_y=400

#Game and Control Unit
fps=30
clock=pygame.time.Clock()


#bullet
bullet_list=[]
def printBullet(bullet_list,bg3):
    for x,y in bullet_list:
        if not y<0:
            game_display.blit(bg3,(x,y))


#ufo 
ufo_list=[]
start_x=0
start_y=30
for i in range(10):
    ufo_list.append([start_x,start_y,True])
    start_x+=40

def print_ufo(ufo_list,bg4):
    for x,y,z in ufo_list:
        game_display.blit(bg4,(x,y))

#not display space ship
def checkDestory():
    for c in ufo_list:
        for i in range(1,41):
            if [abs(c[0]+i),abs(c[1]+i)] in bullet_list:
                ufo_list.remove(c)
                break
            elif [abs(c[0]+i),abs(c[1])] in bullet_list:
                ufo_list.remove(c)
                break
            elif [abs(c[0]),abs(c[1]+i)] in bullet_list:
                ufo_list.remove(c)
                break

while not Game_Over:
    velocity_x=0
    bg2=pygame.image.load("snakeimage/spaceship.png")
    bg3=pygame.image.load("snakeimage/bullet.png")
    bg4=pygame.image.load("snakeimage/ufo.png")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Game_Over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                velocity_x=-20
            if event.key==pygame.K_d:
                velocity_x=20
            if event.key==pygame.K_SPACE:
                bullet_list.append([Space_x+15,Space_y])
            Space_x=Space_x+velocity_x
    for x in bullet_list:
        x[1]=x[1]-5
    for c in ufo_list:
        if c[2]:
            c[0]=c[0]+5
        else:
            c[0]=c[0]-5
        if c[0]>=760 or c[0]<=0:
            c[2]=not c[2]
            c[1]+=40
    if len(ufo_list)==0:
        Game_Over=True
    if [Space_x,Space_y] in ufo_list:
        Game_Over=True
        print("You Lose")
        quit()
    checkDestory()

    game_display.blit(bg1,(0,0))
    game_display.blit(bg2,(Space_x,Space_y))
    printBullet(bullet_list,bg3)
    print_ufo(ufo_list,bg4)
    pygame.display.update()
    clock.tick(fps)

  
print("you Won")

pygame.quit()
quit()