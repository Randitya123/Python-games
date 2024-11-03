import pgzrun, random
HEIGHT=800
WIDTH=1100
c1=(128,200,79)
c2=(0,230,0)
l1=[]
zombie=Actor("zombie.png")
l1.append(zombie)
charcter=Actor("charcter.png")
charcter.pos=550,720
def draw():
    screen.fill(c2)
    charcter.draw()
    for z in l1:
        z.draw()
def update():
    pass
    if keyboard.a:
        charcter.x-=3
    if keyboard.d:
        charcter.x+=3
    for z in l1:
        z.y+=3
        if z.y==HEIGHT:
           z.y=0
           z.x=random.randint(70,1030)  
pgzrun.go()
