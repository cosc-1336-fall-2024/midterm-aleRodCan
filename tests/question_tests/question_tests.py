#write function tests here, don't add input('') statements here!
import unittest

from src.question_b import test_config_b
from src.question_c import test_config_c
from src.question_c import test_config_d
#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_question_b_config(self):
        self.assertEqual(True, test_config_b())

    def test_question_c_config(self):
        self.assertEqual(True, test_config_c())
    
    def test_question_d_config(self): # type: ignore
        self.assertEqual(True, test_config_d())

