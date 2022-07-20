"""
1313. Decompress Run-Length Encoded List.

We are given a list nums of integers representing a list
ompressed with run-length encoding.

Consider each adjacent pair of elements
[freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with
value val concatenated in a sublist. Concatenate all the
sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""
from typing import List


class Solution:
    """Decompress Run-Length Encoded List Class."""

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        """Decompress Run-Length Encoded List."""
        x = []
        for i in range(0, len(nums), 2):
            print(i)
            for j in range(0, nums[i]):
                x.append(nums[i+1])
        return x


def main():
    """Solution."""
    s = Solution()
    nums = [42, 39, 2, 1]
    answer = s.decompressRLElist(nums)
    print(answer)


if __name__ == "__main__":
    main()
