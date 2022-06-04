import turtle
colors= ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
#col=('yellow', 'red', 'blue', 'orange', 'green', 'white')
t= turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

# t2= turtle.Turtle()
# screen= turtle.Screen()
# screen.bgcolor('black')
# t2.speed(30)

# for i in range(150):
#     t2.color(col[i%6])
#     t2.forward(i*4)
#     t2.left(150)
#     t2.width(2)


