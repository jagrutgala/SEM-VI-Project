from core import Question, QuestionGenerator, NumberGen
import random

def positiveNumberInRange(upper_limit) -> float:
    return random.uniform(0, upper_limit)

class QuadraticQuestion(QuestionGenerator, pre_fix="quadratic"):
    def __init__(self, pre_fix, num_gen_type=None) -> None:
        super().__init__(pre_fix)
        # self.num_generator = NumberGen(num_gen_type)
    
    def getEasyNumbers(self) -> tuple[int, int]:
        return (int(positiveNumberInRange(100)), int(positiveNumberInRange(100)))

    def getMediumNumbers(self) -> tuple[int, int]:
        return (int(positiveNumberInRange(100)), int(positiveNumberInRange(100)))

    def getHardNumbers(self) -> tuple[float, float]:
        return (positiveNumberInRange(100), positiveNumberInRange(100))

    def create_question(self, difficulty):
        if difficulty == self.HARD:
            alpha, beta = self.getHardNumbers()
        if difficulty == self.MEDIUM:
            alpha, beta = self.getMediumNumbers()
        else:
            alpha, beta = self.getEasyNumbers()
        q_string = f"x^2 +{alpha+ beta}x + {alpha* beta} = 0"
        ans = self.findAns(alpha, beta)
        return Question(q_string=q_string, answer=ans, question_type=self.q_type, difficulty=difficulty)

    def findAns(self, alpha, beta):
        return (alpha, beta)


def quadraticEquation():
    alpha= random.randint(1, 20)
    beta= random.randint(1, 20)
    equation_string= f"x^2 +{alpha+ beta}x + {alpha* beta} = 0"
    return equation_string


def main():
    qgen = QuestionGenerator("quadratic", num_gen_type="quadratic_numbers")
    print(f"Question Class Type {type(qgen)}")
    for _ in range(10):
        q = qgen.create_question(QuestionGenerator.HARD)
        print(f"EAZY Question \n{q}")
        print()

if __name__ == "__main__":
    main()