"""
1431. Kids With the Greatest Number of Candies from Leetcode.

There are n kids with candies. You are given an integer
array candies, where each candies[i] represents the number
of candies the ith kid has, and an integer extraCandies,
denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i]
is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all
the kids, or false otherwise.

Note that multiple kids can have the greatest number
of candies.
"""
from typing import List


class Solution:
    """Kids With the Greatest Number of Candies Class."""

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """Kids With the Greatest Number of Candies Function."""
        answer = []
        for i in candies:
            if i + extraCandies >= max(candies):
                answer.append(True)
            else:
                answer.append(False)
        return answer


def main():
    """Solution."""
    s = Solution()
    candy = [2, 3, 5, 1, 3]
    extra = 3
    answer = s.kidsWithCandies(candy, extra)
    print(answer)


if __name__ == "__main__":
    main()
