# In-built imports
import random

# Third-party imports

# Relative imports
import question

class SubtractionQuestionType1(question.QuestionType):
    Q_TYPE = "subtraction type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        first_num = sum(num_list) + number_gen_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType2(question.QuestionType):
    Q_TYPE = "subtraction type2"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        first_num = sum(num_list) - number_gen_obj.number()
        question_string = format_string.format(first_num, *num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())

class SubtractionQuestionType3(question.QuestionType):
    Q_TYPE = "subtraction type3"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = "-"
        if number_of_nums < 2: raise Exception("number_of_nums must be 2 or greater")
        if number_of_nums %2 != 0: raise Exception("number_of_nums must be even")
        self.number_of_nums = number_of_nums

    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums//2)
        num_list += [-n for n in num_list]
        random.shuffle(num_list)
        question_string = format_string.format(*num_list)
        return question.Question(question_string, eval(question_string), self.Q_TYPE.title())
