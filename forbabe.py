import turtle

def heart():
    turtle.color('red')
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.left(140)
    turtle.forward(224)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

def line1():
    turtle.penup()
    turtle.goto(-700, -100)
    turtle.color('black')
    turtle.write("Supp babe, I just wanted you to know that falling in love with you has been the beast thing for me in this life", font=("Arial", 16, "bold" ))

def line2():
    turtle.penup()
    turtle.goto(-600, -120)
    turtle.color('black')
    turtle.write("and really words are not enough to express those feelings ........", font=("Arial", 16, "bold" ))

def line3():
    turtle.penup()
    turtle.goto(-700, -140)
    turtle.color('black')
    turtle.write("I still wonder how such a beautiful person can love someone like me xDD", font=("Arial", 16, "bold" ))

def line4():
    turtle.penup()
    turtle.goto(-500, -170)
    turtle.color('black')
    turtle.write("And I genuinely love youuuu! ", font=("Arial", 20, "bold" ))

def line5():
    turtle.penup()
    turtle.goto(-200, -190)
    turtle.color('black')
    turtle.write(" From - OKKAR to his fav person -> NYKMS <3")


def main():
    turtle.speed(1)
    turtle.bgcolor('pink')

    heart()
    line1()
    line2()
    line3()
    line4()
    line5()

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()