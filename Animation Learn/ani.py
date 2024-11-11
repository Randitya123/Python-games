import pgzrun, random,itertools
WIDTH=1560
HEIGHT=920

l1=[(1485,78),(1485,842),(75,842),(75,78)]
posblock=itertools.cycle(l1)
block=Actor("block.png")
man=Actor("man.png")
def draw():
    screen.clear()
    man.draw()
    block.draw()
def move():
    animate(block,"bounce_end", duration=1,pos=next(posblock))
move()
clock.schedule_interval(move,1)
def conmove():
    x=random.randint(80,1480)
    y=random.randint(83,838)
    man.target=x,y
    Angle=man.angle_to(man.target)
    Angle+=360*((man.angle - Angle + 180) // 360)  
    animate(man,angle=Angle, duration=0.01,on_finished=movemenht)
def movemenht():
    anim=animate(man,tween="accel_decel",pos=man.target, duration=man.distance_to(man.target)/1000, on_finished=conmove)
conmove()
pgzrun.go()