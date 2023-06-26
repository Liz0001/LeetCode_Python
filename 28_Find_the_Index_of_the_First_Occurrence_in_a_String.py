class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        return haystack.index(needle)


def main():
    """Solution."""
    sol = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(sol.strStr(haystack, needle))


if __name__ == '__main__':
    main()
