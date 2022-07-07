"""
2235. Add Two Integers from Leetcode.

Given two integers num1 and num2, return the sum of the two integers.
"""


class Solution:
    """Add Two Integers Class."""

    def sum(self, num1, num2) -> int:
        """Add Two Integers Function."""
        return num1 + num2


def main():
    """Solution."""
    x = Solution()
    a = 2
    b = 5
    answer = x.sum(a, b)
    print(answer)


if __name__ == "__main__":
    main()
