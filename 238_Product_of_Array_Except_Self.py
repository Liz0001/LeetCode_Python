from typing import List


class Solution:
    """Sol."""
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        righty = [1] * len(nums)
        lefty = [1] * len(nums)

        for i in range(1, len(nums)):
            lefty[i] = lefty[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            righty[i] = righty[i+1] * nums[i+1]

        for i in range(0, len(nums)):
            nums[i] = righty[i]*lefty[i]

        return nums


def main():
    """Solution."""
    sol = Solution()
    nums = [1, 2, 3, 4]
    # nums = [-1,1,0,-3,3]
    # nums = [4, 5, 1, 8, 2]
    print("RESULT", sol.productExceptSelf(nums))


if __name__ == '__main__':
    main()
