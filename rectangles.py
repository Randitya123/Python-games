import pgzrun
import random
WIDTH=1000
HEIGHT= 800
def draw():
    maxh=800
    maxw=200
    red=random.randint(0,255)
    blue=random.randint(0,255)
    green=random.randint(0,255)
    for i in range(40):
        object=Rect((0,0),(maxw,maxh))
        object.center=500,400
        screen.draw.rect(object,(red,green,blue))
        maxw+=10
        maxh-=10
def update():
    pass
pgzrun.go()
