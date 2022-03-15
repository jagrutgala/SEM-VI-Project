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

class CombinationQuestionType1(question.QuestionType):
    Q_TYPE = "CombinationType1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "+"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self) -> question.Question:
        n ,r = sorted([self.number_generator_obj.number() for i in range(2)], reverse=True)
        c = math.factorial(n) / math.factorial(r) * math.factorial(n - r)
        question_string = f"Find the number of combinations when n={n} and r={r}"
        return question.Question(question_string, c, self.Q_TYPE)

TYPE_LOOKUP:dict[str, Type[question.QuestionType]] = {
    "normal": CombinationQuestionType1
}

