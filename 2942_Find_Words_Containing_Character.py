import unittest
from typing import List


class Solution:
    """2942. Find Words Containing Character."""
        
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]
    

class TestSolution(unittest.TestCase):

    def test_findWordsContaining(self):
        sol = Solution()
        
        self.assertEqual(sol.findWordsContaining(words = ["leet","code"], x = "e"), [0,1])
        self.assertEqual(sol.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "a"), [0,2])
        self.assertEqual(sol.findWordsContaining(words = ["abc","bcd","aaaa","cbc"], x = "z"), [])


if __name__ == "__main__":
    unittest.main()
