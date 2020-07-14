import unittest
import my_word
import cloud

sanitycheck = my_word.sanitycheck
polishWord = my_word.polishWord
makeCloudtext = cloud.makeCloudtext

class TestSum(unittest.TestCase):

    def test_wordReplace(self):
        self.assertEqual(polishWord("terror", "fear"), "fear", "Should be fear")

        # now test polish word with different sets of words 

    def test_makeCloudtext(self):
        self.assertEqual(makeCloudtext(["fear", "love"], [1, 4]), ["<h2>love</h2>"], "Should be equal")    

    #test for replacing words in a sectence based on one target word
    #test with target and key sentences
    #test with syno cousins, i.e. not direct synonyms but share over 70% 


    #quantification tests
    #parser tests, .txt file with hello world, word count, other data,
    #test overlap, "fear", "fear" = 1, how many overlaps?
    #word count (should return key: 1 target: 1 )
    #overlap percentage (100%)


    #display histogram of job posting words 

    # make wordcloud <tag>word </tag>, tag based on frequency, output to .html


if __name__ == '__main__':
    unittest.main()



#


