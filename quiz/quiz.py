import pgzrun
TITLE="Quizizz"
HEIGHT=800
WIDTH=1200

marquee=Rect(0,0,1200,80)
main=Rect(0,0,900,135)
m1=Rect(0,0,435,240)
m2=Rect(0,0,435,240)
m3=Rect(0,0,435,240)
m4=Rect(0,0,435,240)
skip=Rect(0,0,1200,80)
timer=Rect(0,0,1200,80)
marquee.move_ip(0,0)
main.move_ip(15,115)
m1.move_ip(15,280)
m2.move_ip(15,540)
m3.move_ip(480,280)
m4.move_ip(480,540)

l1=[m1,m2,m3,m4]
def draw():
    screen.draw.filled_rect(marquee,"black")
    screen.draw.filled_rect(main,"blue")
    for i in l1:
        screen.draw.filled_rect(i,"purple")


def update():
    pass
pgzrun.go()