import pygame
import random
import math
import time

# Initialize pygame
pygame.init()

# -------setup the screen----
wn = pygame.display.set_mode((798, 600))
pygame.display.set_caption('Crazy Car Game')
logo = pygame.image.load('car.png')
pygame.display.set_icon(logo)

# Load and resize background
bg = pygame.image.load('bg.png')
bg = pygame.transform.scale(bg, (798, 600))  # optional if bg is too big

# -------variables-----
counttime = 3
fps = 60
clock = pygame.time.Clock()

# Fonts
font_crash = pygame.font.Font('freesansbold.ttf', 72)
font_score = pygame.font.Font('freesansbold.ttf', 32)
font_msg = pygame.font.Font('freesansbold.ttf', 42)

# Score
score_value = 0

# Background music
pygame.mixer.init()

# -------Load and resize cars------
car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (30, 60))

car1 = pygame.image.load('car1.jpeg')
car1 = pygame.transform.scale(car1, (30, 60))

car2 = pygame.image.load('car2.png')
car2 = pygame.transform.scale(car2, (30, 60))

car3 = pygame.image.load('car3.png')
car3 = pygame.transform.scale(car3, (30, 60))

# ---------Functions---------
def picture(x, y):
    wn.blit(car, (x, y))

def picture1(x, y):
    wn.blit(car1, (x, y))

def picture2(x, y):
    wn.blit(car2, (x, y))

def picture3(x, y):
    wn.blit(car3, (x, y))

def show_score(x, y):
    score_font = font_score.render("Score: " + str(score_value), True, (255, 255, 255))
    wn.blit(score_font, (x, y))

def show_crash(x, y):
    crash = font_msg.render("Car Crashed!", True, (255, 0, 0))
    wn.blit(crash, (x, y))

def iscollision(car_x, car_y, obj_x, obj_y):
    distance = math.sqrt((car_x - obj_x) ** 2 + (car_y - obj_y) ** 2)
    return distance < 60

def over_font(x, y):
    over_font = font_score.render("Press Enter to continue", True, (0, 255, 0))
    wn.blit(over_font, (x, y))

# ---------Main loop----------
def gameloop():
    global score_value
    score_value = 0

    # Player car position
    car_x = 290
    car_y = 480
    car_xchange = 0

    # Enemy cars
    car1_x = random.randint(250, 485)
    car1_y = -150
    car1_ychange = 4

    car2_x = random.randint(250, 485)
    car2_y = -300
    car2_ychange = 4

    car3_x = random.randint(250, 485)
    car3_y = -450
    car3_ychange = 4

    game_exit = False
    game_over = False

    # Play background music
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.play(-1)

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            # Player controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    car_xchange = 3
                if event.key == pygame.K_LEFT:
                    car_xchange = -3
                if event.key == pygame.K_RETURN and game_over:
                    gameloop()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    car_xchange = 0

        if not game_over:
            # Move player car
            car_x += car_xchange

            # Move enemy cars
            car1_y += car1_ychange
            car2_y += car2_ychange
            car3_y += car3_ychange

            # Respawn cars and increase score
            if car1_y > 600:
                car1_y = -150
                car1_x = random.randint(250, 485)
                score_value += 1

            if car2_y > 600:
                car2_y = -150
                car2_x = random.randint(250, 485)
                score_value += 1

            if car3_y > 600:
                car3_y = -150
                car3_x = random.randint(250, 485)
                score_value += 1

            # Check collisions
            collision1 = iscollision(car_x, car_y, car1_x, car1_y)
            collision2 = iscollision(car_x, car_y, car2_x, car2_y)
            collision3 = iscollision(car_x, car_y, car3_x, car3_y)

            if car_x < 185:
                car_x = 185
            if car_x > 483:
                car_x = 483

            if collision1 or collision2 or collision3:
                pygame.mixer.music.stop()
                crash_sound = pygame.mixer.Sound("car_crash.wav")
                crash_sound.play()
                game_over = True

            # Draw background and cars
            wn.blit(bg, (0, 0))
            picture(car_x, car_y)
            picture1(car1_x, car1_y)
            picture2(car2_x, car2_y)
            picture3(car3_x, car3_y)
            show_score(580, 10)

        else:
            wn.fill((255, 0, 0))
            show_crash(270, 250)
            show_score(310, 350)
            over_font(270, 400)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()
