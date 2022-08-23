"""
804. Unique Morse Code Words from Leetcode.

International Morse Code defines a standard encoding
where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the
English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be
written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...",
which is the concatenation of "-.-.", ".-", and "-...".
We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
"""

from typing import List


class Solution:
    """Unique Morse Code Words Class."""

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """Unique Morse Code Words."""
        malphabet = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
                     "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",      # noqa
                     "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
                     "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",        # noqa
                     "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                     "y": "-.--", "z": "--.."}
        codes = []
        for i in range(0, len(words)):
            # for j in i:
            morse = ""
            for j in words[i]:
                morse += malphabet[j]
            codes.append(morse)
        return len(set(codes))


def main():
    """Solution."""
    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    # output 2
    answer = s.uniqueMorseRepresentations(words)
    print(answer)


if __name__ == "__main__":
    main()
