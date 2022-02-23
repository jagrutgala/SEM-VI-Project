from abc import ABC
import re, random


##############################
# NUM GEN TYPES REGEX
# - negative
# {\d,\d]} ranged limit
# !\d not include \d
##############################

def getNumberFromNumberType(num_type:str=""):
    found = re.search("(-)?(\{\d+,\d+\}|!\d+)?", str(num_type))
    lower_limit = 1
    upper_limit = 1000
    negative = 1
    if found is not None:
        result = found.groups()
        if result[0] is not None: negative = -1
        if result[1] is not None:
            lower_limit, upper_limit = map(int, re.findall("\d+", result[1]))
    number = random.randint(lower_limit, upper_limit)
    number *= negative
    return number

class Question(ABC):
    TYPE = "Question"
    def __init__(self, question_string, answer_func) -> None:
        super().__init__()
        self.question_string = question_string
        self.__answer_func = answer_func

    @property
    def answer(self):
        return self.__answer_func(self.question_string)

    def __repr__(self) -> str:
        return f"[Question] {self.question_string} \tAnswer: {self.answer}"

class AdditionQuestion(Question):
    def __init__(self, num_gen_type_list) -> None:
        if len(num_gen_list) < 2: raise Exception("num_gen_type_list length needs to be atleast 2")
        separator_string = " + "
        num_list = [getNumberFromNumberType(num_gen) for num_gen in num_gen_type_list]
        def answer_func(question_string):
            return eval(question_string) 
        super().__init__(separator_string.join(map(str, num_list)), answer_func)

# Addition Question
format_string = ""

if __name__ == "__main__":
    num_gen_list = ["{1,25}", "{10,15}", "{20,40}"]
    q = AdditionQuestion(num_gen_list)
    print(q)
