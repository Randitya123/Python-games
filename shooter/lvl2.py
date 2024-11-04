import pgzrun, random, time
HEIGHT=800
WIDTH=1100
c1=(128,200,79)
l1=[]
l2=[]
score=0
gameo=False
#zombie=Actor("zombie.png")
for l in range(4):
    l1.append(Actor("zombie.png"))
    l1[-1].x=70+10*l
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
    global score
    if keyboard.a:
        charcter.x-=3
    if keyboard.d:
        charcter.x+=3
    for z in l1:
        z.y+=3
        if z.y>=HEIGHT:
           score-=1
           z.y=0
           z.x=random.randint(70,1030)  
        for g in l2:
            if g.colliderect(z):
                l2.remove(g)
                z.y=0
                z.x=random.randint(70,1030)  
              #  l1.remove(z)
                score+=1
                sounds.splat.play()
    for i in l2:
        i.y-=3
def draw():
    global l1,l2
    screen.fill("black")
    charcter.draw()
    for z in l1:
        z.draw()
    for i in l2:
        i.draw()
    screen.draw.text(str(score),(20,20),fontsize=100)
    if gameo==True:
        screen.fill("darkgreen")
        screen.draw.text("Gameover, try again!-"+ str(score),(350,20),fontsize=50)
        l1=[]
        l2=[]
def game():
    global gameo
    gameo=True
clock.schedule(game,0.1)
pgzrun.go()
