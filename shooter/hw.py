import pgzrun, random
HEIGHT=800
WIDTH=1100
c1=(128,200,79)
l1=[]
l2=[]
score=0
direction=1
charcter=Actor("charcter.png")
charcter.pos=550,720
charcter.dead=False
charcter.countdown=90
def gameo():
    screen.draw.text("You lost!",(550,400))
#zombie=Actor("zombie.png"
for l in range(4):
    for q in range(3):
        l1.append(Actor("zombie.png"))
        l1[-1].x=70+55*l
        l1[-1].y=78+55*q
def on_key_down(key):
    if charcter.dead==False:
        if key==keys.W:
            l2.append(Actor("bullet.png"))
            l2[-1].x=charcter.x+47
            l2[-1].y=charcter.y-120
def update():
    #pass
    movedown=False
    global score, direction
    if charcter.dead==False:
        if keyboard.a:
            charcter.x-=10
        if keyboard.d:
            charcter.x+=10
    for i in l2:
        i.y-=3
    if len(l1)==0:
        gameo()
    if len(l1)>0 and (l1[-1].x>WIDTH-80 or l1[0].x<80):
        movedown=True
        direction=direction*-1
    for z in l1:
        z.x+=5*direction
        if movedown==True:
            z.y+=3
        if z.y>=HEIGHT:
            l1.remove(z)
        for g in l2:
            if g.colliderect(z):
                l2.remove(g)
                l1.remove(z)
                if len(l1)==0:
                    gameo()
                score+=1
        if z.colliderect(charcter):
            charcter.dead=True
    if charcter.dead:
        charcter.countdown-=1
    if charcter.countdown==0:
        charcter.dead=False
        charcter.countdown=90
def draw():
    screen.fill("black")
    if charcter.dead==False:
        charcter.draw()
    for z in l1:
        z.draw()
    for i in l2:
        i.draw()
    screen.draw.text(str(score),(20,20),fontsize=100)
    if len(l1)==0:
        gameo()
pgzrun.go()
