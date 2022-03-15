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

class PermuataionQuestionType1(question.QuestionType):
    Q_TYPE = "PermuataionType1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls

    def generate_question(self) -> question.Question:
        n ,r = sorted([self.number_generator_obj.number() for i in range(2)], reverse=True)
        p = math.factorial(n) / math.factorial(n - r)
        print(p)
        question_string = f"Find the number of permutaions when n={n} and r={r} repeatation not allowed"
        return question.Question(question_string, p, self.Q_TYPE)

class PermuataionQuestionType2(question.QuestionType):
    Q_TYPE = "PermuataionType2"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls

    def generate_question(self) -> question.Question:
        n ,r = sorted([self.number_generator_obj.number() for i in range(2)], reverse=True)
        p = n**r
        question_string = f"Find the number of permutaions when n={n} and r={r} repeatation allowed"
        return question.Question(question_string, p, self.Q_TYPE)

TYPE_LOOKUP:dict[str, Type[question.QuestionType]] = {
    "without repeatation": PermuataionQuestionType1, # without repeatation
    "with repeatation": PermuataionQuestionType2 # with repeatation
}

