import pgzrun, random
HEIGHT=800
WIDTH=1100
c1=(128,200,79)
c2=(0,230,0)
l1=[]
l2=[]
#zombie=Actor("zombie.png")
l1.append(Actor("zombie.png"))
l1[-1].x=70
l1[-1].y=0
charcter=Actor("charcter.png")
charcter.pos=550,720
def on_key_down(key):
    if key==keys.W:
        l2.append(Actor("bullet.png"))
        l2[-1].x=charcter.x+47
        l2[-1].y=charcter.y-120
        
def update():
    #pass
    if keyboard.a:
        charcter.x-=3
    if keyboard.d:
        charcter.x+=3
    for z in l1:
        z.y+=3
        if z.y==HEIGHT:
           z.y=0
           z.x=random.randint(70,1030)  
    for i in l2:
        i.y-=3
def draw():
    screen.fill(c2)
    charcter.draw()
    for z in l1:
        z.draw()
    for i in l2:
        i.draw()
pgzrun.go()
