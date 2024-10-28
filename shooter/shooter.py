import pgzrun, random
HEIGHT=800
WIDTH=1100
c1=(128,200,79)
c2=(0,230,0)
zombie=Actor("zombie.png")
charcter=Actor("charcter.png")
charcter.pos=550,720
def draw():
    screen.fill(c2)
    zombie.draw()
    charcter.draw()
def update():
    pass
pgzrun.go()
