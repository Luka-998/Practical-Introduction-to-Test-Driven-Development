from tested_functions import adder,divider
import unittest
import numpy as np
import inspect
forty = [1]*40
print(forty)


class Test(unittest.TestCase):
    def test_adds_two_integers_correctly(self):
        self.assertEqual(adder(3,5),8)

    def test_adds_negative_numbers_correctly(self):
        self.assertEqual(adder(-3,-2),-5)

    def test_adds_numbers_to_zero_correctly(self):
        self.assertEqual(adder(0,5),5)

    def test_adds_three_integers_correctly(self):
        self.assertEqual(adder(3,3,3),9)

    def test_adds_forty_integers_correctly(self):
        self.assertEqual(adder(*forty),40)

    def test_raises_an_exception_when_given_one_argument(self):
        with self.assertRaises(ValueError):
            adder(1) 
              
            
    def test_raises_an_exception_on_string_argument(self):
        self.assertRaises(TypeError,adder,'123')

    def test_raises_an_exception_when_too_many_arguments(self):
        self.assertRaises(TypeError,divider,1,2,3) 

if __name__ == "__main__":
    unittest.main(verbosity=2)

    inspect.signature(self.assertRaises())