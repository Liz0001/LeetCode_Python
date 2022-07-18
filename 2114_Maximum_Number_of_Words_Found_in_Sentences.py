"""
2114. Maximum Number of Words Found in Sentences from Leetcode.

A sentence is a list of words that are separated by
a single space with no leading or trailing spaces.

You are given an array of strings sentences,
where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in
a single sentence.
"""
from typing import List


class Solution:
    """Maximum Number of Words Found in Sentences Class."""

    def mostWordsFound(self, sentences: List[str]) -> int:
        """Maximum Number of Words Found in Sentences Function."""
        return max([len(x.split()) for x in sentences])


def main():
    """Solution."""
    s = Solution()
    nums = ["This is fun", "This is fun fun", "This isfun"]
    answer = s.mostWordsFound(nums)
    print(answer)


if __name__ == "__main__":
    main()
