# question_strategies/division.py

# In-built imports
from typing import Type, Union

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

class DivisionQuestionType1(question.QuestionType):
    Q_TYPE = "Division_Type1"
    def __init__(self, number_generator_cls:question.numGenType) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "/"
        self.number_of_nums = 2
    
    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        multiple_number_func = lambda x: [x * self.number_generator_obj.number(), x]
        num_list = multiple_number_func(self.number_generator_obj.number())
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

class DivisionQuestionType2(question.QuestionType):
    Q_TYPE = "Division_Type2"
    INIT_VARIABLES= {}
    def __init__(self, number_generator_cls:question.numGenType) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "/"
        self.number_of_nums = 2
    
    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        multiple_number_func = lambda x: [x * self.number_generator_obj.number(is_negative=True), x]
        num_list = multiple_number_func(self.number_generator_obj.number())
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

class DivisionQuestionType3(question.QuestionType):
    Q_TYPE = "Division_Type2"
    def __init__(self, number_generator_cls:question.numGenType) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "/"
        self.number_of_nums = 2
    
    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        multiple_number_func = lambda x: [x * self.number_generator_obj.number(), x]
        num_list = multiple_number_func(self.number_generator_obj.number(is_negative=True))
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

TYPE_LOOKUP:dict[int, Type[question.QuestionType]] = {
    1: DivisionQuestionType1,
    2: DivisionQuestionType2,
    3: DivisionQuestionType3
}