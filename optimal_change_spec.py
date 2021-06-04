# import unittest
# from optimal_change import optimal_change



class OptimalChangeTestCase(unittest.TestCase):
    

    def test_output(self):
        print("Yes")
        # self.assertEqual(to_roman(1), 'I')
        # self.assertEqual(to_roman(3), 'III')
        # self.assertEqual(to_roman(4), 'IV')
        # self.assertEqual(to_roman(944), 'CMXLIV')
        # self.assertEqual(to_roman(150), 'CL')
        # self.assertEqual(to_roman(2400), 'MMCD')
    
    # def test_str(self):
        # self.assertNotEqual(to_roman(1), str)

        # output returns  a string type


    # def test_returns_modern_numerals(self):
        # self.assertNotEqual(to_roman(4), 'IIII')



# optimal_change(62.13, 100)
# > "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

# optimal_change(31.51, 50)
# > "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."

if __name__ == '__main__':
    unittest.main() 