import unittest
from optimal_change import optimal_change

class OptimalChangeTestCase(unittest.TestCase):
    
    # Testing is output is a string   
    def test_returns_a_str(self):
        """When you call optimal_change(), you should get a str back"""
        self.assertEqual(type(optimal_change(62.13, 100)), str)
     
    # Testing for correct output
    def test_output(self): 
        self.assertEqual(optimal_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
        self.assertEqual(optimal_change(49, 50), "The optimal change for an item that costs $49 with an amount paid of $50 is 1 $1 bill.")
        self.assertEqual(optimal_change(48.50, 50), "The optimal change for an item that costs $48.5 with an amount paid of $50 is 1 $1 bill, and 2 quarters.")

    # testing for transaction 
    def test_for_transaction(self): 
        self.assertEqual(optimal_change(0, 0), "No transaction")
    
    # Item cost greater than amount paid returns an error
    def test_transaction_error(self): 
        self.assertEqual(optimal_change(100, 62.13), "Item too expensive!")

if __name__ == '__main__':
    unittest.main()