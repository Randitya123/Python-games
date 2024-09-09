import pgzrun
import random
WIDTH=1000
HEIGHT= 800
def draw():
    rad=360
    red=random.randint(0,255)
    blue=random.randint(0,255)
    green=random.randint(0,255)
    for i in range(70):
        screen.draw.circle((500,400),rad,(red,green,blue))
        rad-=5
def update():
    pass
pgzrun.go()