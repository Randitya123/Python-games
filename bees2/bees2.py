import random
import pgzrun
HEIGHT = 800
WIDTH = 1000
butter = Actor("but.png")  
flower = Actor("images.png")
rock = Actor("rock.png")
butter.pos = 400, 500
flower.pos = 250, 75
rock.pos = 100, 100
score = 0
gameover = False
def draw():
    screen.fill("darkblue")
    butter.draw()  
    flower.draw()
    rock.draw()
    screen.draw.text("Score:" + str(score), (450, 100), fontsize=40)
    if gameover:
        screen.fill("red")
        screen.draw.text("Time is up and your Score is " + str(score), center=(500, 400), fontsize=45)
def update():
    global score 
    if keyboard.a:
        butter.x -= 4
    if keyboard.d:
        butter.x += 4
    if keyboard.w:
        butter.y -= 4
    if keyboard.s:
        butter.y += 4

    if butter.colliderect(flower):
        flo()
        score += 1
    if butter.colliderect(rock):
        moverock()  
        score -= 1

def time():
    global gameover
    gameover = True
def flo():
    flower.x = random.randint(0, 1000)
    flower.y = random.randint(0, 800)
def moverock():  
    rock.x = random.randint(0, 1000)
    rock.y = random.randint(0, 800)

clock.schedule_interval(flo, 5.0)
clock.schedule_interval(moverock, 2.5)
clock.schedule(time, 60)
pgzrun.go()
