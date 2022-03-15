# question_strategies/factors.py
# In-built imports
from typing import Type
import math, random

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

class FactorsQuestionType1(question.QuestionType):
    Q_TYPE = "Factors_Type1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }

    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums
    
    def generate_question(self) -> question.Question:
        num = self.number_generator_obj.number()
        factors = self.factorlist(num)
        num_set1 = random.choice(factors)
        if len(factors) > 1:
            factors.remove(num_set1)
        num_set2 = random.choice(factors)
        question_string = f"Find the Missing Factor: {num_set1[0]}x{'?'}  = {num_set2[0]}x{num_set2[1]}"
        return question.Question(question_string, num_set1[1], self.Q_TYPE.title())

    def factorlist(self, num:int):
        fac_list = []
        for i in range(1, int(math.sqrt(num)+1)):
            if num % i == 0:
                quotient = num // i
                if ((quotient, i) in fac_list): continue
                fac_list.append((i, quotient))
        return list(fac_list)

class FactorsQuestionType2(question.QuestionType):
    Q_TYPE = "Factors_Type2"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }

    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "*"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums
    
    def generate_question(self) -> question.Question:
        num = self.number_generator_obj.number()
        question_string = f"List all Factors of : {num}"
        return question.Question(question_string, self.factorlist(num), self.Q_TYPE.title())

    def factorlist(self, num:int):
        fac_list = []
        for i in range(1, int(num)):
            if num % i == 0:
                fac_list.append((i))
        return list(fac_list)

TYPE_LOOKUP:dict[str, Type[question.QuestionType]] = {
    "missing": FactorsQuestionType1,
    "list": FactorsQuestionType2
}