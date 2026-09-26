import unittest
from unittest import TestCase
from pipelineDuration import calculate_duration


class Test(TestCase):
    def test_first_argument_type_is_invalid(self):
        
        self.assertRaises(TypeError,calculate_duration,'1',2)

    def test_second_argument_type_is_invalid(self):
        
        self.assertRaises(TypeError,calculate_duration,1,'2')

    def test_both_args_same_value_zero_returned(self):
        res = calculate_duration(1,1)
        self.assertEqual(res,0)

    def test_start_bigger_than_end(self):
        self.assertRaises(ValueError,calculate_duration,14,1)

    def test_succesful_case(self):
        z = calculate_duration(10,15)
        self.assertEqual(5,z)
if __name__ =='__main__':
    unittest.main()

