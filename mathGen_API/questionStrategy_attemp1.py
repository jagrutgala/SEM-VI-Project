# Stratergy Pattern Test
from abc import ABC, abstractmethod
from question import Question
import random, math

class QuestionType(ABC):
    @abstractmethod
    def generate_question(self, *args, **kwargs):
        ...

class AdditionQuestionType1(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "+"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), "addition")

class SubtractionQuestionType1(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        first_num = sum(num_list) + number_gen_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return Question(question_string, eval(question_string), "subtraction")

class SubtractionQuestionType2(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        first_num = sum(num_list) - number_gen_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return Question(question_string, eval(question_string), "subtraction")

class SubtractionQuestionType3(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        num_list += sum(num_list) - number_gen_obj.number()
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), "subtraction")

class MultiplicationQuestionType1(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), "multiplication")

class MultiplicationQuestionType2(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums//2)
        num_list += number_gen_obj.numbers(self.number_of_nums - self.number_of_nums//2, is_negative=True)
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), "multiplication")

"""class DivisionQuestionType1(QuestionType):
    def generate_question(self, gen_type):
        pass"""

class LCMQuestionType1(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return "Find LCM of: " + f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, self.findLCM(num_list), "lcm")
    
    def findLCM(self, num_list):
        return 1
    

class HCFQuestionType1(QuestionType):
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int):
        return "Find HCF of: " + f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj):
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, self.findHCF(num_list), "hcf")

    def findHCF(self, num_list):
        return 1

"""class MissingFactorsQuestionType1(QuestionType):
    def generate_question(self, gen_type):
        pass"""

class QuadraticQuestionType1(QuestionType):
    def generate_question(self, number_gen_obj):
        format_string = "{}x^2 + {}x + {} = 0"
        roots = number_gen_obj.numbers(2)
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return Question(question_string, roots, "quadratic")

class QuadraticQuestionType2(QuestionType):
    def generate_question(self, number_gen_obj):
        format_string = "{}x^2 + {}x + {} = 0"
        roots = number_gen_obj.numbers(2)
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return Question(question_string, roots, "quadratic")

class Linear2VarQuestionType1(QuestionType):
    def generate_question(self, number_gen_obj):
        format_string = "{}x + {}y + {} = 0;{}x + {}y + {} = 0;"
        p1 = number_gen_obj.numbers(2)
        p2 = number_gen_obj.numbers(2)
        sol = number_gen_obj.numbers(2)
        c1 = self.generate_coefficient(p1, sol)
        c2 = self.generate_coefficient(p2, sol)
        question_string = format_string.format(*c1, *c2)
        return Question(question_string, sol, "linear2var")

    def generate_coefficient(self, point, ans_point):
        a = (ans_point[1] - point[1])
        b = (ans_point[0] - point[0]) * -1
        c = -(point[0] * (ans_point[1] - point[1])) + (point[1] * (ans_point[0] - point[0]))
        if(a < 0):
            a*= -1
            b*= -1
            c*= -1
        return [a, b, c]

class SimpleInterestQuestionType2(QuestionType):
    def generate_question(self, number_gen_obj):
        format_string = "SI Question principal={} year={} rate={}"
        number_gen_obj.lower_limit(1000)
        number_gen_obj.upper_limit = 100000
        p = number_gen_obj.number()
        number_gen_obj.lower_limit = 1
        number_gen_obj.upper_limit = 10
        n = number_gen_obj.number()
        r = number_gen_obj.number()
        question_string = format_string.format(p, n, r)
        return Question(question_string, self.findSI(p, n, r), "quadratic")

    def findSI(self, p, n, r):
        pass

class CompundInterestQuestionType2(QuestionType):
    def generate_question(self, number_gen_obj):
        format_string = "CI Question principal={} year={} rate={}"
        number_gen_obj.lower_limit = 1000
        number_gen_obj.upper_limit = 100000
        p = number_gen_obj.number()
        number_gen_obj.lower_limit = 1
        number_gen_obj.upper_limit = 10
        n = number_gen_obj.number()
        r = number_gen_obj.number()
        question_string = format_string.format(p, n, r)
        return Question(question_string, self.findCI(p, n, r), "quadratic")

    def findCI(self, p, n, r):
        pass

def main():
    import numberGen
    for g in [AdditionQuestionType1, SubtractionQuestionType1, SubtractionQuestionType2, SubtractionQuestionType3, MultiplicationQuestionType1, MultiplicationQuestionType2, LCMQuestionType1, HCFQuestionType1]:
        n_num = int(input("How many numbers do you want? \n>"))
        gen_obj = g(n_num)
        question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(1, 25))
        print(f"{question.type}")
        print(f"Q) {question}")
        print()

    for g in [QuadraticQuestionType1, Linear2VarQuestionType1]:
        gen_obj = g()
        question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(1, 25))
        print(f"{question.type}")
        print(f"Q) {question}")
        print()

if __name__ == "__main__":
    print("Hello World! 🔥")
    main()
    print("Done ✅")

