import menu
import turtle

print(menu.logo)

my_turtle=turtle.Turtle()
print(my_turtle)
my_turtle.color("blue")
my_turtle.shape("turtle")
my_turtle.forward(100) # first half of the diamond
my_turtle.right(40)
my_turtle.forward(40)
my_turtle.right(20)
my_turtle.forward(50)
my_turtle.right(70)
my_turtle.forward(150)


my_turtle.right(100)
my_turtle.forward(150)
my_turtle.right(60)
my_turtle.forward(40)
my_turtle.right(20)
my_turtle.forward(40)



my_screen =turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
