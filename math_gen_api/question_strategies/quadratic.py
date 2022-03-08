# question_strategies/quadratic.py
# In-built imports
import math
from typing import Type

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

class QuadraticQuestionType1(question.QuestionType):
    Q_TYPE = "Quadratic_Type1"
    def __init__(self, number_generator_cls:question.numGenType) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
    
    def generate_question(self):
        format_string = "{}x^2 - {}x + {} = 0"
        roots = [self.number_generator_obj.number() for _ in range(2)]
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return question.Question(question_string, roots, self.Q_TYPE.title())

# class QuadraticQuestionType2(question.QuestionType):
#     Q_TYPE = "Quadratic_Type1"
#     def __init__(self, number_generator_cls:question.numGenType) -> None:
#         super().__init__()
#         self.number_generator_obj = number_generator_cls
#     
#     def generate_question(self):
#         format_string = "{}x^2 - {}x + {} = 0"
#         roots = [self.number_generator_obj.number() for _ in range(2)]
#         coefficient = [1, sum(roots), math.prod(roots)]
#         question_string = format_string.format(*coefficient)
#         return question.Question(question_string, roots, self.Q_TYPE.title())

TYPE_LOOKUP:dict[int, Type[question.QuestionType]] = {
    1: QuadraticQuestionType1
}