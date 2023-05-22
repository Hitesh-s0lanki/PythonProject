import pygame
import random
pygame.init()

#Variable 
Screen_size=900
Screen_heigth=600

#Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
snakegreen = (35, 45, 40)



#Time and Control Unit
clock=pygame.time.Clock()
fps=10         #Speed of game
font = pygame.font.SysFont(None, 55)


#Cooridnate of Snake
snake_x=90
snake_y=90
snake_Size=30




pygame.display.set_caption("Snake Game")
Game_Display=pygame.display.set_mode((Screen_size,Screen_heigth))
pygame.display.update()

#condition for end 
Game_Over=False
Game_Quit=False

    

#food of Snake
food_x=random.randint(30,Screen_size-30)
while food_x%30!=0:
    food_x=random.randint(30,Screen_size-30)
food_y=random.randint(30,Screen_heigth-30)
while food_y%30!=0:
    food_y=random.randint(30,Screen_heigth-30)  

#Velocity of Snake
velocity_x=0
velocity_y=0


#For moment of tail
snake_list=[]
snake_len=1

#score Board
score=0
highscore=0
with open("hiscore.txt",'r') as f:
    highscore=f.read()

#Function for writing text
def textFormate(text,color,x,y):
    screen_text = font.render(text, True, color)
    Game_Display.blit(screen_text, [x,y])


#function for Drawing rect
def draw(Game_Display,color,snake_list,snake_Size):
    for x,y in snake_list:
        pygame.draw.rect(Game_Display,color,[x,y,snake_Size,snake_Size])

while not Game_Quit:
    if Game_Over:
        Game_Display.fill(white)
        textFormate("Game Over ",red,250,250)
        textFormate("play again press Enter",red,200,280)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Game_Over=True
                Game_Quit=True 
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    Game_Over=False
                    snake_x=90
                    snake_y=90
                    velocity_x=0
                    velocity_y=0
                    snake_list=[]
                    snake_len=1
                else:
                    Game_Quit=True 
    else:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Game_Quit=True 
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    velocity_x=0
                    velocity_y=-30
                if event.key==pygame.K_s:
                    velocity_x=0
                    velocity_y=30
                if event.key==pygame.K_d:
                    velocity_x=30
                    velocity_y=0
                if event.key==pygame.K_a:
                    velocity_x=-30
                    velocity_y=0
        snake_x=snake_x+velocity_x
        snake_y=snake_y+velocity_y
        

        if snake_x<=0 or snake_y<=0 or snake_x>= Screen_size or snake_y>=Screen_heigth:
            Game_Over=True
        
        head=[]
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)

        if len(snake_list)>snake_len:
            del snake_list[0]

        if head in snake_list[:-1]:
            Game_Over = True

        if abs(snake_x-food_x)==0 and abs(snake_y-food_y)==0:
            food_x=random.randint(30,Screen_size-30)
            while food_x%30!=0:
                food_x=random.randint(0,Screen_size-30)
            food_y=random.randint(30,Screen_heigth-30)
            while food_y%30!=0:
                food_y=random.randint(0,Screen_heigth-30)  
            snake_len+=1
            score+=10

        if score>int(highscore):
            highscore=score

        Game_Display.fill(white)
        textFormate("Score="+ str(score),red,10 ,10)
        textFormate("HighScore="+ str(highscore),red,200 ,10)
        draw(Game_Display,red,[[food_x,food_y]],snake_Size)
        draw(Game_Display,black,snake_list,snake_Size)

    pygame.display.update()
    clock.tick(fps)

if score>=int(highscore):
    with open("hiscore.txt",'w') as f:
        f.write(str(score))

pygame.quit()
quit()