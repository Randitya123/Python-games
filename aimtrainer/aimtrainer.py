import pgzrun
import random
TITLE="AimTrainer"
WIDTH=1000
HEIGHT=800
block=Actor("r.png")
s=0
m=0
def draw():
    screen.clear()
    screen.fill("white")
    block.draw()
    screen.draw.text("Score:"+str(s),center=(400,50),fontsize=30,color="black")
    screen.draw.text("Missed:"+str(m),center=(600,50),fontsize=30,color="black")
def r():
    block.x=random.randint(0,1000)
    block.y=random.randint(0,800)
def on_mouse_down(pos):
    global s
    global m
    if block.collidepoint(pos):
        r()
        s+=1
    else:
        m+=1
def update():
    pass
pgzrun.go()