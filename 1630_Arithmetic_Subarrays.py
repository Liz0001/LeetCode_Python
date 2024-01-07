import unittest


class Solution:
    def checkArithmeticSubarrays(self, nums: [int], l: [int], r: [int]) -> [bool]:
        ans = []
        for i in range(len(l)):
            n = nums[l[i]:r[i]+1]
            n.sort()
            ans.append(self.check_seq(n))
        return ans
    
    
    def check_seq(self, arr):
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != arr[1] - arr[0]:
                return False
        return True


class TestSolution(unittest.TestCase):
    """1630. Arithmetic Subarrays."""

    def test_checkArithmeticSubarrays(self):
        sol = Solution()
        
        nums = [4,6,5,9,3,7]
        l = [0,0,2]
        r = [2,3,5]
        exp = [True,False,True]
        out = sol.checkArithmeticSubarrays(nums, l, r)
        self.assertEqual(exp, out)

        nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
        l = [0,1,6,4,8,7]
        r = [4,4,9,7,9,10]
        exp = [False,True,False,False,True,True]
        out = sol.checkArithmeticSubarrays(nums, l, r)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
