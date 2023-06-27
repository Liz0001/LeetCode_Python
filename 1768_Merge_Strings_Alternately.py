class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wordOne = list(word1)
        wordTwo = list(word2)
        w = ''
        if len(word1) <= len(word2):
            for x in range(0, len(word1)):
                w += wordOne[x]
                w += wordTwo[x]
            if (len(word2) > len(word1)):
                w += word2[-(len(word2) - len(word1)):]
        else:
            for x in range(0, len(word2)):
                w += wordOne[x]
                w += wordTwo[x]
            if (len(word1) > len(word2)):
                w += word1[-(len(word1) - len(word2)):]
        
        return w

def main():
    sol = Solution()
    word1 = "abcd"
    word2 = "pq"
    print(sol.mergeAlternately(word1, word2))


if __name__ == '__main__':
    main()
