"""
1365. How Many Numbers Are Smaller Than the Current Number from Leetcode.

Given the array nums, for each nums[i] find out how many numbers
in the array are smaller than it. That is, for each nums[i] you have to
count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""
from typing import List


class Solution:
    """How Many Numbers Are Smaller Than the Current Number Class."""

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """How Many Numbers Are Smaller Than the Current Number Function."""
        output = []
        m = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j and nums[i] > nums[j]:
                    m += 1
            output.append(m)
            m = 0
        return output


def main():
    """Solution."""
    s = Solution()
    nums = [8, 1, 2, 2, 3]
    # [4,0,1,1,3]
    answer = s.smallerNumbersThanCurrent(nums)
    print(answer)


if __name__ == "__main__":
    main()
