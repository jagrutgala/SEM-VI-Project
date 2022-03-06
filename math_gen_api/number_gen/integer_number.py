# In-built imports
import random
from typing import Callable, Optional

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(abspath(__file__)))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from number_gen import number_generator

def intRanged(num_func:Callable):
    """Decorator for number method in IntegerNumberGenerators
    checks for 'is_negative' and 'is_zero' keyword arguments
    if is_negative is True it will return negative of generated number
    if is_zero is True it will return 0

    Args:
        num_func (Callable): _description_
    """
    def wrapper(*args, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False, ):
        if is_zero: return 0
        num = num_func(*args)
        if is_negative: num *= -1
        return num
    return wrapper

class RangedIntegerNumberGenerator(number_generator.RangedNumberGenerator):
    """Ranged Ineger Number Generator
    Generates numbers between a specified lower limit and upper limit.
    lower and upper limits are passed as arguments to the __init__ method.
    
    Args:
        number_generator (_type_): module that holds base classes for number generators
    """
    def __init__(self, lower_limit:Optional[int]=None, upper_limit:Optional[int]=None) -> None:
        if not lower_limit: lower_limit = 1
        if not upper_limit: upper_limit = 1000
        super().__init__(lower_limit, upper_limit)
    
    @intRanged
    def number(self):
        num = random.randint(int(self.lower_limit), int(self.upper_limit))
        return num

if __name__ == "__main__":
    def main():
        # Code Here
        ...
    main()