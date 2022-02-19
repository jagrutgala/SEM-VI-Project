import random

class Question:
    def __init__(self, qstring, answer, question_type) -> None:
        self.qstring = qstring
        self.answer = answer
        self.type = question_type
    
    def __repr__(self) -> str:
        return f"[Question] {self.qstring} \tAnswer: {self.answer}"

class linear2var:
    TYPE = "linear2var"
    def getPoints(self):
        return ((random.randint(1, 20), random.randint(1, 20)) for _i in range(3))

    def getEquation(self, point, ans_point):
        a = (ans_point[1] - point[1])
        b = (ans_point[0] - point[0]) * -1
        c = (point[0] * (ans_point[1] - point[1])) - (point[1] * (ans_point[0] - point[0]))
        return f"{a}x + {b}y + {c} = 0"

    def question(self) -> Question:
        random.seed()
        p1, p2, p3 = self.getPoints()
        eq1 = self.getEquation(p1, p3)
        eq2 = self.getEquation(p2, p3)
        question_string = f"{eq1};{eq2}"
        answer = p3
        return Question(question_string, answer, f"{self.TYPE}")


def main():
    qgen = linear2var()
    for _ in range(5):
        q = qgen.question()
        print(f"EAZY Question \n{q}")
        print()

if __name__ == "__main__":
    main()