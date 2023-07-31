import unittest
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1, n2 = set(nums1), set(nums2)
        return [list(n1.difference(n2)), list(n2.difference(n1))]


def main():
    """Solution."""
    sol = Solution()
    nums11 = [1,2,3]
    nums12 = [2,4,6]
    nums21 = [1,2,3,3]
    nums22 = [1,1,2,2]
    print("Answer:", sol.findDifference(nums11, nums12), '...([[1,3],[4,6]])')
    print("Answer:", sol.findDifference(nums21, nums22), '...([[3],[]])')
    assert sol.findDifference(nums11, nums12) == [[1,3],[4,6]],  "Wrong answer, should be [[1,3],[4,6]]"
    assert sol.findDifference(nums21, nums22) == [[3],[]], "Wrong answer, should be [[3],[]]"
 

class TestSolution(unittest.TestCase):
    def test_findDifference1(self):
        sol = Solution()
        nums1 = [1,2,3]
        nums2 = [2,4,6]
        res = [[1,3],[4,6]]
        self.assertEqual(res, sol.findDifference(nums1, nums2))
        nums1 = [1,2,3,3]
        nums2 = [1,1,2,2]
        res = [[3],[]]
        self.assertEqual(res, sol.findDifference(nums1, nums2))


if __name__ == '__main__':
    main()
    unittest.main()
