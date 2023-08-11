import unittest


class Solution:
    def predictPartyVictory(self, s: str) -> str:
        ss = list(s)
        while "R" in ss and "D" in ss:
            vote = ss.pop(0)
            next_v = ss[0]
                
            if vote != next_v:
                ss.append(vote)
                ss.pop(0)
                continue
 
            if vote == next_v:
                ss.append(vote)
                if vote == 'R':
                    ss.remove("D")
                else:
                    ss.remove("R")

        if "R" not in ss:
            return "Dire"
        if "D" not in ss:
            return "Radiant"    


class TestSolution(unittest.TestCase):
    """649. Dota2 Senate."""

    def test_predictPartyVictory(self):
        sol = Solution()
        senate = "RD"
        exp = "Radiant"
        out = sol.predictPartyVictory(senate)
        self.assertEqual(out, exp)

        senate = "RDD"
        exp = "Dire"
        out = sol.predictPartyVictory(senate)
        self.assertEqual(out, exp)

        senate = "DDRRR"
        exp = "Dire"
        out = sol.predictPartyVictory(senate)
        self.assertEqual(out, exp)

        senate = "DRDRR"
        exp = "Dire"
        out = sol.predictPartyVictory(senate)
        self.assertEqual(out, exp)

        senate = "DRRDRDRDRDDRDRDR"
        exp = "Radiant"
        out = sol.predictPartyVictory(senate)
        self.assertEqual(out, exp)

        senate = "RRDRDDRDRRDDDDDRDRDR"
        exp = "Radiant"
        out = sol.predictPartyVictory(senate)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
