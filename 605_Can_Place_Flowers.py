from typing import List

class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        if len(f) == 1:
            if 0 in f and n == 1:
                return True
            else:
                return False

        if len(f) == 2:
            if 0 in f and 1 not in f and n == 1:
                return True
            else:
                return False
            
        if f[0] == 0 and f[1] == 0:
            f[0] = 1
            n -= 1
            
        for i in range(1, len(f)-1):
            if n == 0:
                return True

            if f[i-1] == 0 and f[i+1] == 0 and f[i] == 0:
                f[i] = 1
                n-= 1           
        
        if n == 0:
            return True
        
        if f[len(f)-1] == 0 and f[len(f)-2] == 0:
            f[len(f)-1] = 1
            n -= 1
        
        return n == 0


def main():
    """Solution."""
    sol = Solution()
    
    flowerbed = [1,0,0,0,1]
    n = 1
    print(sol.canPlaceFlowers(flowerbed, n))
    print(sol.canPlaceFlowers([1,0,0,1,0,1,0,0,0,0], 1))
    print(sol.canPlaceFlowers([0,0,0,1], 1))
    print(sol.canPlaceFlowers([0,0,1], 1))
    print(sol.canPlaceFlowers([1,0,0], 1))
    print(sol.canPlaceFlowers([0,0,1,0,0], 2))
    print(sol.canPlaceFlowers([0], 1))
    print(sol.canPlaceFlowers([1,0,0,0,0,0,1], 2))
    print(sol.canPlaceFlowers([0,0,1,0,0,0,0,0,1,0,0], 4))


if __name__ == '__main__':
    main()
