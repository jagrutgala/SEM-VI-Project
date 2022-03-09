# In-built imports
import sys
from os.path import dirname, abspath
from abc import ABC, abstractmethod
from typing import Optional, TypeVar

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
_package_path = dirname(dirname(abspath(__file__)))
if(_package_path not in sys.path): sys.path.insert(0, _package_path)

# Relative imports


numberType = TypeVar("numberType", int, float)

class NumberGenerator(ABC):
    """Generic Abstract Class for Number Generator

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def number(self, is_negative:Optional[bool]=False, is_zero:Optional[bool]=False):
        ...

class RangedNumberGenerator(NumberGenerator, ABC):
    """Abstract class for Ranged Numbercler Generatoration
    __init__ takes 2 arguments lower_limit and upper_limit
    lower_limit and upper_limit are of type int or float

    Args:
        ABC (_type_): abstract base class
    """
    def __init__(self, lower_limit:numberType, upper_limit:numberType) -> None:
        if lower_limit > upper_limit: raise Exception("Lower Limit should be smaller than Upper Limit")
        self.__lower_limit = lower_limit
        self.__upper_limit = upper_limit

    @property
    def lower_limit(self):
        return self.__lower_limit

    @lower_limit.setter
    def lower_limit(self, ll):
        if ll > self.upper_limit: raise Exception("Lower Limit should be smaller than Upper Limit")
        self.__lower_limit = ll

    @property
    def upper_limit(self):
        return self.__upper_limit

    @upper_limit.setter
    def upper_limit(self, ul):
        if ul < self.lower_limit: raise Exception("Upper Limit should be larger than Lower Limit")
        self.__upper_limit = ul

    @abstractmethod
    def number(self):
        ...
