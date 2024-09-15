import random
import pgzrun
HEIGHT=800
WIDTH=1000
bees=Actor("bees.png")
flower=Actor("images.png")
bees.pos=400,500
flower.pos=250,75
score=0
gameover=False
def draw():
    screen.fill("skyblue")
    bees.draw() 
    flower.draw()             
def update():
    pass
    if keyboard.a:
        bees.x=bees.x-2
    if keyboard.d:
        bees.x=bees.x+2
    if keyboard.w:
        bees.y=bees.y-2
    if keyboard.s:
        bees.y=bees.y+2
def ra():
    flower.x=random.randint(0,1000)
    flower.y=random.randint(0,800)
clock.schedule_interval(ra,3.0)
ra()
pgzrun.go()
