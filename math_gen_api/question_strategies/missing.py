# question_strategies/factors.py
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

class MissingFactorsQuestionType1(question.QuestionType):
    Q_TYPE = "Missing_Factors_Type1"
    INIT_VARIABLES= {
        "number_of_nums": "int"
    }
    def generate_question(self):
        pass

TYPE_LOOKUP:dict[int, Type[question.QuestionType]] = {
    1: MissingFactorsQuestionType1
}