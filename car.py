import pygame
pygame.init()
import random
import math
import time

#-------setup the screen----
wn=pygame.display.set_mode((798,600))
pygame.display.set_caption('Crazy Car Game')
logo=pygame.image.load('car.png')
pygame.display.set_icon(logo)
bg=pygame.image.load('bg.png')

#-------variable-----
counttime=3
fps=100
clock=pygame.time.Clock()

over=pygame.font.Font('freesansbold.ttf',42)
countdown=pygame.font.Font('freesansbold.ttf',42)

#----font of text----
font_crash=pygame.font.Font('freesansbold.ttf',72)
crash_x=270
crash_y=300


#score ---
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

#Background music----

#Adding main car----
car=pygame.image.load('car.png')

#Adding car1---- 
car1=pygame.image.load('car1.jpeg')

#Adding car1----   
car2=pygame.image.load('car2.png')

#Adding car3----
car3=pygame.image.load('car3.png')

#functions---
def picture(x,y):
        wn.blit(car,(x,y))

def picture1(x,y):
        wn.blit(car1,(x,y))

def picture2(x,y):
        wn.blit(car2,(x,y))

def picture3(x,y):
        wn.blit(car3,(x,y))

def show_score(x,y):
        score_font=font.render("Score :"+str(score_value),True,(255,255,255))
        wn.blit(score_font,(x,y))
       
       

def show_crash(x,y):
        crash=font.render("Car Crashed!",True,(255,255,0))
        wn.blit(crash,(x,y))
       

def font_crash(x,y):
        crash=font.render("Car Crashed!,Press Enter to Continue",True,(255,255,255))
        wn.blit(crash,(x,y))

def iscollision(car_x,car_y,car1_x,car1_y):
        distance=math.sqrt((math.pow(car_x-car1_x,2))+(math.pow(car_y-car1_y,2)))
        if distance <60:
            return True
        else:
            return False

def iscollision(car_x,car_y,car2_x,car2_y):
        distance=math.sqrt((math.pow(car_x-car2_x,2))+(math.pow(car_y-car2_y,2)))
        if distance <60:
            return True
        else:
            return False

def iscollision(car_x,car_y,car3_x,car3_y):
        distance=math.sqrt((math.pow(car_x-car3_x,2))+(math.pow(car_y-car3_y,2)))
        if distance <60:
            return True
        else:
            return False

def over_font(x,y):
    over_font=font.render("Press Enter to continue",True,(0,255,0))
    wn.blit(over_font,(x,y))
   
def countdown(x,y):
    count=font.render("Crazy Car Game, Start in :" + str(counttime)+"...",True,(255,0,0))
    wn.blit(count,(x,y))


