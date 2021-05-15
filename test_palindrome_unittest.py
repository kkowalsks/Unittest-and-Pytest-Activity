import unittest
import palindrome

class testCasePalindrome(unittest.TestCase):
    def test_backwards(self):
        self.assertEqual(palindrome.backwards("kayak"), True)
        self.assertEqual(palindrome.backwards("CS 362"), True)
        self.assertEqual(palindrome.backwards("taco cat"), False)
        self.assertEqual(palindrome.backwards("racecar"), False)



if __name__ == '__main__':
    unittest.main()

#Ctrl+Shift+P
