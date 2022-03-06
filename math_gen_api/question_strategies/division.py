# question_strategies/division.py

# In-built imports
import random

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
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "/"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums
    
    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums)]
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

class DivisionQuestionType2(question.QuestionType):
    Q_TYPE = "Division_Type2"
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "/"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums//2)]
        num_list += [self.number_generator_obj.number(is_negative=True) for _  in range(self.number_of_nums - self.number_of_nums//2)]
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

TYPE_LOOKUP = {
    1: DivisionQuestionType1,
    2: DivisionQuestionType2
}