from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        step = 0

        zero_count = 0
        sec = step

        count = 0
        longest = 0

        while step < length:
            num = nums[step]

            if num == 1:
                count += 1
                step += 1
                continue

            if num == 0 and zero_count < k:
                zero_count += 1
                count += 1
                step += 1
                continue

            if num == 0:
                longest = max(longest, count)
                zero_count += 1

                while zero_count > k:
                    sec_num = nums[sec]
                    if sec_num == 0:
                        zero_count -= 1
                    count -= 1
                    sec += 1

                count += 1
                step += 1

        longest = max(longest, count)

        return longest



def main():
    """Solution."""
    sol = Solution()
    nums1 = [1,1,1,0,0,0,1,1,1,1,0]
    k1 = 2
    nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k2 = 3
    nums3 = [0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1]
    k3 = 2197
    nums4 = [0,0,0,0]
    k4 = 0
    nums5 = [0,0,0,1]
    k5 = 4
    print("Answers:", sol.longestOnes(nums1, k1), '(6)')
    print("Answers:", sol.longestOnes(nums2, k2), '(10)')
    print("Answers:", sol.longestOnes(nums3, k3), '(4391)')
    print("Answers:", sol.longestOnes(nums4, k4), '(0)')
    print("Answers:", sol.longestOnes(nums5, k5), '(4)')
    

    


if __name__ == '__main__':
    main()