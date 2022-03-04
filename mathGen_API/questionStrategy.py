# Stratergy Pattern Test
from abc import ABC, abstractmethod
from numbers import Number
from typing import Optional, Tuple
import numberGen
from question import Question
import random, math

class QuestionType(ABC):
    """Base Abstract class for Question Types (To implement strategy pattern)
    negative(-1) difficulty is custom difficulty
    """
    def __init__(self, num_gen_cls, difficulty:int, ll=None, ul=None) -> None:
        super().__init__()
        self.difficulty = difficulty if difficulty != None else 1
        range = self.getRangeFromDifficulty()
        if self.isCustomDifficulty():
            # check if ll and ul are not None
            # if not all((ll, ul)): raise Exception()
            range = (ll, ul)
        print(f"range {range}")
        # if not issubclass(num_gen_cls, numberGen.NumberGenerator): raise Exception("num_gen_cls must be a subsclass of NumberGenerator")
        self.number_gen_obj = num_gen_cls(*range)

    @abstractmethod
    def setDiffiuclty(self, dif:int) -> None:
        ...

    @abstractmethod
    def getRangeFromDifficulty(self) -> Tuple:
        ...

    def isCustomDifficulty(self):
        return self.difficulty < 0

    def setLowerLimit(self, ll):
        if not self.isCustomDifficulty(): raise Exception("Difficulty must be set to -1 to update lower limit")
        self.number_gen_obj.lower_limit = ll

    def setUpperLimit(self, ul):
        if not self.isCustomDifficulty(): raise Exception("Difficulty must be set to -1 to update upper limit")
        self.number_gen_obj.upper_limit = ul

    @abstractmethod
    def generate_question(self, *args, **kwargs) -> Question:
        ...

class AdditionQuestionType1(QuestionType):
    Q_TYPE:str = "addition - type1"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = "+"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def setDiffiuclty(self, dif: int) -> None:
        return None

    def generateFromatString(self, num:int) -> str:
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType1(QuestionType):
    Q_TYPE:str = "subtraction - type1"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int) -> str:
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        first_num = sum(num_list) + number_gen_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType2(QuestionType):
    Q_TYPE:str = "subtraction - type2"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int) -> str:
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        num_list.insert(sum(num_list) - number_gen_obj.number(), 0)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType3(QuestionType):
    Q_TYPE:str = "subtraction - type3"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int) -> str:
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        num_list.insert(sum(num_list) - number_gen_obj.number(), 0)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class MultiplicationQuestionType1(QuestionType):
    Q_TYPE:str = "multiplication - type1"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int) -> str:
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class MultiplicationQuestionType2(QuestionType):
    Q_TYPE:str = "multiplication - type2"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int) -> str:
        return f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums//2)
        num_list += number_gen_obj.numbers(self.number_of_nums - self.number_of_nums//2, is_negative=True)
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

"""class DivisionQuestionType1(QuestionType):
    Q_TYPE:str = ""
    def generate_question(self, gen_type) -> Question:
        pass"""

class LCMQuestionType1(QuestionType):
    Q_TYPE:str = "lcm - type1"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int) -> str:
        return "Find LCM of: " + f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, self.findLCM(num_list), self.Q_TYPE.title())
    
    def findLCM(self, num_list):
        return 1
    

class HCFQuestionType1(QuestionType):
    Q_TYPE:str = "hcf - type1"
    def __init__(self,num_gen_cls, difficulty:int, number_of_nums:int, ll:Optional[Number], ul:Optional[Number]) -> None:
        super().__init__(num_gen_cls, difficulty)
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generateFromatString(self, num:int) -> str:
        return "Find HCF of: " + f" {self.operator} ".join(["{}" for _ in range(num)])

    def generate_question(self, number_gen_obj) -> Question:
        format_string = self.generateFromatString(self.number_of_nums)
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, self.findHCF(num_list), self.Q_TYPE.title())

    def findHCF(self, num_list):
        return 1

"""class MissingFactorsQuestionType1(QuestionType):
    Q_TYPE:str = ""
    def generate_question(self, gen_type) -> Question:
        pass"""

