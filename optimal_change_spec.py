import unittest
from optimal_change import optimal_change



class OptimalChangeTestCase(unittest.TestCase):
    
    # Testing is output is a string
    def test_str(self):
        self.assertEqual(optimal_change(62.12, 100), str)
    
    
    # Testing for correct output
    def test_output(self): 
        self.assertEqual(optimal_change(62.12, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
    
    # Testing for an output value
    def test_output(self): 
        self.assertNotEqual(optimal_change(62.12, 100), None)





# optimal_change(62.13, 100)
# > "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

# optimal_change(31.51, 50)
# > "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

if __name__ == '__main__':
    unittest.main() 