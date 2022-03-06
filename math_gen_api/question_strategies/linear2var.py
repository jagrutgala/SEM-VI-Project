# In-built imports

# Third-party imports

# Relative imports
import question

class Linear2VarQuestionType1(question.QuestionType):
    Q_TYPE = "linear 2 var type1"
    def generate_question(self, number_gen_obj):
        format_string = "{}x + {}y + {} = 0;{}x + {}y + {} = 0;"
        p1 = number_gen_obj.numbers(2)
        p2 = number_gen_obj.numbers(2)
        sol = number_gen_obj.numbers(2)
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
