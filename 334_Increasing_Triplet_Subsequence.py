from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3 or len(set(nums)) < 3:
            return False

        for i in range(0, len(nums)):
            for j in range(len(nums)-1, -1, -1):
                if j > i and nums[j] > nums[i]:
                    sub_arr = nums[i+1:j]
                    for x in range(0, len(sub_arr)):
                        if nums[i] < sub_arr[x] and sub_arr[x] < nums[j]:
                            return True

        return False


def main():
    """Solution."""
    sol = Solution()
    nums = [0, 4, 2, 1, 0, -1, -3]
    print("Answer:", sol.increasingTriplet(nums))


if __name__ == '__main__':
    main()
