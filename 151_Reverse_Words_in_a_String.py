
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for word in range(len(words)-1, -1, -1):
            x = words.pop(word)
            words.append(x)
        
        return (" ".join(words)).strip()


def main():
    """Solution."""
    sol = Solution()
    s1 = "the sky    is blue"
    s2 = "  hello world  "
    print(sol.reverseWords(s1))
    print(sol.reverseWords(s2))


if __name__ == '__main__':
    main()
