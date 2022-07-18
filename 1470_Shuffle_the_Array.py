"""
1470. Shuffle the Array from Leetcode.

Given the array nums consisting of 2n elements
in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""
from typing import List


class Solution:
    """Shuffle the Array Class."""

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """Shuffle the Array Function."""
        new_list = []
        for i in range(0, len(nums)-n):
            new_list.append(nums[i])
            new_list.append(nums[i+n])
        return new_list


def main():
    """Solution."""
    s = Solution()
    nums = [2, 5, 1, 3, 4, 7]
    target = 3
    # [2,3,5,4,1,7] - output
    answer = s.shuffle(nums, target)
    print(answer)


if __name__ == "__main__":
    main()
