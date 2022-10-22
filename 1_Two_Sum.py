"""
1. Two Sum from Leetcode.

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:
    """Two Sum Class."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Two sum function."""
        # # My solution - Approach 1: Brute Force
        for i in range(0, len(nums)):
            for j in range(len(nums)-1, 0, -1):
                if nums[i] + nums[j] == target and not i == j:
                    return [i, j]

        # # Approach 2: Two-pass Hash Table
        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and hashmap[complement] != i:
        #         return [i, hashmap[complement]]

        # # Approach 3: One-pass Hash Table
        # hashmap = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap:
        #         return [i, hashmap[complement]]
        #     hashmap[nums[i]] = i


def main():
    """Solution."""
    solution = Solution()
    nums = [4, 2, 3, 11, 9, 1]
    target = 3
    answer = solution.twoSum(nums, target)
    print(answer)


if __name__ == "__main__":
    main()
