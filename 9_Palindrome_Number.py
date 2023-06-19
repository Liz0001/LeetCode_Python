
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if (x < 0):
        #     return False
        # xList = list(map(int, str(x)))
        # j = len(xList)
        
        # for i in range(0, (len(xList)//2)):
        #     j = j-1
        #     if xList[i] != xList[j]:
        #         return False
        # return True
        y = int((str(x)[::-1]))
        if x == y:
            return True
        return False


def main():
    """Solution."""
    sol = Solution()
    num = 1221
    print(sol.isPalindrome(num))


if __name__ == "__main__":
    main()
