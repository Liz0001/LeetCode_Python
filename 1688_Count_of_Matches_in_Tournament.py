"""
1688. Count of Matches in Tournament from Leetcode.

You are given an integer n, the number of teams in a tournament
that has strange rules:

If the current number of teams is even,
each team gets paired with another team.
A total of n / 2 matches are played,
and n / 2 teams advance to the next round.
If the current number of teams is odd,
one team randomly advances in the tournament,
and the rest gets paired. A total of
(n - 1) / 2 matches are played, and (n - 1) / 2 + 1 
teams advance to the next round.
Return the number of matches played in the
tournament until a winner is decided.
"""


class Solution:
    """Count of Matches in Tournament Class."""

    def numberOfMatches(self, n: int) -> int:
        """Count of Matches in Tournament."""
        match = 0
        while n > 1:
            if n % 2 == 0:
                match += int(n/2)
                n -= int(n/2)
            else:
                match += int((n-1)/2)
                n -= int((n-1)/2)
        return match


def main():
    """Solution."""
    s = Solution()
    n = 14
    answer = s.numberOfMatches(n)
    print(answer)


if __name__ == "__main__":
    main()
