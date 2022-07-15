"""
2011. Final Value of Variable After Performing Operations from Leetcode.

There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of
operations, return the final value of X after performing
all the operations.
"""
from typing import List


class Solution:
    """Final Value of Variable After Performing Operations Class."""

    def finalValueAfterOperations(self, op: List[str]) -> int:
        """Final Value of Variable After Performing Operations Function."""
        y = 0
        for i in op:
            if i[1] == "+":
                y += 1
            else:
                y -= 1
        return y


def main():
    """Solution."""
    s = Solution()
    operations = ["--X", "X++", "X++"]
    answer = s.finalValueAfterOperations(operations)
    print(answer)


if __name__ == "__main__":
    main()
