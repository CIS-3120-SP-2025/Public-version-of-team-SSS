import unittest
from src.findaverage import findaverage


#creating the unittest class for findaverage
class Test_findaverage(unittest.TestCase):


    #test to make sure that the find average function works with,
    #since the output can be a float depending on the input I am using round to ensure everything is consistent
    #the 6 in each self.assrtEqual statement is telling the program how many places to round the result to (6 decimal places)
    def test_findaverage(self):
        #using self.assertEqual to make sure the actual value is equal to the expected value
        self.assertEqual(round(findaverage(1, 2, 3), 6), 2.0)    #test to ensure findavreage gets the output 2
        self.assertEqual(round(findaverage(12, 12, 12), 6), 12.0)  #test findavreage gets the correct output when 3 of the same intergers are entered 
        self.assertEqual(round(findaverage(2, 6, 4), 6), 4) #testing find avreage with an unordered pair of numbers ex 2,6,4 instead of 2,3,4

    #testing fundavreage function when negatives are entered
    #using self.assertEqual to make sure the actual value is equal to the expected value
    def test_findaverage_negatives(self):
        self.assertEqual(round(findaverage(-5, 6, -8), 6), -2.333333) #testing findaverage works when there are two negatives and you get continous answer
        self.assertEqual(round(findaverage(-5, -10, -15), 6), -10.0) #testing findaverage with all negative inputs 

if __name__ == '__main__':
    unittest.main()    #allows all test cases from the class Test_findaverage to run 
