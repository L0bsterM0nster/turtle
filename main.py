import turtle

min_skoldpadda = turtle.Turtle()

min_skoldpadda.shape("turtle")

min_skoldpadda.color("green")

min_skoldpadda.speed(7)


def rita_cirkel(radie):
    for i in range(10):
        min_skoldpadda.color("green")
        min_skoldpadda.circle(radie)
        min_skoldpadda.right(36)
        min_skoldpadda.color("red")
        min_skoldpadda.circle(radie / 4)
        min_skoldpadda.color("blue")
        min_skoldpadda.circle(radie / 2)

rita_cirkel(100)
turtle.done()

