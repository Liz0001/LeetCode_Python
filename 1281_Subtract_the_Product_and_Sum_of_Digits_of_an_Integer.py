"""
1281. Subtract the Product and Sum of Digits of an Integer from Leetcode.

Given an integer number n, return the difference between the product
of its digits and the sum of its digits.
"""




class Solution:
    """Subtract the Product and Sum of Digits of an Integer Class."""

    def subtractProductAndSum(self, n: int) -> int:
        """Subtract the Product and Sum of Digits of an Integer Function."""
        m = 1
        for j in str(n):
            m = m * int(j)
        return m - (sum(([1 * int(i) for i in str(n)])))


def main():
    """Solution."""
    s = Solution()
    num = 234
    answer = s.subtractProductAndSum(num)
    print(answer)


if __name__ == "__main__":
    main()
