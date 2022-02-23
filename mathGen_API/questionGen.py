##############################
# questionGen.py - Docs
"""
"""
##############################
# Type Hinting Reamaining
import lookup

class QuestionGeneration:
    @classmethod
    def generationObject(cls, gen_type):
        gen_cls = lookup.GENERATION_LOOKUP.get(gen_type, None)
        if gen_cls is None: return None
        return gen_cls()

    @classmethod
    def numberObject(cls, num_type:int):
        num_cls = lookup.DIFFICULTY_LOOKUP.get(num_type, None)
        if num_cls is None: return None
        return num_cls

    def create_question(self, gen_type, difficulty:int):
        gen_obj = self.generationObject(gen_type)
        if gen_obj is None: raise Exception("Bad Topic and Type")
        num_obj = self.numberObject(difficulty)
        if num_obj is None: raise Exception("Bad Difficulty")
        question = gen_obj.create_question(num_obj)
        return question

if __name__ == "__main__":
    print("Hello World! :)")
    # print(f"Available stratergies: {', '.join(lookup.GENERATION_LOOKUP.keys())}\n")
    # question_topic, question_type = input("What topic and stratergy do you want to use ? eg. quadratic type2\n").split()
    print("Done ✅")

