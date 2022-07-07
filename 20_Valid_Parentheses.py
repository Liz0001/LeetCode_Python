"""
20. Valid Parentheses from Leetcode.

Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
from typing import str


class Solution:
    """Valid Parentheses Class."""

    def isValid(self, s: str) -> bool:
        """Valid Parentheses Function."""
        # # My solution
        stack = []
        if len(s) % 2 != 0:
            return False

        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "{":
                stack.append("}")
            elif i == "[":
                stack.append("]")

            elif i == ")" or i == "}" or i == "]":
                if stack == []:
                    return False

                popped = stack.pop()

                if i != popped:
                    return False

        if stack == []:
            return True


def main():
    """Solution."""
    x = Solution()
    # s = "(]"
    # s = "()"
    s = "(){}}{"
    answer = x.isValid(s)
    print(answer)


if __name__ == "__main__":
    main()
