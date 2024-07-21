from turtle import Screen, Turtle
import pandas

screen = Screen()
turtle = Turtle()
screen.addshape("gradovi.gif")
turtle.shape("gradovi.gif")
screen.title("Gradovi Srbije")

data = pandas.read_csv("gradovi.csv")
gradovi = data["gradovi"].to_list()

odgovori = []


while len(odgovori) < len(gradovi):
    odgovor = screen.textinput(title=f"{len(odgovori)}/{len(gradovi)} Gradovi Srbije", prompt="Koji jos grad znas?")

    izostavljeni = []

    if odgovor == "Izlaz":
        break

    if odgovor in gradovi:
        if odgovor not in odgovori:
            grad = Turtle()
            grad.penup()
            grad.hideturtle()
            x_pozicija = data[data.gradovi == odgovor]
            y_pozicija = data[data.gradovi == odgovor]
            grad.goto(x_pozicija["x"].item(), y_pozicija["y"].item())
            grad.write(odgovor, font=("Courier", 20, "normal"))
            odgovori.append(odgovor)

    for grad in gradovi:
        if grad not in odgovori:
            izostavljeni.append(grad)
    df = pandas.DataFrame(izostavljeni)
    df.to_csv("izostavljeni_gradovi.csv")

screen.exitonclick()

