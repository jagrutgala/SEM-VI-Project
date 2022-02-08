from typing_extensions import Self
import random

class Question:
    def __init__(self, q_string, answer, question_type, difficulty) -> None:
        self.string = q_string
        self.answer = answer
        self.type = question_type
        self.difficulty = difficulty
    
    def __repr__(self) -> str:
        return f"{self.string} \nAnswer: {self.answer}"

class QuestionGenerator:
    _registry = {}
    EAZY = "1"
    MEDIUM = "10"
    HARD = "100"

    def __init_subclass__(cls, pre_fix, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls._registry[pre_fix] = cls

    def __new__(cls: type[Self], pre_fix, **kwargs) -> Self:
        subclass = cls._registry[pre_fix]
        obj = object.__new__(subclass)
        return obj

    def __init__(self, pre_fix, **kwargs) -> None:
        self.q_type = pre_fix

    def create_question(self, difficulty):
        pass


class NumberGen:
    _registry = {}

    def __init_subclass__(cls, pre_fix, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls._registry[pre_fix] = cls

    def __new__(cls: type[Self], pre_fix) -> Self:
        subclass = cls._registry[pre_fix]
        obj = object.__new__(subclass)
        return obj

    def positiveNumberInRange(self, upper_limit) -> float:
        return random.uniform(0, upper_limit)

    def negativeNumberInRange(self, lower_limit):
        return -1* random.uniform(0, -1*lower_limit)

    def digit(self, available_digits = None):
        pass

    def digitNumber(self, no_of_digits, available_digits = None):
        pass


