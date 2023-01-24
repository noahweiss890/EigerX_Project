import unittest

# Description: This function will take a number and add all of the digits together recursively
def count_digits(n):
    """
    n: a non-negative integer
    return: the sum of all digits of n
    """
    if n < 10: # base case, check if n is a single digit
        return n
    else: # recursive case, n is not a single digit so we need to add the last digit to the sum of the rest of the digits
        return n % 10 + count_digits(n // 10)
    
# tests

class MyTests(unittest.TestCase):
    def test_func_given(self):
        self.assertEqual(count_digits(2347623), 27)

    def test_func_zero(self):
        self.assertEqual(count_digits(0), 0)

    def test_func_big(self):
        self.assertEqual(count_digits(123456789), 45)

if __name__ == '__main__':
    unittest.main()