import pgzrun
import time
import random
HEIGHT=800
WIDTH=1000
#VARIABLES
l1=[]
l2=[]
start=0
dur=0
count=10
nextstar=0
def mactor():
    global start
    for i in range(count):
        star=Actor("star.png")
        star.pos=random.randint(502,950),random.randint(50,750)
        l1.append(star)
    start=time.time()
def draw():
    global dur
    screen.blit("bg.jpg",(0,0))
    num=1
    for i in l1:
        i.draw()
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20))
        num+=1
    for i in l2:
        screen.draw.line(i[0],i[1],(143,48,211))
    if nextstar<count:
        dur=time.time()-start
        screen.draw.text(str(round(dur,1)),(50,50),fontsize=30)
    else:
        screen.draw.text(str(round(dur,1)),(50,50),fontsize=30)


def update():
    pass
def on_mouse_down(pos):
    global nextstar,l2
    if nextstar<count:
        if l1[nextstar].collidepoint(pos):
            if nextstar:
                l2.append((l1[nextstar-1].pos, l1[nextstar].pos))
            nextstar+=1
        else:
            l2=[]
            nextstar=0
mactor()
pgzrun.go()
