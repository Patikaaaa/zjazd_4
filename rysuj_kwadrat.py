import turtle
okno = turtle.Screen()
zolw = turtle.Turtle()
def rysuj_kwadrat(zolw):
    for krok in range(4):
        zolw.forward(150)
        zolw.left(90)
rysuj_kwadrat(zolw)
