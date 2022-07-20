"""
1342. Number of Steps to Reduce a Number to Zero.

Given an integer num, return the number of steps
to reduce it to zero.

In one step, if the current number is even,
you have to divide it by 2, otherwise,
you have to subtract 1 from it.
"""


class Solution:
    """Number of Steps to Reduce a Number to Zero Class."""

    def numberOfSteps(self, num: int) -> int:
        """Number of Steps to Reduce a Number to Zero."""
        counter = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            counter += 1
        return counter



def main():
    """Solution."""
    s = Solution()
    num = 123
    answer = s.numberOfSteps(num)
    print(answer)


if __name__ == "__main__":
    main()
