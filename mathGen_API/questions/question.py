from abc import ABC, abstractmethod

class Question:
    def __init__(self, q_string, answer, question_type, difficulty) -> None:
        self.string = q_string
        self.answer = answer
        self.type = question_type
        self.difficulty = difficulty
    
    def __repr__(self) -> str:
        return f"{self.string} \nAnswer: {self.answer}"

##############################
# Question Generator Abstract
##############################
class QuestionGenerator(ABC):
    EAZY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

    def __init__(self, number_generator) -> None:
        super().__init__()
        self.number_generator = number_generator

    @abstractmethod
    def question(self) -> Question:
        pass

##############################
# Question Generator Types
# - AdditionQuestion
# - SubtractionQuestion
# - MultiplicationQuestion
# - DivisionQuestion
# - LCMQuestion
# - HCFQuestion
# - QuadraticQuestion
# - Linear2VariableQuestion
# - PercentageQuestion
##############################
class AdditionQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class SubtractionQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class MultiplicationQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class DivisionQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class LCMQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class HCFQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class QuadraticQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class Linear2VariableQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

class PercentageQuestion(QuestionGenerator):
    def question(self) -> Question:
        return super().question()

##############################
# Question Generator Factory
##############################
class QuestionGenerator_Factory:
    pass

