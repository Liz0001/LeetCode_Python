import unittest


class Solution:
    """2894. Divisible and Non-divisible Sums Difference."""
    
    def differenceOfSums(self, n: int, m: int) -> int:
        s1 = sum([i for i in range(1, n+1) if i % m != 0])
        s2 = sum([i for i in range(1, n+1) if i % m == 0])
        return s1-s2


class TestSolution(unittest.TestCase):

    def test_differenceOfSums(self):
        sol = Solution()
        
        self.assertEqual(sol.differenceOfSums(n = 10, m = 3), 19)
        self.assertEqual(sol.differenceOfSums(n = 5, m = 6), 15)
        self.assertEqual(sol.differenceOfSums(n = 5, m = 1), -15)


if __name__ == "__main__":
    unittest.main()
