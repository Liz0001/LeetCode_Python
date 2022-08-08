"""
2367. Number of Arithmetic Triplets from Leetcode.

You are given a 0-indexed, strictly increasing integer array
nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.
"""
from typing import List


class Solution:
    """Number of Arithmetic Triplets Class."""

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """Number of Arithmetic Triplets."""
        tripList = []
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, -1, -1):
                for k in range(len(nums)-1, -1, -1):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff and not(i == j == k):
                        tripList.append((i, j, k))
        return len(set(tripList))


def main():
    """Solution."""
    s = Solution()
    nums = [4, 5, 6, 7, 8, 9]
    diff = 2
    answer = s.arithmeticTriplets(nums, diff)
    print(answer)


if __name__ == "__main__":
    main()
