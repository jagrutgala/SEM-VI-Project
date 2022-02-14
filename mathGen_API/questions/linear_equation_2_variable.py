from core import Question, QuestionGenerator, NumberGen
import random

def positiveNumberInRange(upper_limit) -> float:
    return random.uniform(0, upper_limit)

class QuadraticQuestion(QuestionGenerator, pre_fix="quadratic"):
    def __init__(self, pre_fix, num_gen_type=None) -> None:
        super().__init__(pre_fix)
        # self.num_generator = NumberGen(num_gen_type)

    def getCoefficients(self, p1, p2, p3):
        pass

    def getPoints(self, difficulty):
        pass

    def getEquation(self, difficulty)

    def create_question(self, difficulty):
        if difficulty == self.HARD:
            p1, p2, p3 = self.getPoints(difficulty)
            a1, b1, c1 = self.getCoefficients()
            a2, b2, c2 = self.getCoefficients()
        if difficulty == self.MEDIUM:
            alpha, beta = self.getMediumNumbers()
        else:
            alpha, beta = self.getEasyNumbers()
        eq1_string = "{a1}x + {b1}y + {c1}= 0"
        eq2_string = "{a2}x + {b2}y + {c2}= 0"
        q_string = f"{eq1_string};{eq2_string}"
        ans = self.findAns(alpha, beta)
        return Question(q_string=q_string, answer=ans, question_type=self.q_type, difficulty=difficulty)

    def findAns(self, alpha, beta):
        return (alpha, beta)

def main():
    qgen = QuestionGenerator("quadratic", num_gen_type="quadratic_numbers")
    print(f"Question Class Type {type(qgen)}")
    for _ in range(10):
        q = qgen.create_question(QuestionGenerator.HARD)
        print(f"EAZY Question \n{q}")
        print()

if __name__ == "__main__":
    main()