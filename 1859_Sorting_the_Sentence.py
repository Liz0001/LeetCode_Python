"""
1859. Sorting the Sentence from Leetcode.

A sentence is a list of words that are separated
by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word
position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled
as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words,
reconstruct and return the original sentence.
"""


from hashlib import new
from tkinter import W


class Solution:
    """Sorting the Sentence Class."""

    def sortSentence(self, s: str) -> str:
        """Sorting the Sentence Function."""
        words_list = s.split()
        new_s = [""] * len(words_list)
        for word in words_list:
            place = int(word[-1])-1
            new_s[place] = word[:-1]
        return " ".join(new_s)


def main():
    """Solution."""
    s = Solution()
    # target = "is2 sentence4 This1 a3"
    target = "lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"
    answer = s.sortSentence(target)
    print(answer)


if __name__ == "__main__":
    main()
