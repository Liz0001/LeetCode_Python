import unittest


class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(i) for i in n])


class TestSolution(unittest.TestCase):
    """1689. Partitioning Into Minimum Number Of Deci-Binary Numbers."""
    
    def test_minPartitions(self):
        sol = Solution()
        
        n = "32"
        exp = 3
        out = sol.minPartitions(n)
        self.assertEqual(exp, out)
        
        n = "82734"
        exp = 8
        out = sol.minPartitions(n)
        self.assertEqual(exp, out)

        n = "27346209830709182346"
        exp = 9
        out = sol.minPartitions(n)
        self.assertEqual(exp, out)


if __name__ == "__main__":
    unittest.main()
