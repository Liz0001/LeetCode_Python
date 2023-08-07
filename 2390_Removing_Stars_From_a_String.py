import unittest


class Solution:
    def removeStars(self, s: str) -> str:
        ss = list(s)
        stack = []
        mem = 0
        for i in ss:
            if i == '*' and len(stack) > 0:
                stack.pop()
            elif i == '*' and len(stack) == 0:
                mem += 1
            elif mem > 0:
                mem -= 1
            else:
                stack.append(i)

        return "".join(list(stack))


class TestSolution(unittest.TestCase):
    """2390. Removing Stars From a String."""

    def test_removeStars(self):
        sol = Solution()
        s = "leet**cod*e"
        exp = "lecoe"
        out = sol.removeStars(s)
        self.assertEqual(out, exp)

        s = "erase*****"
        exp = ""
        out = sol.removeStars(s)
        self.assertEqual(out, exp)

        s = "*e"
        exp = ""
        out = sol.removeStars(s)
        self.assertEqual(out, exp)

        s = "*****erase"
        exp = ""
        out = sol.removeStars(s)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
