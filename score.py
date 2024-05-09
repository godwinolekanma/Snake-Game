from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.content = 0
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} HighScore: {self.highscore}", align="center", font=("arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score >= self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


