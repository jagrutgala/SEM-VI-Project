# question_strategies/lcm.py
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

class LCMQuestionType1(question.QuestionType):
    Q_TYPE = "LCM_Type1"
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
        question_string = "Find LCM of: " + format_string.format(*num_list)
        return question.Question(question_string, self.findLCM(num_list), self.Q_TYPE)
    
    def gcd(self, a:int, b:int) -> int:
        if (b == 0):
            return a
        return self.gcd(b, a % b)
    
    def findLCM(self, arr:list[int]) -> Union[int, float]:
        ans = arr[0]
        for i in range(1, len(arr)):
            ans = (arr[i] * ans) / self.gcd(arr[i], ans)
        return ans

TYPE_LOOKUP:dict[str, Type[question.QuestionType]] = {
    "normal": LCMQuestionType1
}