"""
1929. Concatenation of Array from Leetcode.

Given an integer array nums of length n,
you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""
from typing import List


class Solution:
    """Concatenation of Array Class."""

    def getConcatenation(self, nums: List[int]) -> List[int]:
        """Concatenation of Array Function."""
        ans = []
        for i in nums:
            ans.append(i)

        return ans + nums


def main():
    """Solution."""
    s = Solution()
    nums = [4, 2, 3, 11, 9, 1]
    returned_list = s.getConcatenation(nums)
    print(returned_list)


if __name__ == "__main__":
    main()
