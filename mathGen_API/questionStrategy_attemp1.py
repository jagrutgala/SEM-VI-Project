# Stratergy Pattern Test
from abc import ABC, abstractmethod

class QuestionType(ABC):
    @abstractmethod
    def create_question(self):
        pass

class AdditionQuestionType1(QuestionType):
    def create_question(self, number_gen_obj):
        pass

"""class SubtractionQuestionType1(QuestionType):
    def create_question(self, gen_type):
        pass

class MultiplicationQuestionType1(QuestionType):
    def create_question(self, gen_type):
        pass

class DivisionQuestionType1(QuestionType):
    def create_question(self, gen_type):
        pass

class LCMQuestionType1(QuestionType):
    def create_question(self, gen_type):
        pass

class HCFQuestionType1(QuestionType):
    def create_question(self, gen_type):
        pass

class MissingFactorsQuestionType1(QuestionType):
    def create_question(self, gen_type):
        pass"""

if __name__ == "__main__":
    print("Hello World! :)")
    print("Done ✅")

