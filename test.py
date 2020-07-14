import unittest
import my_word

sanitycheck = my_word.sanitycheck
polishWord = my_word.polishWord

class TestSum(unittest.TestCase):

    def test_wordReplace(self):
        self.assertEqual(polishWord("terror", "fear"), "fear", "Should be fear")

if __name__ == '__main__':
    unittest.main()



#


