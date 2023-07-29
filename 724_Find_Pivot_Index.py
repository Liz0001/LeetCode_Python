from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr_len = len(nums)
        left = 0
        right = r = sum(nums) - nums[0]

        if arr_len == 1 or right == 0:
            return 0

        for i in range(1, arr_len):
            left += nums[i-1]
            right -= nums[i]

            if left == right:
                return i
        
        if r + nums[0] - nums[arr_len-1] == 0:
            return arr_len-1

        return -1


def main():
    """Solution."""
    sol = Solution()
    nums1 = [1,7,3,6,5,6]
    nums2 = [1,2,3]
    nums3 = [2,1,-1]
    nums4 = [-1,-1,0,1,1,0]
    nums5 = [-1,-1,-1,0,1,1]
    nums6 = [-1,-1,1,1,0,0]
    nums7 = [-1,-1,-1,-1,-1,-1]
    print("Answer:", sol.pivotIndex(nums1), "(3)")
    print("Answer:", sol.pivotIndex(nums2), "(-1)")
    print("Answer:", sol.pivotIndex(nums3), "(0)")
    print("Answer:", sol.pivotIndex(nums4), "(5)")
    print("Answer:", sol.pivotIndex(nums5), "(0)")
    print("Answer:", sol.pivotIndex(nums6), "(4)")
    print("Answer:", sol.pivotIndex(nums7), "(-1)")
    
    
    
    


if __name__ == '__main__':
    main()
