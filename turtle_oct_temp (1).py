from turtle import*

vip=Turtle()
vip.color('red')
vip.shape('turtle')
vip.penup()
vip.goto(-140,140)
vip.pendown()

for i in range(8):
    vip.forward(150)
    vip.right(45)

jay=Turtle()
jay.color('green')
jay.shape('turtle')
jay.penup()
jay.goto(-110,90)
jay.pendown()

for i in range(8):
       jay.forward(100)
       jay.right(45)

raj=Turtle()
raj.color('orange')
raj.shape('turtle')
raj.penup()
raj.goto(-90,40)
raj.pendown()

for i in range(8):
       raj.forward(50)
       raj.right(45)
