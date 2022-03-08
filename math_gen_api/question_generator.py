# math_gen_api/question_generator.py
# In-built imports
from typing import Any, Optional, TypeVar, Union, Type

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
from math_gen_api.question_strategies import missing
package_path = dirname(abspath(__file__))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from number_gen import integer_number
from question_strategies import question, addition, subtraction, multiplication, division, lcm, hcf, quadratic, linear2var, missing

COMBINE_LOOKUP:dict[str, dict[int, Type[Any]]] = {
    "addition": addition.TYPE_LOOKUP,
    "subtraction": subtraction.TYPE_LOOKUP,
    "multiplication": multiplication.TYPE_LOOKUP,
    "division": division.TYPE_LOOKUP,
    "lcm": lcm.TYPE_LOOKUP,
    "hcf": hcf.TYPE_LOOKUP,
    "quadratic": quadratic.TYPE_LOOKUP,
    "linear2var": linear2var.TYPE_LOOKUP,
    "missing": missing.TYPE_LOOKUP
}


def Question_Generator(q_topic:str, q_type:int, ll:Optional[int], ul:Optional[int], args):
    question_generator_cls = COMBINE_LOOKUP.get(q_topic, {}).get(q_type, None)
    if question_generator_cls == None: return None
    if args == None:
        question_generator = question_generator_cls(integer_number.RangedIntegerNumberGenerator(ll, ul))
    else:
        question_generator = question_generator_cls(integer_number.RangedIntegerNumberGenerator(ll, ul), **args)
    return question_generator

