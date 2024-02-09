# Voici le code source du mini-projet
# Importation de la bibliothèque 
import turtle


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.width(2)
t.speed(15)

col = ('white', 'pink', 'cyan')
for i in range (300):
    t.pencolor(col[i%3])
    t.forward(i*4)
    t.right(121)
