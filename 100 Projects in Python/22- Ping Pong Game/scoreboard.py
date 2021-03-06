from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.beautify_screen()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.beautify_screen()
        self.goto(0, 250)
        self.write(f"{self.l_score} Scoreboard {self.r_score}", align="center", font=("Arial", 20, "normal"))

    def beautify_screen(self):
        for x in range(-250, 250, 50):
            self.goto(0, x)
            self.write(".", align="center", font=("Arial", 20, "normal"))
        for x in range(-250,250, 50):
            self.goto(-380,x)
            self.write("|", align="center", font=("Arial", 20, "normal"))
        for x in range(-250,250, 50):
            self.goto(380,x)
            self.write("|", align="center", font=("Arial", 20, "normal"))
        for x in range(-360,380, 30):
            self.goto(x, 220 )
            self.write("--", align="center", font=("Arial", 20, "normal"))
        for x in range(-360,380, 30):
            self.goto(x, -265)
            self.write("--", align="center", font=("Arial", 20, "normal"))

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