class QuadraticQuestionType1(QuestionType):
    Q_TYPE:str = "quadratic - type1"
    def generate_question(self, number_gen_obj) -> Question:
        format_string = "{}x^2 + {}x + {} = 0"
        roots = number_gen_obj.numbers(2)
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return Question(question_string, roots, self.Q_TYPE.title())

"""class QuadraticQuestionType2(QuestionType):
    Q_TYPE:str = ""
    def generate_question(self, number_gen_obj) -> Question:
        format_string = "{}x^2 + {}x + {} = 0"
        roots = number_gen_obj.numbers(2)
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return Question(question_string, roots, self.Q_TYPE.title()"""

class Linear2VarQuestionType1(QuestionType):
    Q_TYPE:str = "linear2var - type1"
    def generate_question(self, number_gen_obj) -> Question:
        format_string = "{}x + {}y + {} = 0;{}x + {}y + {} = 0;"
        p1 = number_gen_obj.numbers(2)
        p2 = number_gen_obj.numbers(2)
        sol = number_gen_obj.numbers(2)
        c1 = self.generate_coefficient(p1, sol)
        c2 = self.generate_coefficient(p2, sol)
        question_string = format_string.format(*c1, *c2)
        return Question(question_string, sol, self.Q_TYPE.title())

    def generate_coefficient(self, point, ans_point):
        a = (ans_point[1] - point[1])
        b = (ans_point[0] - point[0]) * -1
        c = -(point[0] * (ans_point[1] - point[1])) + (point[1] * (ans_point[0] - point[0]))
        if(a < 0):
            a*= -1
            b*= -1
            c*= -1
        return [a, b, c]

class SimpleInterestQuestionType1(QuestionType):
    Q_TYPE:str = "simple interest - type1"
    def generate_question(self, number_gen_obj) -> Question:
        format_string = "SI Question principal={} year={} rate={}"
        number_gen_obj.lower_limit(1000)
        number_gen_obj.upper_limit = 100000
        p = number_gen_obj.number()
        number_gen_obj.lower_limit = 1
        number_gen_obj.upper_limit = 10
        n = number_gen_obj.number()
        r = number_gen_obj.number()
        question_string = format_string.format(p, n, r)
        return Question(question_string, self.findSI(p, n, r), self.Q_TYPE.title())

    def findSI(self, p, n, r):
        pass

class CompundInterestQuestionType1(QuestionType):
    Q_TYPE:str = "compound interest - type1"
    def generate_question(self, number_gen_obj) -> Question:
        format_string = "CI Question principal={} year={} rate={}"
        number_gen_obj.lower_limit = 1000
        number_gen_obj.upper_limit = 100000
        p = number_gen_obj.number()
        number_gen_obj.lower_limit = 1
        number_gen_obj.upper_limit = 10
        n = number_gen_obj.number()
        r = number_gen_obj.number()
        question_string = format_string.format(p, n, r)
        return Question(question_string, self.findCI(p, n, r), self.Q_TYPE.title())

    def findCI(self, p, n, r):
        pass

def runAll():
    import numberGen
    for g in [AdditionQuestionType1, SubtractionQuestionType1, SubtractionQuestionType2, MultiplicationQuestionType1, MultiplicationQuestionType2, LCMQuestionType1, HCFQuestionType1]:
        n_num = int(input("How many numbers do you want? \n>"))
        gen_obj = g(n_num)
        question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(1, 25))
        print(f"{question.type}")
        print(f"{question}")
        print()

    for g in [QuadraticQuestionType1, Linear2VarQuestionType1]:
        gen_obj = g()
        question:Question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(1, 25))
        print(f"{question.type}")
        print(f"{question}")
        print()


def main():
    import numberGen
    gen_obj = QuadraticQuestionType1(numberGen.RangedIntegerNumberGenerator, 50)
    question:Question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(50, 100))
    print(f"{question.type}")
    print(f"{question}")
    print()

if __name__ == "__main__":
    print("Hello World! 🔥")
    print("Done ✅")