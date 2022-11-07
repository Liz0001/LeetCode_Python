"""
2220. Minimum Bit Flips to Convert Number.

A bit flip of a number x is choosing a bit in the binary representation of
x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose
any bit (including any leading zeros not shown) and flip it. We can flip
the first bit from the right to get 110, flip the second bit from the
right to get 101, flip the fifth bit from the right
(a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit
flips to convert start to goal.
"""


class Solution:
    """Minimum Bit Flips to Convert Number."""

    def minBitFlips(self, start: int, goal: int) -> int:
        """Minimum Bit Flips to Convert Number."""
        diff = 0
        start = "{0:b}".format(start)
        goal = "{0:b}".format(goal)

        if (len(goal) < len(start)):
            goal = ((len(start) - len(goal)) * "0") + goal
        elif (len(start) < len(goal)):
            start = ((len(goal) - len(start)) * "0") + start

        for x, y in zip(goal, start):
            if x != y:
                diff += 1

        return diff


def main():
    """Solution."""
    solution = Solution()
    start = 3
    goal = 4
    answer = solution.minBitFlips(start, goal)
    print(answer)


if __name__ == "__main__":
    main()
