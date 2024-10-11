import unittest


class Solution:
    """3280. Convert Date to Binary."""
    
    def convertDateToBinary(self, date: str) -> str:
        y, m, d = date.split("-")
        return bin(int(y)).split("b")[1]+"-"+bin(int(m)).split("b")[1]+"-"+bin(int(d)).split("b")[1]


class TestSolution(unittest.TestCase):

    def test_convertDateToBinary(self):
        sol = Solution()
        
        self.assertEqual(sol.convertDateToBinary(date = "2080-02-29"), "100000100000-10-11101")
        self.assertEqual(sol.convertDateToBinary(date = "1900-01-01"), "11101101100-1-1")


if __name__ == "__main__":
    unittest.main()
