from abc import ABC, abstractmethod
import random
print(f"### Welcome to Math Question Generator ###")

# 1. Basic Operations(+-*/)
# 2. LCM and HCF     3. Percentage
# 4. Linear Equations
# 5. Quadratic Equations

class Question:
    def __init__(self, q_string, answer) -> None:
        self.__q_string= q_string
        self.__answer= answer
    
    def __repr__(self) -> str:
        return self.q_string
    
    @property
    def q_string(self):
        return self.__q_string
    
    @property
    def answer(self):
        return self.__answer

class QuestionGenerator(ABC):
    easy= "EASY"
    medium= "MEDIUM"
    hard= "HARD"

    def __init__(self, difficulty) -> None:
        super().__init__()
        self.difficulty= difficulty

    def generateQuestion(self) -> Question:
        if(self.difficulty == self.hard):
            question= self.generateHardQuestion()
        elif(self.difficulty == self.medium):
            question= self.generateMediumQuestion()
        else:
            question= self.generateEasyQuestion()
        return question

    @abstractmethod
    def generateEasyQuestion(self) -> Question:
        pass
    @abstractmethod
    def generateMediumQuestion(self) -> Question:
        pass
    @abstractmethod
    def generateHardQuestion(self) -> Question:
        pass
    @abstractmethod
    def getAnswer(self, **kwargs):
        pass

class BasicOperations(QuestionGenerator):
    operations= ['+', '-', '/', '*', "^"]

    def generateEasyQuestion(self):
        return Question("Easy Question", 0)

    def generateMediumQuestion(self):
        return Question("Easy Question", 0)

    def generateHardQuestion(self):
        return Question("Easy Question", 0)

    def getAnswer(self, num1, num2, operation):
        if(operation == "+"):
            return num1+ num2
        elif(operation == "-"):
            return num1- num2
        elif(operation == "*"):
            return num1* num2
        elif(operation == "/"):
            return num1/ num2
        elif(operation == "^"):
            return num1** num2



bo_qgen= BasicOperations(BasicOperations.easy)
print(bo_qgen.generateQuestion())


# def basicOperation(no_of_questions):
#     question_list= []
#     while len(question_list) < no_of_questions:
#         # print(f"length of question list: {len(question_list)}")
#         try:
#             question= BasicOperationQuestion.generateQuestion(EasyDifficulty)
#             question_list.append(question)
#         except ZeroDivisionError: pass
#     return question_list

# for i in basicOperation(5):
#     print(i)



        #     op= random.choice(self.operations)
        # if(op == "+" or op == "-"):
        #     num1, num2= round(random.random()* 10)
        #     if(random.random()>= 0.7):
        #         num1*= -1
        #     num2= int(random.random()* 10)
        # elif(op == "*", op == "/"):
        #     num1, num2= 0
        #     while num1== 0 or num2 == 0:
        #         num1= random.randint(2, 100)
        #         num2= random.randint(2, 100)
        #     question= BasicOperationQuestion(num1, num2, op)
        # elif(op == "/"):
        #     num2= 0
        #     while num2== 0:
        #         num2= random.randint(2, 100)
        #     question= BasicOperationQuestion(random.random(2, 1000), num2, op)
        # elif(op == "^"):
        #     question= BasicOperationQuestion(random.randint(2, 25), random.randint(2, 10), op)
        # return question