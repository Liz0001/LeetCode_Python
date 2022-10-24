"""
1832. Check if the Sentence Is Pangram.

A pangram is a sentence where every letter of the English alphabet appears
at least once.

Given a string sentence containing only lowercase English letters,
return true if sentence is a pangram, or false otherwise.
"""


class Solution:
    """Check if the Sentence Is Pangram."""

    def checkIfPangram(self, sentence: str) -> bool:
        """Check if the Sentence Is Pangram."""
        for i in range(97, 123):
            if chr(i) not in sentence:
                return False
        return True


def main():
    """Solution."""
    solution = Solution()
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    answer = solution.checkIfPangram(sentence)
    print(answer)


if __name__ == "__main__":
    main()
