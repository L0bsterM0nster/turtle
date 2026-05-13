import turtle


iris = input("Vad är din primära ögonfärg?")
iris2 = input("Vad är din sekundära ögonfärg?")

screen = turtle.Screen()
screen.bgcolor("#000000")
screen.tracer(0)

pupill = "black"

lob = "white"

vinkel = 2

min_skoldpadda = turtle.Turtle()

min_skoldpadda.shape("turtle")

            

def rita_lob(radie):
        min_skoldpadda.color(lob)
        min_skoldpadda.begin_fill()
        min_skoldpadda.circle(radie)
        min_skoldpadda.end_fill()


def rita_iris(radie):
        min_skoldpadda.color(iris)
        min_skoldpadda.begin_fill()
        min_skoldpadda.circle(radie / 1.7)
        min_skoldpadda.end_fill()

def rita_iris2(radie):
        min_skoldpadda.color(iris2)
        min_skoldpadda.circle(radie / 1.7)



def rita_pupill(radie):
        min_skoldpadda.color(pupill)
        min_skoldpadda.begin_fill()
        min_skoldpadda.circle(radie / 6)
        min_skoldpadda.end_fill()

for i in range(80):
    rita_lob(100)
    min_skoldpadda.right(36)

    min_skoldpadda.right(vinkel + 36)

for i in range(80):
    rita_iris(100)
    min_skoldpadda.right(36)

    min_skoldpadda.right(vinkel + 36)

for i in range(80):
    rita_iris2(100)
    min_skoldpadda.right(36)

    min_skoldpadda.right(vinkel + 36)

for i in range(80):
    rita_pupill(100)
    min_skoldpadda.right(36)

    min_skoldpadda.right(vinkel + 36)

turtle.done()


