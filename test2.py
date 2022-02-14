# Characteristics of a Question
# string, type, difficulty, ans, fake_options?

# Characteristics of a Question Generator
# format string, 


from random import sample
from typing_extensions import Self

class Question:

    def __init__(self, q_type, q_string:str, q_diff, q_answer, q_options=None) -> None:
        self.q_type = q_type
        self.q_string = q_string
        self.q_diff = q_diff
        self.q_answer = q_answer
        self.q_options = q_options

    def __repr__(self) -> str:
        return f"{self.q_string} \nAns: {','.join(sample([*self.q_options, self.q_answer], len(self.q_options)+1))}"

def createQuestion(q_type, q_string, q_diff, ng_F, q_ans_F, q_options_F) -> Question:
    return Question("", "", "", "", "")

# Question Generator using composition
# composition parts (question_string, number_generator, ans_function, difficulty, )


class QuestionGenerator:
    def __init__(self, type, ng) -> None:
        pass

