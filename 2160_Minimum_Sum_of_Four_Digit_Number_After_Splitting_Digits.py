"""
2160. Minimum Sum of Four Digit Number After Splitting Digits from Leetcode.

You are given a positive integer num consisting of exactly four digits.
Split num into two new integers new1 and new2 by using the digits found 
in num. Leading zeros are allowed in new1 and new2, and all the digits
found in num must be used.

For example, given num = 2932, you have the following digits:
two 2's, one 9 and one 3. Some of the possible pairs
[new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.
"""


class Solution:
    """Minimum Sum of Four Digit Number After Splitting Digits Class."""

    def minimumSum(self, num: int) -> int:
        """Minimum Sum of Four Digit Number After Splitting Digits Function."""
        a = num // 1000
        b = int((num - (a*1000)) / 100)
        c = int((num - (a*1000) - (b*100)) // 10)
        d = int(num - (a*1000) - (b*100) - (c*10))

        nums = [a, b, c, d]
        nums.sort()
        return int(str(nums[0]) + "" + str(nums[3])) + int(str(nums[1]) + "" + str(nums[2]))


def main():
    """Solution."""
    s = Solution()
    target = 4009   # 13
    # target = 2932   # 52
    answer = s.minimumSum(target)
    print(answer)


if __name__ == "__main__":
    main()
