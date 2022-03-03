class Question:
    def __init__(self, qstring: str, answer, question_type: str) -> None:
        self.qstring = qstring
        self.answer = answer
        self.type = question_type
    
    def __repr__(self) -> str:
        return f"[Question] {self.qstring} \tAnswer: {self.answer}"

if __name__ == "__main__":
    pass
