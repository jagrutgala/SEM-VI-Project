class Question:
    def __init__(self, qstring: str, answer, question_type: str) -> None:
        self.qstring = qstring
        self.answer = answer
        self.type = question_type
    
    def __repr__(self) -> str:
        return f"[Question] {self.qstring} \tAnswer: {self.answer}"

    def toJson(self):
        qson = dict()
        qson["question_string"] = self.qstring
        qson["answer"] = self.answer
        return qson


