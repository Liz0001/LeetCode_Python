import collections
from typing import List 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        biggest = max(candies)
        arr = []
        for i in candies:
            if i+extraCandies >= biggest:
                arr.append(True)
            else:
                arr.append(False)
        return arr


def main():
    """Solution."""
    sol = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(sol.kidsWithCandies(candies, extraCandies))

if __name__ == '__main__':
    main()
