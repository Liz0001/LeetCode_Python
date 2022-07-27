"""
1389. Create Target Array in the Given Order from Leetcode.

Given two arrays of integers nums and index.
Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i],
insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
"""
from typing import List


class Solution:
    """Create Target Array in the Given Order Class."""

    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:        # noqa
        """Create Target Array in the Given Order function."""
        arr = []
        for i in range(0, len(nums)):
            arr.insert(index[i], nums[i])
        return arr


def main():
    """Solution."""
    s = Solution()
    nums = [0, 1, 2, 3, 4]
    ind = [0, 1, 2, 2, 1]
    # [0,4,1,3,2] - output
    answer = s.createTargetArray(nums, ind)
    print(answer)


if __name__ == "__main__":
    main()
