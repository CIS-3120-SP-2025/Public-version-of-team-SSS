import unittest  #importing the unittest framework
from io import StringIO  #imported in order to capture the printed output 
import sys  #imported in order to redirect where certain outputs go 
from src.introduction import introduction  #Importing the introduction function from SRC folder for unittest

#creating a class with the unittest framework in order to test Introduction function 
class Introduction_UT(unittest.TestCase):
    def test_introduction(self):
        captured_output = StringIO()  #Using stringIO to capture the printed output 
        sys.stdout = captured_output  #redirecting the printed output to the captured_output 

        introduction()  #calling function being tested 

        sys.stdout = sys.__stdout__  #redirecting the captured output to the terminal 

        #output from the introduction function 
        expected_output = (
            'This program prompts the user to enter 3 integers values.\n'
            'The program then finds the average of these 3 values\n'
            'It then compares them to the average and prints an appropriate message\n'
            'The program operates on a loop. To exit the program: enter 0 0 0'
        )
         #using self.assertEqual to make sure captured output is = to expected output and making sure there is no white space in the captured output
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        


if __name__ == '__main__':
     unittest.main()  #allows all test cases from the class Introudcution_UT to run 
