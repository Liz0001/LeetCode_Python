import unittest


class Solution:
    def minOperations(self, boxes: str) -> [int]:
        res = [0]*len(boxes)
        
        for start in range(len(boxes)):
            if boxes[start] == '1':
                ptr = start
                count = 0
                while ptr < len(boxes)-1:
                    count += 1
                    ptr +=1
                    res[ptr] += count
                    
        boxes = boxes[::-1]
        res = res[::-1]
        
        for end in range(len(boxes)):
            if boxes[end] == '1':
                ptr = end
                count = 0
                while ptr < len(boxes)-1:
                    count += 1
                    ptr +=1
                    res[ptr] += count
        return res[::-1]
        

class TestSolution(unittest.TestCase):
    """1769. Minimum Number of Operations to Move All Balls to Each Box."""

    def test_minOperations(self):
        sol = Solution()

        boxes = "110"
        exp = [1,1,3]
        out = sol.minOperations(boxes)
        self.assertEqual(exp, out)

        boxes = "001011"
        exp = [11,8,5,4,3,4]
        out = sol.minOperations(boxes)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
