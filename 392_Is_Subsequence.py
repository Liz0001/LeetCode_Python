class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        tt = list(t)
        start = 0

        for i in s:
            sub = tt[start:len(tt)]
            if i in sub:
                ind = sub.index(i)
                start += ind+1
            else:
                return False

        return True




def main():
    """Solution."""
    sol = Solution()
    s1 = "abc"
    t1 = "ahbgdc"
    s2 = "axc"
    t2 = "ahbgdc"
    s3 = "aaaaaa"
    t3 = "bbaaaa"
    print("Answer 1:", sol.isSubsequence(s1, t1))
    print("Answer 2:", sol.isSubsequence(s2, t2))
    print("Answer 3:", sol.isSubsequence(s3, t3))
    


if __name__ == '__main__':
    main()
    