#------main loop-----
def gameloop():
     
        car3_x=290
        car3_y=-600
        car3_xchange=0
        car3_ychange=7
        car2_x=290
        car2_y=-250
        car2_xchange=0
        car2_ychange=7
        car1_x=290
        car1_y=-400
        car1_xchange=0
        car1_ychange=7
        car_x=290
        car_y=498
        car_xchange=0
        car_ychange=0
        score_x=580
        score_y=280
        game_exit = False
        game_over=False
        global score_value
        score_value=0
        over_x=200
        over_y=450
        font_crash_x=200
        font_crash_y=300
        pygame.mixer.music.load('background.wav')
        pygame.mixer.music.play(-1)


        while not game_exit:
         
           
            if game_over:
                over_font(over_x,over_y)
                time.sleep(2)
               
               
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                            game_exit=True
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                                gameloop()
                     

                               
               
            else:
                   
                    wn.blit(bg,(0,0))
                    for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                game_exit=True
                           
                            #-----key to control the car----
                            if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_RIGHT:
                                    car_xchange=4
                                if event.key==pygame.K_LEFT:
                                    car_xchange=-4
                               
                               
                   
                    car_x+=car_xchange
                    car_y+=car_ychange

                     # car continues come form random place--

                    car1_y+=car1_ychange
                    car1_ychange=9
                    if car1_y>600:
                       
                        car1_y=-100
                        car1_x=random.randint(250,485)
                        car1_ychange=9
                        score_value+=1
                   
                       
                           
                    car2_y+=car2_ychange
                    car2_ychange=9
                    if car2_y>600:
                       
                        car2_y=-100
                        car2_x=random.randint(230,485)
                        car2_ychange=9
                        score_value+=1
                        pygame.display.update()
                       
                               
                    car3_y+=car3_ychange
                    car3_ychange=9
                    if car3_y>600:
                       
                        car3_y=-100
                        car3_x=random.randint(210,485)
                        car3_ychange=9
                        score_value+=1
                        pygame.display.update()
                       
                           
                    collision1=iscollision(car_x,car_y,car1_x,car1_y)
                    collision2=iscollision(car_x,car_y,car2_x,car2_y)
                    collision3=iscollision(car_x,car_y,car3_x,car3_y)
                   
               
                   
                   
                     #call the functions--
                    show_score(score_x,score_y)
                    picture1(car1_x,car1_y)
                    picture2(car2_x,car2_y)
                    picture3(car3_x,car3_y)
                    picture(car_x,car_y)

                     #collision with boundaries--
                     #-x-coordinate
                    if car_x<185:
                   
                        pygame.mixer.music.stop()
                        car_x=185
                        wn.fill((255,0,255))
                       
                        car1_y=0
                        car2_y=0
                        car3_y=0
                        car1_ychange=0
                        car2_ychange=0
                        car3_ychange=0
                        car_x=0
                        car_xchange=0
                        car_x=0
                        car_xchange=0
                        show_score(310,350)
                       
                        game_over=True
                        pygame.display.update()
                       
                       
                       
                     #x-coordinate---
                    elif car_x>483:
                           
                           
                           
                            pygame.mixer.music.stop()
                            car_x=483
                           
                           
                            wn.fill((255,0,255))
                            car1_y=0
                            car2_y=0
                            car3_y=0
                            car1_ychange=0
                            car2_ychange=0
                            car3_ychange=0
                            car_x=0
                            car_xchange=0
                            car_x=0
                            car_xchange=0
                            show_crash(crash_x,crash_y)
                            show_score(310,350)
                           
                            game_over=True
                            pygame.display.update()
                           
                           
                           
                    elif collision1:
                            wn.fill((255,0,255))
                           
                            pygame.mixer.music.stop()
                            crash_Sound=pygame.mixer.Sound("car_crash.wav")
                            crash_Sound.play(0)
                            car1_y=0
                            car2_y=0
                            car3_y=0
                            car1_ychange=0
                            car2_ychange=0
                            car3_ychange=0
                            car_x=0
                            car_xchange=0
                            show_crash(crash_x,crash_y)
                            show_score(310,350)
                           
                           
                           
                            game_over=True
                            pygame.display.update()
                       
                    elif collision2:

                            wn.fill((255,0,255))
                           
                            pygame.mixer.music.stop()
                            crash_Sound=pygame.mixer.Sound("car_crash.wav")
                            crash_Sound.play(0)
                            car1_y=0
                            car2_y=0
                            car3_y=0
                            car1_ychange=0
                            car2_ychange=0
                            car3_ychange=0
                            car_x=0
                            car_xchange=0
                            show_crash(crash_x,crash_y)
                            show_score(310,350)
                           
                           
                           
                            game_over=True
                            pygame.display.update()
                           
                           
                    elif collision3:
                            wn.fill((255,0,255))
                           
                           
                            pygame.mixer.music.stop()
                            crash_Sound=pygame.mixer.Sound("car_crash.wav")
                            crash_Sound.play(0)
                            car1_y=0
                            car2_y=0
                            car3_y=0
                            car1_ychange=0
                            car2_ychange=0
                            car3_ychange=0
                            car_x=0
                            car_xchange=0
                            show_crash(crash_x,crash_y)
                            show_score(310,350)
                           
                           
                           
                            game_over=True
                            pygame.display.update()
                           
            clock.tick(fps)                   
            pygame.display.update()   
        pygame.quit()
        quit()
gameloop()