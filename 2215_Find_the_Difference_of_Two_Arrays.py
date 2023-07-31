from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1, n2 = set(nums1), set(nums2)
        return [list(n1.difference(n2)), list(n2.difference(n1))]


def main():
    """Solution."""
    sol = Solution()
    nums11 = [1,2,3]
    nums12 = [2,4,6]
    nums21 = [1,2,3,3]
    nums22 = [1,1,2,2]
    print("Answer:", sol.findDifference(nums11, nums12), '...([[1,3],[4,6]])')
    print("Answer:", sol.findDifference(nums21, nums22), '...([[3],[]])')


if __name__ == '__main__':
    main()
