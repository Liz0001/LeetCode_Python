from typing import List
import unittest


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        different_groups = set(groupSizes)
        g = {}
        res = []

        for df in different_groups:
            g[df] = []
        
        for i in range(len(groupSizes)):
            g[groupSizes[i]].append(i)
        
        for i in g:
            ag = g.get(i)
            j = [ag[x:x+i] for x in range(0, len(ag), i)]
            res += j
        return res
    
    
class TestSolution(unittest.TestCase):
    """1282. Group the People Given the Group Size They Belong To."""

    def test_groupThePeople(self):
        sol = Solution()
        
        groupSizes = [3,3,3,3,3,1,3]
        exp = [[5],[0,1,2],[3,4,6]]
        out = sol.groupThePeople(groupSizes)
        self.assertEqual(out, exp)
        
        groupSizes = [2,1,3,3,3,2]
        exp = [[1],[0,5],[2,3,4]]
        out = sol.groupThePeople(groupSizes)
        self.assertEqual(out, exp)
        

if __name__ == '__main__':
    unittest.main()
