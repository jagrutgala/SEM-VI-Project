# In-built imports

# Third-party imports

# Relative imports
import question

class LCMQuestionType1(question.QuestionType):
    Q_TYPE = "lcm type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums
    
    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = "Find LCM of: " + format_string.format(*num_list)
        return question.Question(question_string, self.findLCM(num_list), self.Q_TYPE.title())
    
    def findLCM(self, num_list):
        return 1

class HCFQuestionType1(question.QuestionType):
    Q_TYPE = "hcf type1"
    def __init__(self, number_of_nums) -> None:
        super().__init__()
        self.operator = ","
        if number_of_nums < 2: raise Exception("number_of_nums musst be 2 or greater")
        self.number_of_nums = number_of_nums
    
    def generate_question(self, number_gen_obj):
        format_string = f" {self.operator} ".join(["{}" for _ in range(self.number_of_nums)])
        num_list = number_gen_obj.numbers(self.number_of_nums)
        question_string = "Find HCF of: " + format_string.format(*num_list)
        return question.Question(question_string, self.findHCF(num_list),self.Q_TYPE.title())
    
    def findHCF(self, num_list):
        def gcd(n,d):
            if (d == 0):
                return n
            return gcd(d, n%d)

        def gcdArray(num_list:list):
            num_list.sort()
            hcf = num_list.pop()
            while len(num_list):
                print(hcf, num_list[0])
                hcf = gcd(hcf, num_list[0])
                num_list.pop(0)
            return hcf
        return gcdArray(num_list)

# class MissingFactorsQuestionType1(question.QuestionType):
#     Q_TYPE = "missing factors type1"
#     def generate_question(self, gen_type):
#         pass
