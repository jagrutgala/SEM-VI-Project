# question_strategies/test_all_question_types.py
# In-built imports

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(dirname(abspath(__file__))))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from question_strategies import addition, subtraction, multiplication, division, lcm_hcf, quadratic, linear2var
from number_gen import integer_number, floating_number

add_question = addition.AdditionQuestionType1(integer_number.RangedIntegerNumberGenerator(25, 30), 5)
print(add_question.generate_question())

quad_question = quadratic.QuadraticQuestionType1(integer_number.RangedIntegerNumberGenerator(10, 25))
print(quad_question.generate_question())
