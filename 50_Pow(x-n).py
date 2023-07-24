import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x, n)


def main():
    """Solution."""
    sol = Solution()
    x1 = 2
    n1 = 3
    x2 = 2.00000
    n2 = -3 
    print(sol.myPow(x1, n1))
    print(sol.myPow(x2, n2))


if __name__ == '__main__':
    main()
