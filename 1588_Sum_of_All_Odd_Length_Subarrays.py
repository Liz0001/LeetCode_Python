"""
1588. Sum of All Odd Length Subarrays from Leetcode.

Given an array of positive integers arr,
return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
"""
from typing import List


class Solution:
    """Sum of All Odd Length Subarrays Class."""

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """Sum of All Odd Length Subarrays."""
        ss = []
        for n in range(1, len(arr)+1, 2):
            for i in range(len(arr)+1-n):
                ss.append(arr[i:i+n])
        return (sum(sum(s) for s in ss))


def main():
    """Solution."""
    s = Solution()
    arr = [1, 4, 2, 5, 3]       # 58
    answer = s.sumOddLengthSubarrays(arr)
    print(answer)


if __name__ == "__main__":
    main()
