from abc import ABC, abstractmethod
from numberGen import PositiveNumberGenerator

class Question:
    def __init__(self, qstring, answer, question_type) -> None:
        self.qstring = qstring
        self.answer = answer
        self.type = question_type
    
    def __repr__(self) -> str:
        return f"[Question] {self.qstring} \tAnswer: {self.answer}"


##############################
# Question Generator Abstract
##############################
class QuestionGenerator(ABC):
    """
    Required Inputs
    - number_of_numbers_needed
    - types_of_numbers_needed (ordered)
    - position_of_numbers_needed (ordered)
    """
    EAZY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    @abstractmethod
    def question(self) -> Question:
        pass

##############################
# Question Generator Types
# - AdditionQuestion
# - SubtractionQuestion
# - MultiplicationQuestion
# - DivisionQuestion
# - LCMQuestion
# - HCFQuestion
# - QuadraticQuestion
# - Linear2VariableQuestion
# - PercentageQuestion
# - LogQuestion

##############################
"""class AdditionQuestion(QuestionGenerator):
    TYPE = "addition"
    def question(self) -> Question:
        num1 , num2 = (self.number_generator.number() for _ in range(2))
        string = f"{num1} + {num2}"
        answer = num1 + num2
        return Question(string, answer, self.TYPE, self.DIFFICULTY)

class SubtractionQuestion(QuestionGenerator):
    TYPE = "subtraction"
    def question(self) -> Question:
        num1 , num2 = (self.number_generator.number() for _ in range(2))
        string = f"{num1} - {num2}"
        answer = num1 - num2
        return Question(string, answer, self.TYPE, self.DIFFICULTY)

class MultiplicationQuestion(QuestionGenerator):
    TYPE = "multiplication"
    def question(self) -> Question:
        num1 , num2 = (self.number_generator.number() for _ in range(2))
        string = f"{num1} * {num2}"
        answer = num1 * num2
        return Question(string, answer, self.TYPE, self.DIFFICULTY)

class DivisionQuestion(QuestionGenerator):
    TYPE = "division"
    def question(self) -> Question:
        num1 , num2 = (self.number_generator.number() for _ in range(2))
        # zero division check
        string = f"{num1} / {num2}"
        answer = num1 / num2
        return Question(string, answer, self.TYPE, self.DIFFICULTY)"""

class LCMQuestion(QuestionGenerator):
    TYPE = "lcm"
    format_string = "Find LCM of these numbers: "
    def __init__(self, type_list=None) -> None:
        super().__init__()
        self.type_list = type_list if type_list is not None else tuple([PositiveNumberGenerator for _ in range(3)])
        self.length = len(self.type_list)

    def numberByType(self, num_type, **kwargs):
        return num_type().number()

    def questionString(self, num_list, separator=", "):
        return self.format_string + f"{separator}".join(map(str, num_list)).format(*num_list)

    def question(self) -> Question:
        num_list = list()
        for i in self.type_list:
            num_list.append(self.numberByType(i))
        return Question(self.questionString(num_list, ", "), self.findAnswer(num_list), self.TYPE)

    def findAnswer(self, num_list):
        return 1


        # if self.DIFFICULTY is self.HARD:
        #     n = self.number_generator.rangeNumber(6, 9)
        # elif self.DIFFICULTY is self.MEDIUM:
        #     n = self.number_generator.rangeNumber(3, 6)
        # else:
        #     n = 2
        # num_list = (self.number_generator.number() for _ in range(n))
        # string = f"Find LCM of the following numbers: " + ",".join(map(str, num_list))
        # answer = self.findAnswer(num_list)
        # return Question(string, answer, self.TYPE, self.DIFFICULTY)

class HCFQuestion(QuestionGenerator):
    TYPE = "hcf"
    format_string = "Find HCF of these numbers: "
    def __init__(self, type_list=None) -> None:
        super().__init__()
        self.type_list = type_list if type_list is not None else tuple([PositiveNumberGenerator for _ in range(3)])
        self.length = len(self.type_list)

    def numberByType(self, num_type, **kwargs):
        return num_type.number()

    def questionString(self, num_list, separator=", "):
        return self.format_string + f"{separator}".join(map(str, num_list)).format(*num_list)

    def question(self) -> Question:
        num_list = list()
        for i in self.type_list:
            num_list.append(self.numberByType(i))
        return Question(self.questionString(num_list, ", "), self.findAnswer(num_list), self.TYPE)

    def findAnswer(self, num_list):
        return 1

"""class QuadraticQuestion(QuestionGenerator):
    TYPE = "quadratic"
    def question(self) -> Question:
        return super().question()

class Linear2VariableQuestion(QuestionGenerator):
    TYPE = "lin2var"
    def question(self) -> Question:
        return super().question()

class PercentageQuestion(QuestionGenerator):
    TYPE = "percent"
    def question(self) -> Question:
        return super().question()"""

##############################
# Question Generator Factory
##############################
class QuestionGenerator_Factory:
    
    _available_types = ["bas", "add", "sub", "mul", "div", "lcm", "hcf", "fac"]

    @property
    def available_types(self):
        return self._available_types

    @classmethod
    def buildLCMQuestionGenerator(cls, num_types):
        return LCMQuestion(num_types)



if __name__ == "__main__":
    print("Hello World!")
    addq = QuestionGenerator_Factory.buildLCMQuestionGenerator((PositiveNumberGenerator, PositiveNumberGenerator, PositiveNumberGenerator,PositiveNumberGenerator,PositiveNumberGenerator))
    question = addq.question()
    print(question)