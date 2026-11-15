from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20 ,"normal")




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.t_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER ", move=False, align = ALIGNMENT ,font = FONT)


    def reset_score(self):
        if self.t_score > self.high_score:
            self.high_score = self.t_score
            print(f"the highest score is one:{self.high_score }")
        self.t_score = 0
        self.update()



    def update(self,):
        self.clear()
        with open("data.txt", mode = "w") as file:
            file.write(f"{self.high_score}")
            print(f"the highest score is two :{self.high_score}")

        self.write(f"Score: {self.t_score} High Score:{self.high_score}",move=False, align = ALIGNMENT ,font = FONT)


    def new_score(self):
        self.t_score += 1
        self.clear()
        self.update()

