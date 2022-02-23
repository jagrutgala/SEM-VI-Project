##############################
# numberGen.py - Docs
"""
"""
##############################
# Type Hinting Reamaining

import random
from abc import ABC, abstractmethod
from typing import Optional

class NumberGenerator(ABC):
    def __init__(self, lower_limit, upper_limit) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    @abstractmethod
    def number(self, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False):
        ...

class RangedIntegerNumberGenerator(NumberGenerator):
    def __init__(self, lower_limit=1, upper_limit=1000) -> None:
        super().__init__(lower_limit, upper_limit)
        # self.lower_limit = lower_limit
        # self.upper_limit = upper_limit

    def number(self, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False):
        if is_zero: return 0
        num = random.randint(self.lower_limit, self.upper_limit)
        if is_negative: num *= -1
        return num

class RangedFloatingNumberGenerator(NumberGenerator):
    def __init__(self, lower_limit=1, upper_limit=1000) -> None:
        super().__init__(lower_limit, upper_limit)
        # self.lower_limit = lower_limit
        # self.upper_limit = upper_limit

    def number(self, decimal:int, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False):
        ... # Floating Number Generation Implementation


"""class SmallNumberGenerator:
    def __init__(self, lower_limit=1, upper_limit=25) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)

class MediumNumberGenerator:
    def __init__(self, lower_limit=25, upper_limit=100) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)

class LargeNumberGenerator:
    def __init__(self, lower_limit=100, upper_limit=1000) -> None:
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def number(self):
        return random.randint(self.lower_limit, self.upper_limit)"""


