from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current, highest  = 0, 0
        for i in range(len(gain)):
            current += gain[i]
            highest = max(highest, current)
        
        return highest


def main():
    """Solution."""
    sol = Solution()
    gain1 = [-5,1,5,0,-7]
    gain2 = [-4,-3,-2,-1,4,3,2]
    print("Answer:", sol.largestAltitude(gain1), "(1)")
    print("Answer:", sol.largestAltitude(gain2), "(0)")


if __name__ == '__main__':
    main()
