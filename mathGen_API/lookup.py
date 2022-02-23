from numberGen import RangedIntegerNumberGenerator
from Stratergy_Pattern_Test import AdditionQuestionType1

DIFFICULTY_LOOKUP = { 
    1: RangedIntegerNumberGenerator(lower_limit=1, upper_limit=25), # 1 to 25
    2: RangedIntegerNumberGenerator(lower_limit=25, upper_limit=100), # 25 to 100
    3: RangedIntegerNumberGenerator(lower_limit=100, upper_limit=1000) # 100 to 1000
    }

GENERATION_LOOKUP = {
    ("addition", "type1"): AdditionQuestionType1,
    ("addition", 1): AdditionQuestionType1
    
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