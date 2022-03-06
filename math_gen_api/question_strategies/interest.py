# In-built imports

# Third-party imports

# Relative imports
import question

class SimpleInterestQuestionType1(question.QuestionType):
    Q_TYPE = "simple interest type1"
    def generate_question(self, number_gen_obj):
        format_string = "SI Question principal={} year={} rate={}"
        number_gen_obj.lower_limit(1000)
        number_gen_obj.upper_limit = 100000
        p = number_gen_obj.number()
        number_gen_obj.lower_limit = 1
        number_gen_obj.upper_limit = 10
        n = number_gen_obj.number()
        r = number_gen_obj.number()
        question_string = format_string.format(p, n, r)
        return question.Question(question_string, self.findSI(p, n, r), self.Q_TYPE.title())

    def findSI(self, p, n, r):
        pass

class CompundInterestQuestionType1(question.QuestionType):
    Q_TYPE = "compund interest type1"
    def generate_question(self, number_gen_obj):
        format_string = "CI Question principal={} year={} rate={}"
        number_gen_obj.lower_limit = 1000
        number_gen_obj.upper_limit = 100000
        p = number_gen_obj.number()
        number_gen_obj.lower_limit = 1
        number_gen_obj.upper_limit = 10
        n = number_gen_obj.number()
        r = number_gen_obj.number()
        question_string = format_string.format(p, n, r)
        return question.Question(question_string, self.findCI(p, n, r), self.Q_TYPE.title())

    def findCI(self, p, n, r):
        pass
