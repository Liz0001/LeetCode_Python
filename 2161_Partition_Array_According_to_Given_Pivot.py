import unittest


class Solution:
    def pivotArray(self, nums: [int], pivot: int) -> [int]:
        less = []
        equal = []
        more = []
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                equal.append(i)
        return less + equal + more
        

class TestSolution(unittest.TestCase):
    """2161. Partition Array According to Given Pivot"""

    def test_pivotArray(self):
        sol = Solution()
        
        nums = [9,12,5,10,14,3,10]
        pivot = 10
        exp = [9,5,3,10,10,12,14]
        out = sol.pivotArray(nums, pivot)
        self.assertEqual(exp, out)

        nums = [-3,4,3,2]
        pivot = 2
        exp = [-3,2,4,3]
        out = sol.pivotArray(nums, pivot)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
