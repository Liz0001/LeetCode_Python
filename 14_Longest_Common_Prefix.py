from typing import List

class Solution:
    def longestCommonPrefix(self, strs:List[str])-> str:
        prefix = ""
        pos = 0
        value = False
        strs.sort()
        for x in strs[0]:
            
            value = all(i[pos] == x for i in strs)
            pos += 1
            if (value):
                prefix += x
            else:
                return prefix

        return prefix


def main():
    """Solution."""
    sol = Solution()
    # strs = ["flower", "flow", "flight"]
    strs = ["ab", "a"]
    print(sol.longestCommonPrefix(strs))


if __name__ == '__main__':
    main()
