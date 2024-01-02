from typing import List
import unittest


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        x = nums.count(max(set(nums), key = nums.count))
        arr = []
        for i in range(x):
            arr.append([])
        c = 0
        for n in nums:
            go = True
            while go:
                if n in arr[c]:
                    c += 1
                    continue
                arr[c].append(n)
                c = 0
                go = False
                
        return arr
        

class TestSolution(unittest.TestCase):
    """2610. Convert an Array Into a 2D Array With Conditions."""

    def test_findMatrix(self):
        sol = Solution()

        nums = [1,3,4,1,2,3,1]
        exp = [[1,3,4,2],[1,3],[1]]
        out = sol.findMatrix(nums)
        self.assertEqual(out, exp)

        nums = [1,2,3,4]
        exp = [[1,2,3,4]]
        out = sol.findMatrix(nums)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
