# question_strategies/subtraction.py
# In-built imports
import random
from typing import Type, Union

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

class SubtractionQuestionType1(question.QuestionType):
    Q_TYPE = "Subtraction_Type1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums)]
        first_num = sum(num_list) + self.number_generator_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE)

class SubtractionQuestionType2(question.QuestionType):
    Q_TYPE = "Subtraction_Type2"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums)]
        first_num = sum(num_list) + self.number_generator_obj.number(is_negative=True)
        question_string = format_string.format(first_num, *num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE)

class SubtractionQuestionType3(question.QuestionType):
    Q_TYPE = "Subtraction_Type3"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        if (number_of_nums % 2) != 0: raise Exception("number_of_nums must be even")
        self.number_of_nums = number_of_nums

    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums//2)]
        num_list += [n for n in num_list]
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

TYPE_LOOKUP:dict[str, Type[question.QuestionType]] = {
    "positive": SubtractionQuestionType1,
    "negative": SubtractionQuestionType2,
    "zeros": SubtractionQuestionType3
}