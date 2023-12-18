import unittest


class Solution:
    def garbageCollection(self, g: [str], t: [int]) -> int:
        gg = ''.join(g)
        time = 0
        
        if "G" in gg:
            i = ([(pos, word) for pos, word in enumerate(g) if 'G' in word][-1])[0]
            time += sum(t[:i]) + gg.count("G")
            
        if "P" in gg:
            i = ([(pos, word) for pos, word in enumerate(g) if 'P' in word][-1])[0]
            time += sum(t[:i]) + gg.count("P")
            
        if "M" in gg:
            i = ([(pos, word) for pos, word in enumerate(g) if 'M' in word][-1])[0]
            time += sum(t[:i]) + gg.count("M")
            
        return time
        
        
class TestSolution(unittest.TestCase):
    """2391. Minimum Amount of Time to Collect Garbage."""

    def test_garbageCollection(self):
        sol = Solution()

        garbage = ["G","P","GP","GG"]
        travel = [2,4,3]
        exp = 21
        out = sol.garbageCollection(garbage, travel)
        self.assertEqual(out, exp)

        garbage = ["MMM","PGM","GP"]
        travel = [3,10]
        exp = 37
        out = sol.garbageCollection(garbage, travel)
        self.assertEqual(out, exp)
        

if __name__ == '__main__':
    unittest.main()
