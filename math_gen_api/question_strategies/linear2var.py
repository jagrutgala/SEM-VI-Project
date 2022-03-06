# question_strategies/linear2var.py
# In-built imports

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import question

class Linear2VarQuestionType1(question.QuestionType):
    Q_TYPE = "Linear_2_Var_Type1"
    def __init__(self, number_generator_cls:question.numGenType) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
    
    def generate_question(self):
        format_string = "{}x + {}y + {} = 0;{}x + {}y + {} = 0;"
        p1 = [self.number_generator_obj.number() for _ in range(2)]
        p2 = [self.number_generator_obj.number() for _ in range(2)]
        sol = [ self.number_generator_obj.number() for _ in range(2)]
        c1 = self.generate_coefficient(p1, sol)
        c2 = self.generate_coefficient(p2, sol)
        question_string = format_string.format(*c1, *c2)
        return question.Question(question_string, sol, self.Q_TYPE.title())

    def generate_coefficient(self, point, ans_point):
        a = (ans_point[1] - point[1])
        b = (ans_point[0] - point[0]) * -1
        c = -(point[0] * (ans_point[1] - point[1])) + (point[1] * (ans_point[0] - point[0]))
        if(a < 0):
            a*= -1
            b*= -1
            c*= -1
        return [a, b, c]

TYPE_LOOKUP = {
    1: Linear2VarQuestionType1
}