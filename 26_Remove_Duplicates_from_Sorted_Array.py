from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        se = list(set(nums))
        se.sort()
        l = len(se)
        
        for i in range(0, l):
            nums[i] = se[i]
        
        return l


def main():
    """Solution."""
    sol = Solution()
    nums = [-1,0,0,0,0,3,3]
    print(sol.removeDuplicates(nums))


if __name__ == '__main__':
    main()
