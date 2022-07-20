"""
1720. Decode XORed Array from Leetcode.

There is a hidden integer array arr that
consists of n non-negative integers.

It was encoded into another integer array encoded
of length n - 1, such that encoded[i] = arr[i] XOR
arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an
integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved
that the answer exists and is unique.
"""
from typing import List


class Solution:
    """Decode XORed Array Class."""

    def decode(self, encoded: List[int], first: int) -> List[int]:
        """Decode XORed Array Function."""
        res = [first]
        for i in encoded:
            res.append(res[-1] ^ i)
        return res


def main():
    """Solution."""
    s = Solution()
    nums = [6, 2, 7, 3]
    target = 4
    # [4, 2, 0, 7, 4] - output
    answer = s.decode(nums, target)
    print(answer)


if __name__ == "__main__":
    main()

        