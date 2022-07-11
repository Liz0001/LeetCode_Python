"""
1920. Build Array from Permutation from Leetcode.

Given a zero-based permutation nums (0-indexed),
build an array ans of the same length where ans[i] = nums[nums[i]]
for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of
distinct integers from 0 to nums.length - 1 (inclusive).
"""
from typing import List


class Solution:
    """Build Array from Permutation Class."""

    def buildArray(self, nums: List[int]) -> List[int]:
        """Build Array from Permutation Function."""
        # My solution
        ans = []
        for i in nums:
            ans.append(nums[i])
        return ans

        # Another solution
        # return [nums[i] for i in nums]


def main():
    """Solution."""
    s = Solution()
    nums = [0, 2, 1, 5, 3, 4]
    returned = s.buildArray(nums)
    print(returned)


if __name__ == "__main__":
    main()
