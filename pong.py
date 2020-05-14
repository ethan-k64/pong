#Setup
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#Variables
bat_y = 4
lives = 3
score = 0

ball_position = [3,3]
ball_velocity = [1,1]

#Colors
white = (255,255,255)
purple = (255,0,255)

#Functions
def die():
    sleep(10000)

def draw_bat():
    sense.set_pixel(0,bat_y,white)
    sense.set_pixel(0,bat_y - 1,white)
    sense.set_pixel(0,bat_y + 1,white)
    
def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1
        
def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1
        
def draw_ball():
    global score
    sense.set_pixel(ball_position[0],ball_position[1],purple)
    
    #Ball Movement
    ball_position[0] += ball_velocity[0]
    
    if ball_position[0] == 7:
        ball_velocity[0] = -ball_velocity[0]
    
    ball_position[1] += ball_velocity[1]
    
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    
    if ball_position[0] == 0 and ball_position[1]:
        ball_velocity[0] = -ball_velocity[0]
        
    if ball_position[0] == 1 and ball_position[1] == bat_y:
        ball_velocity[0] = -ball_velocity[0]
        score += 1
    elif ball_position[0] == 1 and ball_position[1] == bat_y -1:
        ball_velocity[0] = -ball_velocity[0]
        score += 1
    elif ball_position[0] == 1 and ball_position[1] == bat_y + 1:
        ball_velocity[0] = -ball_velocity[0]
        score += 1
        
def lose():
    global lives
    global purple
    global score
    
    if ball_position[0] == 0:
        lives -= 1
        ball_position[1] = 3
        ball_position[0] = 3
        ball_velocity[1] = 1
        ball_velocity[0] = 1
        
    if lives == 3:
        purple = (255,0,255)
        
    if lives == 2:
        purple = (255,128,0)
        
    if lives == 1:
        purple = (255,0,0)
        
    if lives == 0:
        ball_velocity[1] = 0
        ball_velocity[0] = 0
        
        sense.show_message("Score: ")
        
        if score <= 9:
            sense.show_letter(str(score))
            sleep(0.75)
            sense.clear(0,0,0)
            sleep(0.75)
            sense.show_letter(str(score))
            sleep(0.75)
            sense.clear(0,0,0)
            sleep(0.75)
            sense.show_letter(str(score))
            sleep(0.75)
            score = 0
            lives = 3
            ball_velocity[1] = 1
            ball_velocity[0] = 1
        else:
            sense.show_message(str(score))
            score = 0
            lives = 3
            ball_velocity[1] = 1
            ball_velocity[0] = 1

#Main Program
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while True:
    sense.clear(0,0,0)
    draw_bat()
    draw_ball()
    lose()
    sleep(0.25)

