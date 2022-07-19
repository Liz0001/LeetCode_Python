"""
771. Jewels and Stones from Leetcode.

You're given strings jewels representing
the types of stones that are jewels,
and stones representing the stones you have.
Each character in stones is a type of stone you
have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered
a different type of stone from "A".
"""


class Solution:
    """Jewels and Stones Class."""

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """Jewels and Stones Function."""
        nr = 0
        for jewel in jewels:
            if jewel in stones:
                nr += stones.count(jewel)
        return nr


def main():
    """Solution."""
    s = Solution()
    a = "z"
    b = "ZZ"
    answer = s.numJewelsInStones(a, b)
    print(answer)


if __name__ == "__main__":
    main()
