# Stratergy Pattern Test
from abc import ABC, abstractmethod
from question import Question
import random, math

class QuestionType(ABC):
    @abstractmethod
    def generate_question(self, *args, **kwargs):
        ...

class AdditionQuestionType1(QuestionType):
    Q_TYPE = "addition type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "+"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType1(QuestionType):
    Q_TYPE = "subtraction type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        first_num = sum(num_list) + number_gen_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType2(QuestionType):
    Q_TYPE = "subtraction type2"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        first_num = sum(num_list) - number_gen_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType3(QuestionType):
    Q_TYPE = "subtraction type3"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        if number_of_nums %2 != 0: raise Exception("number_of_nums must be even")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums//2)
        num_list += [-n for n in num_list]
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class MultiplicationQuestionType1(QuestionType):
    Q_TYPE = "multiplication type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class MultiplicationQuestionType2(QuestionType):
    Q_TYPE = "multiplication type2"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums//2)
        num_list += number_gen_obj.numbers(self.number_of_nums - self.number_of_nums//2, is_negative=True)
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class DivisionQuestionType1(QuestionType):
    Q_TYPE = "division type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "/"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums
    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class DivisionQuestionType2(QuestionType):
    Q_TYPE = "division type2"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "/"
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums//2)
        num_list += number_gen_obj.numbers(self.number_of_nums - self.number_of_nums//2, is_negative=True)
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return Question(question_string, eval(question_string), self.Q_TYPE.title())

class LCMQuestionType1(QuestionType):
    Q_TYPE = "lcm type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = "Find LCM of: " + format_string.format(*num_list)
        return Question(question_string, self.findLCM(num_list), self.Q_TYPE.title())
    
    def findLCM(self, num_list):
        return 1
    

class HCFQuestionType1(QuestionType):
    Q_TYPE = "hcf type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = "Find HCF of: " + format_string.format(*num_list)
        return Question(question_string, self.findHCF(num_list),self.Q_TYPE.title())

    def findHCF(self, num_list):
        def gcd(n,d):
            if (d == 0):
                return n
            return gcd(d, n%d)

        def gcdArray(num_list:list):
            num_list.sort()
            hcf = num_list.pop()
            while len(num_list):
                print(hcf, num_list[0])
                hcf = gcd(hcf, num_list[0])
                num_list.pop(0)
            return hcf
        return gcdArray(num_list)

"""class MissingFactorsQuestionType1(QuestionType):
    Q_TYPE = "missing factors type1"
    def generate_question(self, gen_type):
        pass"""

class QuadraticQuestionType1(QuestionType):
    Q_TYPE = "quadratic type1"
    def generate_question(self, number_gen_obj):
        format_string = "{}x^2 - {}x + {} = 0"
        roots = number_gen_obj.numbers(2)
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return Question(question_string, roots, self.Q_TYPE.title())

"""class QuadraticQuestionType2(QuestionType):
    Q_TYPE = "quadratic type2"
    def generate_question(self, number_gen_obj):
        format_string = "{}x^2 + {}x + {} = 0"
        roots = number_gen_obj.numbers(2)
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return Question(question_string, roots, self.Q_TYPE.title())"""

class Linear2VarQuestionType1(QuestionType):
    Q_TYPE = "linear 2 var type1"
    def generate_question(self, number_gen_obj):
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
    Q_TYPE = "simple interest type1"
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
        return Question(question_string, self.findSI(p, n, r), self.Q_TYPE.title())

    def findSI(self, p, n, r):
        pass

class CompundInterestQuestionType1(QuestionType):
    Q_TYPE = "compund interest type1"
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
        return Question(question_string, self.findCI(p, n, r), self.Q_TYPE.title())

    def findCI(self, p, n, r):
        pass

if __name__ == "__main__":
    def runAll():
        import numberGen
        for g in [AdditionQuestionType1, SubtractionQuestionType1, SubtractionQuestionType2, SubtractionQuestionType3, MultiplicationQuestionType1, MultiplicationQuestionType2, LCMQuestionType1, HCFQuestionType1]:
            n_num = int(input("How many numbers do you want? \n>"))
            gen_obj = g(n_num)
            question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(1, 25))
            print(f"{question.type} \n {question}")
    
        for g in [QuadraticQuestionType1, Linear2VarQuestionType1]:
            gen_obj = g()
            question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(1, 25))
            print(f"{question.type} \n {question}")
    
    def main():
        import numberGen
        gen_obj = QuadraticQuestionType1()
        question:Question = gen_obj.generate_question(numberGen.RangedIntegerNumberGenerator(1, 25))
        print(f"{question.type}")
        print(f"{question}")
        print()
    
    print("Hello World! 🔥")
    # Run Code Here
    main()
    print("Done ✅")