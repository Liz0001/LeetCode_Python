"""
2413. Smallest Even Multiple from Leetcode.

Given a positive integer n, return the smallest
positive integer that is a multiple of both 2 and n.
"""


class Solution:
    """Smallest Even Multiple Class."""

    def smallestEvenMultiple(self, n: int) -> int:
        """Smallest Even Multiple."""
        return n if (n % 2 == 0) else n*2


def main():
    """Solution."""
    solution = Solution()
    n = 5
    answer = solution.smallestEvenMultiple(n)
    print(answer)
    n = 6
    answer = solution.smallestEvenMultiple(n)
    print(answer)


if __name__ == "__main__":
    main()
