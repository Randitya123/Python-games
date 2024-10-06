import pgzrun
import random

HEIGHT=630
WIDTH=1100

gameo=False
gamec=False
level=1
l2=[]
tlev=8
speed=15
l1=["bag.png","computer.png","mirror.png","pot.png"]
def draw():
    screen.blit("recycle.jpg",(0,0))
def update():
    pass
def put(extra):
    l3=[]
    option=["box.png"]+random.choice(l1)
    random.shuffle(option)
    #creating a cmbined list and making actor
    for i in option:
        
pgzrun.go()