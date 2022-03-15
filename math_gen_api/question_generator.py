# math_gen_api/question_generator.py
# In-built imports
from typing import Any, Optional, Type

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(abspath(__file__))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from number_gen import integer_number
from question_strategies import addition, subtraction, multiplication, division
from question_strategies import lcm, hcf, quadratic, linear2var, factors, square, factorial
from question_strategies import permutation, combination , fibonacci, profit, loss

COMBINE_LOOKUP:dict[str, dict[str, Type[Any]]] = {
    "addition": addition.TYPE_LOOKUP,
    "subtraction": subtraction.TYPE_LOOKUP,
    "multiplication": multiplication.TYPE_LOOKUP,
    "division": division.TYPE_LOOKUP,
    "lcm": lcm.TYPE_LOOKUP,
    "hcf": hcf.TYPE_LOOKUP,
    "quadratic": quadratic.TYPE_LOOKUP,
    "linear2var": linear2var.TYPE_LOOKUP,
    "factors": factors.TYPE_LOOKUP,
    "square": square.TYPE_LOOKUP,
    "factorial": factorial.TYPE_LOOKUP,
    "permutation": permutation.TYPE_LOOKUP,
    "combination": combination.TYPE_LOOKUP,
    "fibonacci": fibonacci.TYPE_LOOKUP,
    "profit": profit.TYPE_LOOKUP,
    "loss": loss.TYPE_LOOKUP
}


def Question_Generator(q_topic:str, q_type:str, ll:Optional[int], ul:Optional[int]):
    question_generator_cls = COMBINE_LOOKUP.get(q_topic, {}).get(q_type, None)
    if question_generator_cls == None: return None
    question_generator = question_generator_cls(integer_number.RangedIntegerNumberGenerator(ll, ul))
    return question_generator

