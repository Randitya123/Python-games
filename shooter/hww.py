import pgzrun, random
HEIGHT=800
WIDTH=1100
c1=(128,200,79)
l1=[]
l2=[]
score=0
l1.append(Actor("shark.png"))
l1[-1].x=70
l1[-1].y=0
charcter=Actor("sub.png")
charcter.pos=550,720
def on_key_down(key):
    if key==keys.W:
        l2.append(Actor("bubble.png"))
        l2[-1].x=charcter.x
        l2[-1].y=charcter.y-120
def update():
    pass
    global score
    if keyboard.a:
        charcter.x-=3
    if keyboard.d:
        charcter.x+=3
    for z in l1:
        z.y+=3
        if z.y>=HEIGHT:
           z.y=0
           z.x=random.randint(70,1030)  
        for g in l2:
            if g.colliderect(z):
                l2.remove(g)
                z.y=0
                z.x=random.randint(70,1030) 
                z.y+=0 
                score+=100
                sounds.splat.play()
    for i in l2:
        i.y-=3
def draw():
    screen.blit("bg.jpg",(0,0))
    charcter.draw()
    for z in l1:
        z.draw()
    for i in l2:
        i.draw()
    screen.draw.text(str(score),(20,20),fontsize=100)
pgzrun.go()
