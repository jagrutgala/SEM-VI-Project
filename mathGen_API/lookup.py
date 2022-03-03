from mathGen_API.questionStrategy_attemp1 import AdditionQuestionType2
from numberGen import RangedIntegerNumberGenerator
from questionStrategy_attemp1 import *

DIFFICULTY_LOOKUP = { 
    1: RangedIntegerNumberGenerator(lower_limit=1, upper_limit=25), # 1 to 25
    2: RangedIntegerNumberGenerator(lower_limit=25, upper_limit=100), # 25 to 100
    3: RangedIntegerNumberGenerator(lower_limit=100, upper_limit=1000) # 100 to 1000
    }

GENERATION_LOOKUP = {
    ("addition", 1): AdditionQuestionType1,
    ("addition", 2): AdditionQuestionType2,
    ("addition", 3): AdditionQuestionType2,
    ("addition", 4): AdditionQuestionType2,
    ("subtraction", 1): SubtractionQuestionType1,
    ("subtraction", 2): SubtractionQuestionType2,
    ("subtraction", 3): SubtractionQuestionType3,
    ("subtraction", 4): SubtractionQuestionType4,
    
    # ("addition", "type1"): AdditionQuestionType1,
    # ("addition", "type2"): AdditionQuestionType2,
    # ("addition", "type3"): AdditionQuestionType3,
    # ("addition", "type1"): AdditionQuestionType1,
    # ("addition", "type2"): AdditionQuestionType2,
    # ("addition", "type3"): AdditionQuestionType3,
    # ("addition", "type1"): AdditionQuestionType1,
    # ("addition", "type2"): AdditionQuestionType2,
    # ("addition", "type3"): AdditionQuestionType3,
    # ("addition", "type1"): AdditionQuestionType1,
    # ("addition", "type2"): AdditionQuestionType2,
    # ("addition", "type3"): AdditionQuestionType3,
}