# In-built imports
import unittest

# Third-party imports

# Sys-Paths for Relative Imports
import sys
from os.path import dirname, abspath
package_path = dirname(dirname(dirname(abspath(__file__))))
if(package_path not in sys.path): sys.path.insert(0, package_path)

# Relative imports
from number_gen import integer_number

class TestRangedIntegerNumberGenerator(unittest.TestCase):
    def test_generator_range(self):
        ...
    def test_number(self):
        ...


if __name__ == "__main__":
    # Code Here
    unittest.main()
