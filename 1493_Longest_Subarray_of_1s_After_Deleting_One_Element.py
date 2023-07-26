from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        most, curr = 0, 0
        i, j, k = 0, 0, 0

        while j < n:
            num = nums[j]

            if num == 1:
                curr += 1
                j += 1
                continue

            if num == 0 and k < 1:
                curr += 1
                j += 1
                k += 1
                continue

            if num == 0 and k >= 1:
                most = max(most, curr)
                k = + 1

                while k > 0 :
                    if nums[i] == 0:
                        k -= 1
                    i += 1
                    curr -= 1

        most = max(most, curr)

        return most - 1


def main():
    """Solution."""
    sol = Solution()
    nums1 = [1,1,0,1]
    nums2 = [0,1,1,1,0,1,1,0,1]
    nums3 = [1,1,1]
    nums4 = [1,1,0,0,1,1,1,0,1]
    print("Answer:", sol.longestSubarray(nums1), "(3)")
    print("Answer:", sol.longestSubarray(nums2), "(5)")
    print("Answer:", sol.longestSubarray(nums3), "(2)")
    print("Answer:", sol.longestSubarray(nums4), "(4)")


if __name__ == '__main__':
    main()
