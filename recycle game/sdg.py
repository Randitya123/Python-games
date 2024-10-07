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
    for t in l2:
        t.draw()
def update():
    global l2, level
    
    if len(l2)==0:
        l2=put(level)
    pass
def put(extra):
    l3=[]
    option=["box"]+random.choices(l1,k=extra)
    random.shuffle(option)
    #creating a cmbined list and making actor
    for i in option:
        act=Actor(i)
        l3.append(act)
    size=WIDTH/(len(l3))
    for u,z in enumerate(l3):
        z.x=(u+1)*size
        z.y=0
        animate(z, duration=speed - level, on_finshed=handle_game_over, y=HEIGHT)
    return l3
def handle_game_over():
    global gameo
    gameo=True
pgzrun.go()
