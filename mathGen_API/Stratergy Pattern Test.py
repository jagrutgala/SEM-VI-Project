# Stratergy Pattern Test
from abc import ABC, abstractmethod

class QuestionGeneration(ABC):
    @abstractmethod
    def question(self, **kwargs):
        pass

class BasicQuestionGeneration(QuestionGeneration):
    type_ = "basic"
    def question(self, **kwargs):
        print(f"{self.type_} stratergy implemented")

class LCMQuestionGeneration(QuestionGeneration):
    type_ = "lcm"
    def question(self, **kwargs):
        print(f"{self.type_} stratergy implemented")

class HCFQuestionGeneration(QuestionGeneration):
    type_ = "hcf"
    def question(self, **kwargs):
        print(f"{self.type_} stratergy implemented")

QUESTION_TYPE_LOOKUP = {
    "basic": BasicQuestionGeneration,
    "lcm": LCMQuestionGeneration,
    "hcf": HCFQuestionGeneration
}

def question(type_):
    question = QUESTION_TYPE_LOOKUP[type_]().question()


if __name__ == "__main__":
    print(f"Available stratergies: {', '.join(QUESTION_TYPE_LOOKUP.keys())}\n")
    stratergy = input("What stratergy do you want to use ? >\n")
    question(stratergy)

