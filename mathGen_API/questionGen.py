##############################
# questionGen.py - Docs
"""
"""
##############################
# Type Hinting Reamaining
import lookup, question


class QuestionGenerator:
    @classmethod
    def generatorObject(cls, gen_type, **kwargs):
        gen_cls = lookup.GENERATION_LOOKUP.get(gen_type, None)
        if gen_cls is None: return None
        return gen_cls(**kwargs)

    @classmethod
    def numberObject(cls, num_type:int):
        num_cls = lookup.DIFFICULTY_LOOKUP.get(num_type, None)
        if num_cls is None: return None
        return num_cls

    def create_question(self, gen_type, difficulty:int) -> question.Question:
        gen_obj = self.generatorObject(gen_type)
        if gen_obj is None: raise Exception("Bad Topic and Type")
        num_obj = self.numberObject(difficulty)
        if num_obj is None: raise Exception("Bad Difficulty")
        question = gen_obj.create_question(num_obj)
        return question

class BasicQuestionGenerator(QuestionGenerator):
    def __init__(self) -> None:
        super().__init__()

    def create_question(self, gen_type, difficulty: int) -> question.Question:

        num_obj = self.numberObject(difficulty)
        if num_obj is None: raise Exception("Bad Difficulty")
        return super().create_question(gen_type, difficulty)


if __name__ == "__main__":
    print("Hello World 🔥")
    qg = QuestionGenerator()
    q = qg.create_question(("addition", 1), 1)
    print(f"Q) {q}")
    print("Done ✅")