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
    screen.draw.text("Score:"+str(score),(450,100),fontsize=35)   
    if gameover:
        screen.fill("red")
        screen.draw.text("Time is up and your Score is "+str(score),center=(500,400),fontsize=45)   

def update():
    pass
    global score
    if keyboard.a:
        bees.x=bees.x-4
    if keyboard.d:
        bees.x=bees.x+4
    if keyboard.w:
        bees.y=bees.y-4  
    if keyboard.s:
        bees.y=bees.y+4
    if bees.colliderect(flower):
        ra()
        score+=1
def time():
    global gameover
    gameover=True
    
def ra():
    flower.x=random.randint(0,1000)
    flower.y=random.randint(0,800)
clock.schedule_interval(ra,5.0)
clock.schedule(time,60)
ra()
pgzrun.go()
