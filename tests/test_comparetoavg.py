import unittest
import sys  #imported in order to redirect where certain outputs go 
from io import StringIO #imported in order to capture the printed output 
from src.comparetoavg import comparetoavg

class Test_comparetoavg(unittest.TestCase):

    def test_comparetoavg_none_equal(self):
        captured_output = StringIO() #Using stringIO to capture the printed output 
        sys.stdout = captured_output #redirecting the printed output to the captured_output 

        comparetoavg(1, 2, 3, 2.0)

        sys.stdout = sys.__stdout__   #redirecting the captured output to the terminal 
        output = captured_output.getvalue().strip().split('\n')

        expected_output = [
            "1 is less than the average",
            "2 is equal to the average",
            "3 is greater than the average",
            "Number of values equal to the average: 1"
        ]
        self.assertEqual(output, expected_output)  #using self.assertEqual to make sure captured output is = to expected output

        #Test case where only one value equals the average
    def test_comparetoavg_one_equal(self): 
        captured_output = StringIO()
        sys.stdout = captured_output  #redirecting the printed output to the captured_output 

        comparetoavg(4, 6, 8, 6.0)

        sys.stdout = sys.__stdout__  #redirecting the captured output to the terminal 
        output = captured_output.getvalue().strip().split('\n')

        expected_output = [
            "4 is less than the average",
            "6 is equal to the average",
            "8 is greater than the average",
            "Number of values equal to the average: 1"
        ]
        self.assertEqual(output, expected_output)  #using self.assertEqual to make sure captured output is = to expected output

        
        #Test case where all values equal zero
        #It is not possible for two values to equal the average
    def test_comparetoavg_all_equal(self):
        captured_output = StringIO()
        sys.stdout = captured_output  #redirecting the printed output to the captured_output 

        comparetoavg(5, 5, 5, 5.0)

        sys.stdout = sys.__stdout__  #redirecting the captured output to the terminal 
        output = captured_output.getvalue().strip().split('\n')

        expected_output = [
            "5 is equal to the average",
            "5 is equal to the average",
            "5 is equal to the average",
            "Number of values equal to the average: 3"
        ]
        self.assertEqual(output, expected_output) #using self.assertEqual to make sure captured output is = to expected output

        #Test case for negative values
    def test_comparetoavg_negative_values(self):
        captured_output = StringIO()
        sys.stdout = captured_output  #redirecting the printed output to the captured_output 

        comparetoavg(-3, -6, -9, -6.0)

        sys.stdout = sys.__stdout__   #redirecting the captured output to the terminal 
        output = captured_output.getvalue().strip().split('\n')

        expected_output = [
            "-3 is greater than the average",
            "-6 is equal to the average",
            "-9 is less than the average",
            "Number of values equal to the average: 1"
        ]
        self.assertEqual(output, expected_output)  #using self.assertEqual to make sure captured output is = to expected output

if __name__ == '__main__':
    unittest.main() #allows all test cases to run


   
