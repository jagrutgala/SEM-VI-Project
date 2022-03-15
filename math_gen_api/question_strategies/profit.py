# question_strategies/addition.py
# In-built imports
from typing import Type
import math

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

class ProfitQuestionType1(question.QuestionType):
    Q_TYPE = "ProfitType1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self) -> question.Question:
        format_string = "Find Profit Percentage When Cost Price is {} and Sell Price is {}"
        num_list = [self.number_generator_obj.number() for _ in range(2)]
        num_list.sort()
        cp, sp = num_list
        percentage = self.percent(cp, sp)
        question_string = format_string.format(cp, sp)
        return question.Question(question_string, percentage, self.Q_TYPE)

    def percent(self, cp, sp):
        return round(((sp - cp) / sp) * 100, 2)


class ProfitQuestionType2(question.QuestionType):
    Q_TYPE = "ProfitType2"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self) -> question.Question:
        format_string = "Find Cost Price Percentage When Profit Percentage is {} and Sell Price is {}"
        num_list = [self.number_generator_obj.number() for _ in range(2)]
        num_list.sort()
        cp, sp = num_list
        percentage = self.percent(cp, sp)
        question_string = format_string.format(percentage, sp)
        return question.Question(question_string, cp, self.Q_TYPE)

    def percent(self, cp, sp):
        return round(((sp - cp) / sp) * 100, 2)

class ProfitQuestionType3(question.QuestionType):
    Q_TYPE = "ProfitType3"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self) -> question.Question:
        format_string = "Find Sell Price Percentage When Profit Percentage is {} and Cost Price is {}"
        num_list = [self.number_generator_obj.number() for _ in range(2)]
        num_list.sort()
        cp, sp = num_list
        percentage = self.percent(cp, sp)
        question_string = format_string.format(percentage, cp)
        return question.Question(question_string, sp, self.Q_TYPE)

    def percent(self, cp, sp):
        return round(((sp - cp) / sp) * 100, 2)

TYPE_LOOKUP:dict[str, Type[question.QuestionType]] = {
    "Find Profit": ProfitQuestionType1,
    "FInd Cost": ProfitQuestionType2,
    "Find Sell": ProfitQuestionType3
}

