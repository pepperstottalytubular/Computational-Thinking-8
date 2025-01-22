import turtle 

t = turtle.Turtle()
t.goto(-10,15)
t.color("cyan")
for i in range(500):
    t.forward(5+i)
    t.left(284)
    t.speed( 10 )

turtle.exitonclick()
colors = ["pink","cyan","gray"]
for i in range( 10 ):
    t.color( pink[ i % 3 ] )
    t.forward(284)
    t.left( 90 )