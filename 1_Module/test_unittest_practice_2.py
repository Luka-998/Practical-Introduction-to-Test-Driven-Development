import unittest
from tested_functions import divider
import inspect

class Test(unittest.TestCase):
    def test_non_integer_results(self):
        self.assertAlmostEqual(divider(7,2),3.5)

    def test_too_many_arguments(self):
        self.assertRaises(ValueError,divider,*(1,2,3))

    def test_raise_error_if_non_int_args(self):
        self.assertRaises(TypeError,divider,*('123',1))

    def test_raise_erorr_0_div(self):
        self.assertRaises(ValueError,divider,1,0)
    def test_large_division(self):
        self.assertEqual(divider(4*10000,4*1000),10)

    def test_succesive_divisions(self):
        self.assertEqual(divider(divider(divider(16,2),8),1),1)


if __name__=='__main__':
    unittest.main(verbosity=2)
