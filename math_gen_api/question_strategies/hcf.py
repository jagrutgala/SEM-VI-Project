# question_strategies/hcf.py
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

class HCFQuestionType1(question.QuestionType):
    Q_TYPE = "HCF_Type1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int=2) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self) -> question.Question:
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums)]
        question_string = "Find HCF of: " + format_string.format(*num_list)
        return question.Question(question_string, self.findHCF(num_list), self.Q_TYPE)
    
    def findHCF(self, num_list:list):
        def gcd(n,d):
            if (d == 0):
                return n
            return gcd(d, n%d)

        def gcdArray(num_list:list):
            num_list.sort()
            hcf = num_list.pop()
            while len(num_list):
                # print(hcf, num_list[0])
                hcf = gcd(hcf, num_list[0])
                num_list.pop(0)
            return hcf
        return gcdArray(num_list)

TYPE_LOOKUP:dict[str, Type[question.QuestionType]] = {
    "normal": HCFQuestionType1
}