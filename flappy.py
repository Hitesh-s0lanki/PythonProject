import random
import pygame
import sys

setWidth=289
setHeight=511
white= (255, 255, 255)
pygame.init()

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakegreen = (35, 45, 40)

#creating the Window
bg1=pygame.image.load('gallery/sprites/background.png')
bg2=pygame.image.load('gallery/sprites/base.png')

game_display=pygame.display.set_mode((setWidth,setHeight))
pygame.display.set_caption("Flappy Game")
game_display.blit(bg1,(0,0))
game_display.blit(bg2,(0,400))
pygame.display.update()

#Game Control Unit
clock=pygame.time.Clock()
fps=32
Game_Over=False
Game_Quit=False


#Build pipe
def pipeBuild(pipe_list):
    pipe=pygame.image.load('gallery/sprites/pipe.png').convert_alpha()
    pipe2=pygame.image.load('gallery/sprites/reverse.png').convert_alpha()
    for pipe_x,pipe_y in pipe_list:
        game_display.blit(pipe,(pipe_x,pipe_y))
        game_display.blit(pipe2,(pipe_x,-1*(320-(pipe_y-120))))
        pygame.display.update()

font=pygame.font.SysFont(None,30)

def textFormate(text,color,x,y):
    screen_text = font.render(text, True, color)
    game_display.blit(screen_text, [x,y])

def GameLoop():
    Game_Over=False
    Game_Quit=False
    #Bird Location
    bird_x=80
    bird_y=170
    #pipe List
    pipe_list=[]
    pipe_no=1
    bg1=pygame.image.load('gallery/sprites/background.png')
    bg2=pygame.image.load('gallery/sprites/base.png')
    bg4=pygame.image.load('gallery/sprites/bird.png').convert_alpha()
    while not Game_Quit:
        velocity_y=30
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Game_Quit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    velocity_y=-40
        if len(pipe_list)<pipe_no or (len(pipe_list)!=0 and pipe_list[-1][0]<=setWidth/2):
            pipe_x=setWidth-20
            pipe_y=random.randint(120,390) 
            temp=[]
            temp.append(pipe_x)
            temp.append(pipe_y)
            pipe_list.append(temp)

        if bird_y in pipe_list and bird_x in pipe_list:
            game_display.blit(bg1,(0,0)) 
            game_display.blit(bg2,(0,400)) 
            textFormate('Game Over',red,200,200)
            break

        bird_y=bird_y+velocity_y
        for x in pipe_list:
            x[0]=x[0]-10

        game_display.blit(bg1,(0,0)) 
        pipeBuild(pipe_list)
        game_display.blit(bg2,(0,400)) 
        game_display.blit(bg4,(bird_x,bird_y))
        pygame.display.update()
        
        clock.tick(5)


            

def welcome():
    Game_Over=False
    Game_Quit=False
    bg3=pygame.image.load('gallery/sprites/message.png')
    game_display.blit(bg3,(50,90))
    pygame.display.update()
    while not Game_Quit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Game_Quit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    GameLoop()
                
        clock.tick(fps)

welcome()



pygame.quit()
quit() 