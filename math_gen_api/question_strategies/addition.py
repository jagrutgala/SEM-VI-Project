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

class AdditionQuestionType1(question.QuestionType):
    Q_TYPE = "AdditionType1"
    def __init__(self, number_generator_cls:question.numGenType, number_of_nums:int) -> None:
        super().__init__()
        self.number_generator_obj = number_generator_cls
        self.operator = "+"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self) -> question.Question:
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = [self.number_generator_obj.number() for _ in range(self.number_of_nums)]
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE)

TYPE_LOOKUP = {
    1: AdditionQuestionType1
}



if __name__ == "__main__":
    # Code Here
    import sys
    from os.path import dirname, abspath
    package_path = dirname(dirname(abspath(__file__)))
    if(package_path not in sys.path): sys.path.insert(0, package_path)

    def main():
        from number_gen.integer_number import RangedIntegerNumberGenerator
        add_question_type = AdditionQuestionType1(RangedIntegerNumberGenerator(1, 9), 2)
        my_question:question.Question = add_question_type.generate_question()
        print(my_question)

    main()
