"""
1512. Number of Good Pairs from Leetcode.

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from typing import List


class Solution:
    """Number of Good Pairs Class."""

    def numIdenticalPairs(self, nums: List[int]) -> int:
        """Number of Good Pairs Function."""
        pairs = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i != j:
                    pairs += 1
        return pairs


def main():
    """Solution."""
    s = Solution()
    nums = [1, 1, 1, 1]
    answer = s.numIdenticalPairs(nums)
    print(answer)


if __name__ == "__main__":
    main()
