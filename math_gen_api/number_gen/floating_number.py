# In-built imports
import random
from typing import Optional, Callable

# Third-party imports

# Relative imports
import number_generator

def floatRanged(num_func:Callable):
    """Decorator for number method in FloatingNumberGenerators
    checks for 'round_count', 'is_negative' and 'is_zero' keyword arguments
    if round_count is >= 0 it will round the generated number to round_count digits else it will not round the generated number
    if is_negative is True it will return negative of generated number
    if is_zero is True it will return 0

    Args:
        num_func (Callable): _description_
    """
    def wrapper(*args, round_count:Optional[int]=None, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False):
        if round_count == None: round_count= -1
        if is_zero: return 0
        num = num_func(*args)
        if round_count >= 0:
            num = round(num, round_count)
        if is_negative: num *= -1
        return num
    return wrapper

class RangedFloatingNumberGenerator(number_generator.RangedNumberGenerator):
    """Ranged Floating Number Generator
    Generates numbers between a specified lower limit and upper limit.
    lower and upper limits are passed as arguments to the __init__ method.

    Args:
        number_generator (_type_): module that holds base classes for number generators
    """
    def __init__(self, lower_limit:Optional[float]=1.0, upper_limit:Optional[float]=1000.0) -> None:
        if not lower_limit: lower_limit = 1.0
        if not upper_limit: upper_limit = 1000.0
        super().__init__(lower_limit, upper_limit)

    @floatRanged
    def number(self):
        num = random.uniform(float(self.lower_limit), float(self.upper_limit))
        return num
