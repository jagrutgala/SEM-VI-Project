from numberGen import RangedIntegerNumberGenerator
from questionStrategy import *

DIFFICULTY_LOOKUP = { 
    1: RangedIntegerNumberGenerator(lower_limit=1, upper_limit=25), # 1 to 25
    2: RangedIntegerNumberGenerator(lower_limit=25, upper_limit=100), # 25 to 100
    3: RangedIntegerNumberGenerator(lower_limit=100, upper_limit=1000) # 100 to 1000
    }


QUESTION_LOOKUP_KEYS = [
    ("add", 1),
    ("sub", 1), ("sub", 2), ("sub", 3),
    ("mul", 1), ("mul", 2),
    ("div", 1), ("div", 2),
    ("lcm", 1),
    ("hcf", 1),
    ("quadratic", 1),
    ("linear2var", 1)
]



QUESTION_LOOKUP = {
    (str("add"), int(1)): AdditionQuestionType1,
    (str("sub"), int(1)): SubtractionQuestionType1,
    (str("sub"), int(2)): SubtractionQuestionType2,
    (str("sub"), int(3)): SubtractionQuestionType3,
    (str("mul"), int(1)): MultiplicationQuestionType1,
    (str("mul"), int(2)): MultiplicationQuestionType2,
    (str("div"), int(1)): DivisionQuestionType1,
    (str("div"), int(2)): DivisionQuestionType2,
    (str("lcm"), int(1)): LCMQuestionType1,
    (str("hcf"), int(1)): HCFQuestionType1,
    (str("quadratic"), int(1)): QuadraticQuestionType1,
    (str("linear2var"), int(1)): Linear2VarQuestionType1
}