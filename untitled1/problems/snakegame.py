import pygame
import time
import random
pygame.init()
dis_width=800
dis_height=500

white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
yellow=(255,255,102)
green=(0,255,0)
orange=(255,165,0)

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption("Adi_Rock_11")
clock=pygame.time.Clock()

snake_block=13
snake_speed=16

font_style = pygame.font.SysFont(None,25)
score_font=pygame.font.SysFont(italic=True,name="comicsansms",size=25)

def your_score(score):
    value=score_font.render("Your Score: " +str(score),True,green)
    dis.blit(value,[0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.circle(dis,red,[x[0],x[1]],8,3)

def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[int(dis_width/6),int(dis_height/3)])

def gameLoop():
    over=False
    close=False

    x1 = int(dis_width / 2)
    y1 = int(dis_height / 2)

    x1_change = 0
    y1_change = 0
    snake_list=[]
    length_of_snake=1

    foodx=round(random.randrange(0,int(dis_width-snake_block))/10)*10
    foody = round(random.randrange(0, int(dis_height - snake_block)) / 10) * 10

    while not(over):
        while close==True:
            dis.fill(white)
            message("You Lost ! Prees Q-Quit or C-play again",red)
            your_score(length_of_snake -1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        over=True
                        close=False
                    elif event.key==pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-10
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=10
                    y1_change=0
                elif event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-10
                elif event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=10


        x1 +=x1_change
        y1 +=y1_change
        dis.fill(blue)

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            close=True

        pygame.draw.circle(dis,yellow,[foodx,foody],7,7)
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list)>length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x==snake_head:
                close=True

        our_snake(snake_block,snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx=int(round(random.randrange(0,dis_width - snake_block)/10.0)*10.0)
            foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
            length_of_snake +=1

        clock.tick(snake_speed)


    time.sleep(2)
    pygame.quit()
    quit()
    
gameLoop()