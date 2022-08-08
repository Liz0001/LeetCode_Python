"""
1486. XOR Operation in an Array from Leetcode.

You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed)
and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""


class Solution:
    """XOR Operation in an Array Class."""

    def xorOperation(self, n: int, start: int) -> int:
        """XOR Operation in an Array."""
        num = start
        for i in range(1, n):
            num = num ^ (start + 2 * i)
        return num


def main():
    """Solution."""
    s = Solution()
    n = 5
    start = 0
    answer = s.xorOperation(n, start)
    print(answer)


if __name__ == "__main__":
    main()
