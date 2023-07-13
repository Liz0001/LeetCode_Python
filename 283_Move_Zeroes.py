from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        print(nums)
        for i in range(0, len(nums)):
            if nums[i] != 0:
                continue
            
            for j in range(len(nums)-1, i, -1):
                if nums[j] == 0:
                    continue
                nums[j], nums[i] = nums[i], nums[j]
        print(nums)


def main():
    """Solution."""
    sol = Solution()
    nums1 = [0,1,0,3,12]
    nums2 = [0]
    nums3 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0] 
    # sol.moveZeroes(nums1)
    # sol.moveZeroes(nums2)
    sol.moveZeroes(nums3)


if __name__ == "__main__":
    main()
