# To Figure out :??
# easily add new gen function to GEN_FUNCS
# refference to all the different question gen functions
# question gen func decorator

from abc import ABC, abstractmethod

class Question:
    def __init__(self, qstring, answer, question_type) -> None:
        self.qstring = qstring
        self.answer = answer
        self.type = question_type
    
    def __repr__(self) -> str:
        return f"[Question] {self.qstring} \tAnswer: {self.answer}"

class QuestionGenerator(ABC):
    def __init__(self, num_gen_strat) -> None:
        super().__init__()
        self.num_gen_strat = num_gen_strat

    @abstractmethod
    def question(self) -> Question:
        pass

class AdditionQuestionGenerator(QuestionGenerator):
    TYPE = "add"
    def __init__(self,no_of_nums:int, num_gen_strat) -> None:
        super().__init__(num_gen_strat)
        self.no_of_nums = no_of_nums
        if self.no_of_nums < 2: self.no_of_nums = 2
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        format_string = " + ".join(["{}" for _ in range(self.no_of_nums)])
        question_string = format_string.format(*num_list)
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

class SubtractionQuestionGenerator(QuestionGenerator):
    TYPE = "sub"
    def __init__(self,no_of_nums:int, num_gen_strat) -> None:
        super().__init__(num_gen_strat)
        self.no_of_nums = no_of_nums
        if self.no_of_nums < 2: self.no_of_nums = 2
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        format_string = " - ".join(["{}" for _ in range(self.no_of_nums)])
        question_string = format_string.format(*num_list)
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

class MultiplicationQuestionGenerator(QuestionGenerator):
    TYPE = "mul"
    def __init__(self,no_of_nums:int, num_gen_strat) -> None:
        super().__init__(num_gen_strat)
        self.no_of_nums = no_of_nums
        if self.no_of_nums < 2: self.no_of_nums = 2
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        format_string = " * ".join(["{}" for _ in range(self.no_of_nums)])
        question_string = format_string.format(*num_list)
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

class DivisionQuestionGenerator(QuestionGenerator):
    TYPE = "div"
    def __init__(self,no_of_nums:int, num_gen_strat) -> None:
        super().__init__(num_gen_strat)
        self.no_of_nums = no_of_nums
        if self.no_of_nums < 2: self.no_of_nums = 2
    
    def question(self) -> Question:
        num_list = []
        for i in range(self.no_of_nums):
            num_list.append(self.num_gen_strat.number())
        format_string = " / ".join(["{}" for _ in range(self.no_of_nums)])
        question_string = format_string.format(*num_list)
        answer = eval(question_string)
        return Question(question_string, answer, f"{self.TYPE}-{self.no_of_nums}")

class QuadraticQuestionGenerator(QuestionGenerator):
    TYPE = "quad"
    def __init__(self, num_gen_strat) -> None:
        super().__init__(num_gen_strat)
    
    def question(self) -> Question:
        alpha= self.num_gen_strat.number()
        beta= self.num_gen_strat.number()
        question_string= f"x^2 +{alpha+ beta}x + {alpha* beta} = 0"
        answer = (alpha, beta)
        return Question(question_string, answer, f"{self.TYPE}")

class Linear2VarQuestionGenerator(QuestionGenerator):
    TYPE = "linear2var"
    def __init__(self, num_gen_strat) -> None:
        super().__init__(num_gen_strat)

    def getPoints(self):
        return ((self.num_gen_strat.number(), self.num_gen_strat.number()) for _i in range(3))

    def getEquation(self, point, ans_point):
        a = (ans_point[1] - point[1])
        b = (ans_point[0] - point[0]) * -1
        c = (point[0] * (ans_point[1] - point[1])) - (point[1] * (ans_point[0] - point[0]))
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
