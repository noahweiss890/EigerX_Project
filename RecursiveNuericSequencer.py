import unittest
from unittest.mock import patch

# Description: This function takes a sequence of numbers and returns the biggest number and the number of times it occurs
def recursice_numeric_sequencer(n, max_num=float("-inf"), max_count=0):
    """
    n: a number
    max_num: the biggest number in the sequence up until this point
    max_count: the number of times the biggest number has occurred in the sequence up until this point
    return: the biggest number and the number of times it occurs in the sequence
    """
    if n == 0: # base case, we have reached the end of the sequence and can return the biggest number and the number of times it occurred
        return (max_num, max_count)
    next_int = int(input())
    if n > max_num: # if the current number is bigger than the biggest number we have seen so far, update the biggest number and reset the number of times it has occurred
        return recursice_numeric_sequencer(next_int, n, 1)
    elif n == max_num: # if the current number is the same as the biggest number we have seen so far, increment the number of times it has occurred
        return recursice_numeric_sequencer(next_int, max_num, max_count + 1)
    else: # if the current number is smaller than the biggest number we have seen so far, do nothing
        return recursice_numeric_sequencer(next_int, max_num, max_count)
    

# tests

class MyTests(unittest.TestCase):
    @patch('builtins.input', side_effect=[5, 42, -376, 5, 19, 5, 3, 42, 2, 0])
    def test_func_given(self, mock_input):
        self.assertEqual(recursice_numeric_sequencer(1), (42, 2))

    def test_func_empty(self):
        self.assertEqual(recursice_numeric_sequencer(0), (float("-inf"), 0))

    @patch('builtins.input', side_effect=[-5, -42, -376, -5, -19, -5, -34, -42, -23, 0])
    def test_func_negitives(self, mock_input):
        self.assertEqual(recursice_numeric_sequencer(-10), (-5, 3))


if __name__ == '__main__':
    unittest.main()