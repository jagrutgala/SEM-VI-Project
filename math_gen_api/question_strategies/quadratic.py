# In-built imports
import math

# Third-party imports

# Relative imports
import question

class QuadraticQuestionType1(question.QuestionType):
    Q_TYPE = "quadratic type1"
    def generate_question(self, number_gen_obj):
        format_string = "{}x^2 - {}x + {} = 0"
        roots = number_gen_obj.numbers(2)
        coefficient = [1, sum(roots), math.prod(roots)]
        question_string = format_string.format(*coefficient)
        return question.Question(question_string, roots, self.Q_TYPE.title())

# class QuadraticQuestionType2(question.QuestionType):
#     Q_TYPE = "quadratic type2"
#     def generate_question(self, number_gen_obj):
#         format_string = "{}x^2 + {}x + {} = 0"
#         # Type2 functionality here
#         return question.Question(question_string, roots, self.Q_TYPE.title())
