# INSTRUCTIONS
# 1. Install Python 3.7.6 in MAC operative system.
# 2. Right click on readText.py file, open with,  and then select python launcher.
# 3. Verify the console which opens after launching python.

#UNIT TESTS

import unittest
file_path = "inputText.txt"
from RevertedText import fun

class TestLongestWord(unittest.TestCase):
    
    def setUp(self):
        self.word = "Abcd"
        self.reversed_word = "dcbA"
        self.negative_word = "abc"
        self.negative_reversed_word = "dcbAe"
    
    def tearDown(self):
        self.word = None
        self.reversed_word = None
    
    def test_longest_string(self):
        self.assertEqual(fun(file_path)[0], self.word, "Should be Abcd")
    
    def test_reverted_longest_string(self):
        self.assertEqual(fun(file_path)[1], self.reversed_word, "Should be dcbA")

    def test_longest_negative_string(self):
        self.assertEqual(fun(file_path)[0], self.negative_word, "Should be be Abcd")
    
    def test_reverted_longest_negative_string(self):
        self.assertEqual(fun(file_path)[1], self.negative_reversed_word, "Should be dcbA")

if __name__ == '__main__':
    unittest.main()



