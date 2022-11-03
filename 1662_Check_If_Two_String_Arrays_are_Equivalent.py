"""
1662. Check If Two String Arrays are Equivalent.

Given two string arrays word1 and word2, return true if
the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements
concatenated in order forms the string.
"""
from typing import List


class Solution:
    """Check If Two String Arrays are Equivalent."""

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """Check If Two String Arrays are Equivalent."""
        w1 = ""
        w2 = ""
        for i in word1:
            w1 += i
        for j in word2:
            w2 += j
        return w1 == w2


def main():
    """Solution."""
    solution = Solution()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    answer = solution.arrayStringsAreEqual(word1, word2)
    print(answer)


if __name__ == "__main__":
    main()
