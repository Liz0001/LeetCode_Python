

class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        aa = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        leftie = 0
        rightie = len(ss)-1
        while leftie <= rightie:
            if leftie == rightie:
                break
            if ss[leftie] not in aa:
                leftie += 1
            if ss[rightie] not in aa:
                rightie -= 1
            
            if ss[leftie] in aa and ss[rightie] in aa:
                ss[leftie], ss[rightie] = ss[rightie], ss[leftie]
                leftie += 1
                rightie -= 1
            
        return ''.join(ss)


def main():
    """Solution."""
    sol = Solution()
    s = "leetcode"
    print(sol.reverseVowels(s))


if __name__ == '__main__':
    main()
