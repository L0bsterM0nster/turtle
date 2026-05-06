import turtle
fönster = turtle.Screen()

min_skoldpadda = turtle.Turtle()

min_skoldpadda.shape("turtle")

min_skoldpadda.color("green")

min_skoldpadda.speed(7)

antal = int(input("Hur många sidor ska din figur ha? "))
storlek = int(input("Hur stor ska den vara?"))

vinkel = 360 / antal

for i in range(antal):
    min_skoldpadda.forward(storlek)
    min_skoldpadda.right(vinkel)
turtle.done()
    


#def rita_cirkel(radie):
#        min_skoldpadda.color("green")
#        min_skoldpadda.right(36)
#        min_skoldpadda.color("red")
 #       min_skoldpadda.circle(radie / 4)
  #      min_skoldpadda.color("blue")
   #     min_skoldpadda.circle(radie / 2)

#rita_cirkel(100)
#turtle.done()


