# question_strategies/question.py
# In-built imports
import sys
from os.path import dirname, abspath
from abc import ABC, abstractmethod
from typing import Union
# import json, xml

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports

from number_gen import integer_number, floating_number

numGenType = Union[integer_number.RangedIntegerNumberGenerator, floating_number.RangedFloatingNumberGenerator]

class Question:
    """This is a Generic Question class
    """
    def __init__(self, qstring: str, answer, question_type: str) -> None:
        self.qstring = qstring
        self.answer = answer
        self.type = question_type
    
    def __repr__(self) -> str:
        return f"[Question] {self.qstring} \tAnswer: {self.answer}"

    def toDict(self):
        """Returns Dictionary Object of Question

        Returns:
            dict: keys [ question_string, answer, type ]
        """
        q = {
            "question_string": self.qstring,
            "answer": self.answer,
            "type": self.type
        }
        return q

    def toJson(self):
        """Returns JSON Object of Question

        Returns:
            dict: keys [ question_string, answer, type ]
        """
        q = {
            "question_string": self.qstring,
            "answer": self.answer,
            "type": self.type
        }
        # convert to JSON
        return q

    def toXml(self):
        """Returns XML Object of Question

        Returns:
            dict: keys [ question_string, answer, type ]
        """
        q = {
            "question_string": self.qstring,
            "answer": self.answer,
            "type": self.type
        }
        # convert to XML
        return q

class QuestionType(ABC):
    """Abstract class for all QuestionTypes
    If you want to make a new question it must extend this class

    Args:
        ABC (_type_): abstract base class
    """
    @abstractmethod
    def generate_question(self) -> Question:
        ...