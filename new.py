from turtle import*
from random import randint

speed(0)
penup()
goto(-140,140)

for i in range(16):
        write(i,align='center')
        right(90)
        forward(10)
        pendown()
        forward(190)
        penup()
        backward(200)
        left(90)
        forward(20)

vip=Turtle()
vip.color('red')
vip.shape('turtle')
vip.right(360)
vip.penup()
vip.goto(-160,100)
vip.pendown()

jay=Turtle()
jay.color('blue')
jay.shape('turtle')
jay.right(360)
jay.penup()
jay.goto(-160,70)
jay.pendown()

dude=Turtle()
dude.color('green')
dude.shape('turtle')
dude.right(360)
dude.penup()
dude.goto(-160,40)
dude.pendown()

bhai=Turtle()
bhai.color('yellow')
bhai.shape('turtle')
bhai.right(360)
bhai.penup()
bhai.goto(-160,10)
bhai.pendown()

chomu=Turtle()
chomu.color('orange')
chomu.shape('turtle')
chomu.right(360)
chomu.penup()
chomu.goto(-160,-20)
chomu.pendown()

churan=Turtle()
churan.color('pink')
churan.shape('turtle')
churan.right(360)
churan.penup()
churan.goto(-160,-50)
churan.pendown()

for turn in range(100):
    vip.forward(randint(1,5))
    jay.forward(randint(1,5))
    dude.forward(randint(1,5))
    bhai.forward(randint(1,5))
    chomu.forward(randint(1,5))
    churan.forward(randint(1,5))
    
