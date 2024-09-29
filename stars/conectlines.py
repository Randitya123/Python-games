import pgzrun
import time
import random
HEIGHT=800
WIDTH=1000
#VARIABLES
l1=[]
l2=[]
start=0
end=0
dur=0
count=10
def mactor():
    for i in range(count):
        star=Actor("star.png")
        star.pos=random.randint(0,1000),random.randint(0,800)
        l1.append(star)
def draw():
    screen.blit("bg.jpg",(0,0))
    for i in l1:
        i.draw()
def update():
    pass
mactor()
pgzrun.go()