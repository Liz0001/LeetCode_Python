"""
1672. Richest Customer Wealth from Leetcode .

"""
from typing import List


class Solution:
    """Richest Customer Wealth Class."""

    def maximumWealth(self, acc: List[List[int]]) -> int:
        """Richest Customer Wealth Function."""
        x = sum(acc[0])
        for i in acc:
            if sum(i) > x:
                x = sum(i)
        return x


def main():
    """Solution."""
    s = Solution()
    acc = [[4, 2, 3], [11, 9, 1]]
    answer = s.maximumWealth(acc)
    print(answer)


if __name__ == "__main__":
    main()
