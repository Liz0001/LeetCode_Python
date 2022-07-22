"""
1528. Shuffle String.

You are given a string s and an
integer array indices of the same
length. The string s will be shuffled such that
the character at the ith position moves to indices[i]
in the shuffled string.

Return the shuffled string.
"""
from typing import List


class Solution:
    """Shuffle String."""

    def restoreString(self, ss: str, ind: List[int]) -> str:
        """Shuffle String."""
        new_list = [''] * len(ss)
        for i, char in enumerate(ss):
            new_list[ind[i]] = char
        return "".join(new_list)


def main():
    """Solution."""
    s = Solution()
    ss = "codeleet"
    yy = [4, 5, 6, 7, 0, 2, 1, 3]
    # yy = [1, 2, 3]
    answer = s.restoreString(ss, yy)
    print(answer)


if __name__ == "__main__":
    main()
