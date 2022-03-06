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
    
    @abstractmethod
    def numbers(self, num_of_nums, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False):
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

    def numbers(self, num_of_nums, is_negative: Optional[bool]=False, is_zero: Optional[bool]=False):
        num_list = []
        for _ in range(num_of_nums):
            num_list.append(self.number(is_negative, is_zero))
        return num_list


class RangedFloatingNumberGenerator(NumberGenerator):
    def __init__(self, lower_limit=1, upper_limit=1000) -> None:
        super().__init__(lower_limit, upper_limit)
        # self.lower_limit = lower_limit
        # self.upper_limit = upper_limit

    def number(self, round_digit:Optional[int]=2, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False):
        if is_zero: return 0
        num = round(random.uniform(self.lower_limit, self.upper_limit), round_digit)
        if is_negative: num *= -1
        return num

    def numbers(self, num_of_nums, round_digit:Optional[int]=2, is_negative: Optional[bool]=False, is_zero: Optional[bool]=False):
        num_list = []
        for _ in range(num_of_nums):
            num_list.append(self.number(round_digit, is_negative, is_zero))
        return num_list
