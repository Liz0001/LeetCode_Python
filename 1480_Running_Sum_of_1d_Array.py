"""
1480. Running Sum of 1d Array from Leetcode.

Given an array nums. We define a running sum of
an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
from typing import List


class Solution:
    """Running Sum of 1d Array Class."""

    def runningSum(self, nums: List[int]) -> List[int]:
        """Running Sum of 1d Array Function."""
        b = [nums[0]]
        for i in range(1, len(nums)):
            b.append((nums[i] + b[i-1]))
        return b


def main():
    """Solution."""
    s = Solution()
    nums = [1, 1, 1, 1, 1]
    # 1,2,3,4,5
    answer = s.runningSum(nums)
    print(answer)


if __name__ == "__main__":
    main()
