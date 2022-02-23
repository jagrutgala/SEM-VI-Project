# To Figure out :??
# easily add new gen function to GEN_FUNCS
# refference to all the different question gen functions
# question gen func decorator

from abc import ABC, abstractmethod
import random

########## Temporary
class SmallNumberGenerator:
    def __init__(self) -> None:
        self.lower_limit = 1
        self.upper_limit = 25

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)

class MediumNumberGenerator:
    def __init__(self) -> None:
        self.lower_limit = 25
        self.upper_limit = 100

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)

class LargeNumberGenerator:
    def __init__(self) -> None:
        self.lower_limit = 100
        self.upper_limit = 999

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)
########## Temporary

class Question:
    def __init__(self, qstring, answer, question_type) -> None:
        self.qstring = qstring
        self.answer = answer
        self.type = question_type
    
    def __repr__(self) -> str:
        return f"[Question] {self.qstring} \tAnswer: {self.answer}"

class QuestionGenerator(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def question(self) -> Question:
        pass

class AdditionQuestionGenerator(QuestionGenerator):
    TYPE = "add"
    def __init__(self, no_of_nums:int, num_gen_strat) -> None:
        super().__init__()
        self.no_of_nums = no_of_nums
        self.num_gen_strat = num_gen_strat
        if self.no_of_nums < 2: raise Exception("Invalid No of Arguments")
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        question_string = " + ".join(map(str, num_list))
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

"""    def type1(self):
        num_list = []
        for i in range(2):
            num_list.append(random.randint(1, 20))
        format_string = " + ".join(["{}" for _ in range(self.no_of_nums)])
        question_string = format_string.format(*num_list)
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

    def  type2(self):
        num_list = []
        for i in range(2):
            num_list.append(random.randint(50, 99))
        format_string = " + ".join(["{}" for _ in range(self.no_of_nums)])
        question_string = format_string.format(*num_list)
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

    def  type3(self):
        num_list = []
        for i in range(3):
            num_list.append(random.randint(50, 99))
        format_string = " + ".join(["{}" for _ in range(self.no_of_nums)])
        question_string = format_string.format(*num_list)
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")"""

class SubtractionQuestionGenerator(QuestionGenerator):
    TYPE = "sub"
    def __init__(self,no_of_nums:int, num_gen_strat) -> None:
        super().__init__()
        self.no_of_nums = no_of_nums
        self.num_gen_strat = num_gen_strat
        if self.no_of_nums < 2: raise Exception("Invalid No of Arguments")
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        question_string = " - ".join(map(str, num_list))
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

class MultiplicationQuestionGenerator(QuestionGenerator):
    TYPE = "mul"
    def __init__(self,no_of_nums:int, num_gen_strat) -> None:
        super().__init__()
        self.no_of_nums = no_of_nums
        self.num_gen_strat = num_gen_strat
        if self.no_of_nums < 2: raise Exception("Invalid No of Arguments")
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        question_string = " * ".join(map(str, num_list))
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

class DivisionQuestionGenerator(QuestionGenerator):
    TYPE = "div"
    def __init__(self,no_of_nums:int, num_gen_strat) -> None:
        super().__init__()
        self.no_of_nums = no_of_nums
        self.num_gen_strat = num_gen_strat
        if self.no_of_nums < 2: raise Exception("Invalid No of Arguments")
    
    def question(self) -> Question:
        num_list = []
        base_num = self.num_gen_strat.number()
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.multipleNumber(base_num))
        question_string = " / ".join(map(str, num_list))
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

class LCMQuestionGenerator(QuestionGenerator):
    TYPE = "add"
    def __init__(self, no_of_nums:int, num_gen_strat) -> None:
        super().__init__()
        self.no_of_nums = no_of_nums
        self.num_gen_strat = num_gen_strat
        if self.no_of_nums < 2: raise Exception("Invalid No of Arguments")
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        question_string = "Find LCM of " + ", ".join(map(str, num_list))
        answer = self.findAnswer(num_list)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")
    
    def gcd(self, num1, num2):
        pass

    def findAnswer(self, num_list):
        return 1

class HCFQuestionGenerator(QuestionGenerator):
    TYPE = "add"
    def __init__(self, no_of_nums:int, num_gen_strat) -> None:
        super().__init__()
        self.no_of_nums = no_of_nums
        self.num_gen_strat = num_gen_strat
        if self.no_of_nums < 2: raise Exception("Invalid No of Arguments")
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        question_string = "Find HCF of " + ", ".join(map(str, num_list))
        answer = self.findAnswer(num_list)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")
    
    def gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def findAnswer(self, num_list):
        num_list = sorted(num_list)
        num1 = num_list[0]
        num2 = num_list[1]
        hcf = self.gcd(num1, num2)
        for n in num_list[2:]:
            hcf = self.gcd(hcf, n)
        return hcf
class QuadraticQuestionGenerator(QuestionGenerator):
    TYPE = "quad"
    def __init__(self, num_gen_strat) -> None:
        super().__init__()
        self.num_gen_strat = num_gen_strat
    
    def question(self) -> Question:
        alpha= self.num_gen_strat.number()
        beta= self.num_gen_strat.number()
        question_string= f"x^2 +{alpha+ beta}x + {alpha* beta} = 0"
        answer = (alpha, beta)
        return Question(question_string, answer, f"{self.TYPE}")

class Linear2VarQuestionGenerator(QuestionGenerator):
    TYPE = "linear2var"
    def __init__(self, num_gen_strat) -> None:
        super().__init__()
        self.num_gen_strat = num_gen_strat

    def getPoints(self):
        return ((self.num_gen_strat.number(), self.num_gen_strat.number()) for _i in range(3))

    def getEquation(self, point, ans_point):
        a = (ans_point[1] - point[1])
        b = (ans_point[0] - point[0]) * -1
        c = -(point[0] * (ans_point[1] - point[1])) + (point[1] * (ans_point[0] - point[0]))
        if(a < 0):
            a*= -1
            b*= -1
            c*= -1
        return f"{a}x + {b}y + {c} = 0"

    def question(self) -> Question: # Temprary Algo (Sign Optimization Required and Wrong answer)
        p1, p2, p3 = self.getPoints()
        eq1 = self.getEquation(p1, p3)
        eq2 = self.getEquation(p2, p3)
        question_string = f"{eq1};{eq2}"
        answer = p3
        return Question(question_string, answer, f"{self.TYPE}")

class SimpleInterestQuestionGenerator(QuestionGenerator):
    pass

class CompoundInterestQuestionGenerator(QuestionGenerator):
    pass

if __name__ == "__main__":
    qg = QuadraticQuestionGenerator(LargeNumberGenerator())
    for _  in range(5):
        question = qg.question()
        print(question)
