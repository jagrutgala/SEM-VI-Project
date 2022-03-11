# question_strategies/addition.py
# In-built imports
from typing import Type

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

class SquareQuestionType1(question.QuestionType):
    Q_TYPE = "SquareType1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=1) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "+"
        if number_of_nums < 1: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self) -> question.Question:
        format_string = f"Find Square of: " + f"{self.operator}".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums)]
        question_string = format_string.format(*num_list)
        return question.Question(question_string, self.sq(num_list), self.Q_TYPE)

    def sq(self, num_list):
        return [i*i for i in num_list]

TYPE_LOOKUP:dict[int, Type[question.QuestionType]] = {
    1: SquareQuestionType1
}
