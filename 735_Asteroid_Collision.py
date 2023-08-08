from typing import List
import unittest


class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        astack = []

        for i in a:
            if i > 0:
                astack.append(i)

            elif i < 0:
                if len(astack) == 0:
                    astack.append(i)
                    continue

                destroid = True
                while destroid and len(astack) > 0:
                    popped = astack[-1]
                    if popped < 0:
                        astack.append(i)
                        destroid = False

                    elif popped == abs(i):
                        astack.pop()
                        destroid = False

                    elif popped < abs(i):
                        astack.pop()
                        if len(astack) == 0:
                            astack.append(i)
                            destroid = False

                    elif popped > abs(i):
                        destroid = False

        return astack


class TestSolution(unittest.TestCase):
    """735. Asteroid Collision."""
    def test_asteroidCollision(self):
        sol = Solution()
        asteroids = [5,10,-5]
        exp = [5,10]
        out = sol.asteroidCollision(asteroids)
        self.assertEqual(out, exp)

        asteroids = [8,-8]
        exp = []
        out = sol.asteroidCollision(asteroids)
        self.assertEqual(out, exp)

        asteroids = [10,2,-5]
        exp = [10]
        out = sol.asteroidCollision(asteroids)
        self.assertEqual(out, exp)

        asteroids = [-4, 6]
        exp = [-4, 6]
        out = sol.asteroidCollision(asteroids)
        self.assertEqual(out, exp)

        asteroids = [1,-2,10,-5]
        exp =  [-2, 10]
        out = sol.asteroidCollision(asteroids)
        self.assertEqual(out, exp)

        asteroids = [-2,-1,1,2]
        exp =  [-2,-1,1,2]
        out = sol.asteroidCollision(asteroids)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
