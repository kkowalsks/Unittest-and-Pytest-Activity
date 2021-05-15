import unittest
import word_count

class testCaseWordCount(unittest.TestCase):
    def test_wordCount(self):
        self.assertEqual(word_count.wordCount("3 Word Sentence"), 3)
        self.assertEqual(word_count.wordCount("OneWordLongSentence"), 1)
        self.assertEqual(word_count.wordCount(""), 0)
        self.assertEqual(word_count.wordCount("This sentence will fail"), 7)



if __name__ == '__main__':
    unittest.main()