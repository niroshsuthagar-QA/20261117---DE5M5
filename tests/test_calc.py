import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        # ARRANGE - Create and arrange your test data
        self.calc = Calculator(8,2)
        self.calc2 = Calculator(9,0)

    def test_sum(self):
        self.assertEqual(self.calc.get_sum(), 10, "The sum is wrong")

    def tearDown(self):
        #Typically where you destroy assets you no longer need - Optional
        pass
        


if __name__ == "__main__":
    unittest.main()
