import unittest
from pipelineRun import PipeObj


class Test(unittest.TestCase):
    def setUp(self):
        self.pip = PipeObj(10,0,13)

    def test_first_argument_type_is_not_valid(self):
        self.assertRaises(TypeError,setattr,PipeObj,'1',0,14)
    def test_second_argument_type_is_not_valid(self):
        self.assertRaises(TypeError,PipeObj,1,'0',15)
    def test_second_argument_is_not_in_valid_range(self):
        self.assertRaises(ValueError,PipeObj,1,5,10)

    def test_third_argument_type_is_not_valid(self):
        self.assertRaises(TypeError,setattr,PipeObj,1,0,'15')

    def test_start_end_adequate_values(self):
        self.assertLess(self.pip.start,self.pip.end)

    def test_equal_start_end_gives_0(self):
        pip = PipeObj(10,1,10)
        self.assertEqual(pip.pipeline_duration(),0)

    def test_status_is_running(self):
        pip = PipeObj(10,0,None)
        self.assertEqual(pip.status,'RUNNING')

    def test_return_value_when_pipe_is_running(self):
        pip = PipeObj(10,0,None)
        self.assertEqual(pip.pipeline_duration(),'Pipeline is still running!')

    def test_status_is_failed(self):
        pip = PipeObj(10,2,15)
        self.assertEqual(pip.status,'FAILED')

    def test_status_is_completed(self):
        pip=PipeObj(10,0,15)
        self.assertEqual(pip.status,'DONE')

    def test_result_is_valid(self):
        self.assertEqual(self.pip.pipeline_duration(),3)
if __name__=='__main__':
    unittest.main()