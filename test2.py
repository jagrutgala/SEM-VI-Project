# Characteristics of a Question
# string, type, difficulty, ans, fake_options?
# Characteristics of a Question Generator
# format string, *numbergenerator_objs, difficulty
# format string, number_of_numbers_needed, types_of_numbers_needed, position_of_numbers_needed

DIFFICULTY_LOOKUP = { 
    1: SmallNumberGenerator, # 1 to 25
    2: MediumNumberGenerator, # 25 to 100
    3: LargeNumberGenerator # 100 to 1000
    }

GENERATION_LOOKUP = {
    ("addition", "type1"): AdditionQuestionType1,
    ("addition", "type2"): AdditionQuestionType2,
    ("addition", "type3"): AdditionQuestionType3,
    
    ("addition", "type1"): AdditionQuestionType1,
    ("addition", "type2"): AdditionQuestionType2,
    ("addition", "type3"): AdditionQuestionType3,
    ("addition", "type1"): AdditionQuestionType1,
    ("addition", "type2"): AdditionQuestionType2,
    ("addition", "type3"): AdditionQuestionType3,
    ("addition", "type1"): AdditionQuestionType1,
    ("addition", "type2"): AdditionQuestionType2,
    ("addition", "type3"): AdditionQuestionType3,
    ("addition", "type1"): AdditionQuestionType1,
    ("addition", "type2"): AdditionQuestionType2,
    ("addition", "type3"): AdditionQuestionType3,
}