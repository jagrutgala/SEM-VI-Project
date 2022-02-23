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
    def number(self):
        pass
    
    @abstractmethod
    def multipleNumber(self, num):
        pass

    @abstractmethod
    def factorNumber(self, num):
        pass

    @abstractmethod
    def rangeNumber(self, lower_limit, upper_limit):
        pass
    
    # @abstractmethod
    # def Number(self):
    #     pass

    @abstractmethod
    def digitNumber(self, no_of_digits: int, available_digits: list= None):
        pass 

    def __joinDigits(self, digits: list):
        return int("".join(digits))

    def unitNumber(self, available_digits: list= None):
        return self.digitNumber(1, available_digits)

    def tensNumber(self, available_digits: list= None):
        return self.digitNumber(2, available_digits)

    def thousandsNumber(self, available_digits: list= None):
        return self.digitNumber(3, available_digits)

##############################
# Number Generator Types
# - Positive Number Generator
# - Negative Number Generator
# - Integer Number Generator
# - Positive Integer Number Generator
# - Integer Number Generator
# - Floating Number Generator
##############################
class PositiveNumberGenerator(NumberGenerator):
    def number(self) -> int:
        return random.randint(0, 1000)

    def multipleNumber(self, num, limit= 1000):
        return num* self.rangeNumber(upper_limit=limit)

    def factorNumber(self, num):
        pass

    def rangeNumber(self, lower_limit=0, upper_limit=1000) -> int:
        return random.randint(0, upper_limit)

    def digitNumber(self, no_of_digits: int, available_digits: list):
        pass 


class IntegerNumberGenerator(NumberGenerator):
    def number(self):
        pass

    def multipleNumber(self, num):
        pass

    def factorNumber(self, num):
        pass

    def rangeNumber(self, lower_limit, upper_limit):
        pass

    def digitNumber(self, no_of_digits: int, available_digits: list):
        pass 

class FloatingNumberGenerator(NumberGenerator):
    def number(self):
        pass

    def multipleNumber(self, num):
        pass

    def factorNumber(self, num):
        pass

    def rangeNumber(self, lower_limit, upper_limit):
        pass

    def digitNumber(self, no_of_digits: int, available_digits: list):
        pass

    def regularFloat(self):
        pass

class NumberGenerator_Factory:
    pass




class SmallNumberGenerator:
    def __init__(self) -> None:
        self.lower_limit = 1
        self.upper_limit = 25

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)

class MediumNumberGenerator:
    def __init__(self) -> None:
        self.lower_limit = 25
        self.upper_limit = 100

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)

class LargeNumberGenerator:
    def __init__(self) -> None:
        self.lower_limit = 100
        self.upper_limit = 999

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)