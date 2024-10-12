import unittest
from typing import List


class TestSolution(unittest.TestCase):

    def test_numberOfEmployeesWhoMetTarget(self):
        sol = Solution()

        self.assertEqual(sol.numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2), 3)
        self.assertEqual(sol.numberOfEmployeesWhoMetTarget(hours = [5,1,4,2,2], target = 6), 0)


class Solution:
    """2798. Number of Employees Who Met the Target."""
    
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int: 
        hours.sort()
        c = 0
        for i in hours[::-1]:
            if i >= target:
                c += 1
            else:
                break
        return c


if __name__ == "__main__":
    unittest.main()
