"""
1221. Split a String in Balanced Strings from Leetcode.

Balanced strings are those that
have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.
"""


class Solution:
    """Split a String in Balanced Strings Class."""

    def balancedStringSplit(self, s: str) -> int:
        """Split a String in Balanced Strings."""
        l, r = 0, 0
        count = 0
        for i in s:
            if 'L' == i:
                l += 1
            else:
                r += 1
            if r == l:
                count += 1
        return count


def main():
    """Solution."""
    s = Solution()
    # target = "RLRRRLLRLL"       #  2
    target = "RLRRLLRLRL"       # 4
    answer = s.balancedStringSplit(target)
    print(answer)


if __name__ == "__main__":
    main()
