from core import Question, QuestionGenerator, NumberGen
import random

def positiveNumberInRange(upper_limit) -> float:
    return random.uniform(0, upper_limit)

class AdditionQuestion(QuestionGenerator, pre_fix="addition"):
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
            num1, num2 = self.getHardNumbers()
        if difficulty == self.MEDIUM:
            num1, num2 = self.getMediumNumbers()
        else:
            num1, num2 = self.getEasyNumbers()
        q_string = f"{num1} + {num2}"
        ans = self.findAns(num1, num2)
        return Question(q_string=q_string, answer=ans, question_type=self.q_type, difficulty=difficulty)

    def findAns(self, num1, num2):
        return num1 + num2

class SubtractionQuestion(QuestionGenerator, pre_fix="subtraction"):
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
            num1, num2 = self.getHardNumbers()
        if difficulty == self.MEDIUM:
            num1, num2 = self.getMediumNumbers()
        else:
            num1, num2 = self.getEasyNumbers()
        q_string = f"{num1} - {num2}"
        ans = self.findAns(num1, num2)
        return Question(q_string, ans, self.q_type, difficulty)

    def findAns(self, num1, num2):
        return num1 - num2

class MultiplicationQuestion(QuestionGenerator, pre_fix="multiplication"):
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
            num1, num2 = self.getHardNumbers()
        if difficulty == self.MEDIUM:
            num1, num2 = self.getMediumNumbers()
        else:
            num1, num2 = self.getEasyNumbers()
        q_string = f"{num1} * {num2}"
        ans = self.findAns(num1, num2)
        return Question(q_string, ans, self.q_type, difficulty)

    def findAns(self, num1, num2):
        return num1 * num2

class DivisionQuestion(QuestionGenerator, pre_fix="division"):
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
            num1, num2 = self.getHardNumbers()
        if difficulty == self.MEDIUM:
            num1, num2 = self.getMediumNumbers()
        else:
            num1, num2 = self.getEasyNumbers()
        q_string = f"{num1} / {num2}"
        ans = self.findAns(num1, num2)
        return Question(q_string, ans, self.q_type, difficulty)

    def findAns(self, num1, num2):
        return num1 / num2

def main():
    qgen = QuestionGenerator("addition", num_gen_type="basic_numbers")
    print(f"Question Class Type {type(qgen)}")
    for _ in range(10):
        q = qgen.create_question(QuestionGenerator.EAZY)
        print(f"EAZY Question \n{q}")
        q = qgen.create_question(QuestionGenerator.MEDIUM)
        print(f"MEDIUM Question \n{q}")
        q = qgen.create_question(QuestionGenerator.HARD)
        print(f"HARD Question \n{q}")
        print()

if __name__ == "__main__":
    main()