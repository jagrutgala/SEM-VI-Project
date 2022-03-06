# In-built imports

# Third-party imports

# Relative imports
import question

print("addition")

class AdditionQuestionType1(question.QuestionType):
    Q_TYPE = "addition type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "+"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

