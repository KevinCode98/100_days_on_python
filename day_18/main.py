import turtle as t
import random

timmy_the_turtle = t.Turtle()
t.colormode(255)
# while True:
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# for x in range(20):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(30)
#         timmy_the_turtle.right(angle)

# for shape_side_n in range(3,30):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)

# while True:
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))


screen = t.Screen()
screen.exitonclick()
