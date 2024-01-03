import unittest


class Solution:
    def numberOfBeams(self, bank: [str]) -> int:
        bank = bank[::-1]
        total = 0
        c = 0
        for i in bank:
            if '1' in i:
                iii = i.count("1")
                total += c*iii
                c = iii    
        return total
    

class TestSolution(unittest.TestCase):
    """2125. Number of Laser Beams in a Bank."""

    def test_numberOfBeams(self):
        sol = Solution()
        
        bank = ["011001","000000","010100","001000"]
        exp = 8
        out = sol.numberOfBeams(bank)
        self.assertEqual(exp, out)
        
        bank = ["000","111","000"]
        exp = 0
        out = sol.numberOfBeams(bank)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
