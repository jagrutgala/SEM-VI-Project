from abc import ABC, abstractmethod
import random

##############################
# Number Generator Abstract
##############################
class NumberGenerator(ABC):
    """
    Number Generator Function
    - number
    - multipleNumber (n)
    - factorNumber (n)
    - rangeNumber (ll, ul)
    - Number
    - digitNumber (no_of_digits:int, available_digits:list)
    - joinDigits (digits: list)
    """

    @abstractmethod
    def number(self, **kwargs):
        pass

class BasicEasyNumberGen:
    pass

class BasicMediumNumberGen:
    pass

class BasicHardNumberGen:
    pass

class DivisionEasyNumberGen:
    pass

class DivisionMediumNumberGen:
    pass

class DivisionHardNumberGen:
    pass

class QuadraticEasyNumberGen:
    pass

class QuadraticMediumNumberGen:
    pass

class QuadraticHardNumberGen:
    pass

