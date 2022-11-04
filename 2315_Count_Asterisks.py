"""
2315. Count Asterisks.

You are given a string s, where every two consecutive vertical bars '|'
are grouped into a pair. In other words, the 1st and 2nd '|' make a pair,
the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.
"""


class Solution:
    """Count Asterisks."""

    def countAsterisks(self, s: str) -> int:
        """Count Asterisks."""
        c = 0
        ans = 0
        for i in s:
            if i == "|" and c == 1:
                c = 0
            elif i == "|" and c == 0:
                c = 1

            if i == "*" and c == 0:
                ans += 1

        return ans


def main():
    """Solution."""
    solution = Solution()
    s = "l|*e*et|c**o|*de|"
    answer = solution.countAsterisks(s)
    print(answer)


if __name__ == "__main__":
    main()
