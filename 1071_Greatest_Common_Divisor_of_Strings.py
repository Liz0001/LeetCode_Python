import math

class Solution:
    def gcdOfStrings(self, s: str, t: str) -> str:
        gcd = ''
        smallest_word = ''
        
        if s not in t and t not in s:
            return gcd
        
        if s == t:
            return s

        if s < t:
            s, t = t, s
        
        for j in t:
            smallest_word += j
            the_word = s
            if len(the_word.replace(smallest_word, '')) == 0:
                break

        if (len(s.replace(smallest_word, '')) > 0 or len(t.replace(smallest_word, '')) > 0):
            return gcd

        x = s.replace(smallest_word, 'x')
        y = t.replace(smallest_word, 'x')
        
        d = math.gcd(len(x), len(y))
        return d * smallest_word


def main():
    """Solution."""
    sol = Solution()
    str1 = "ABCABC"
    str2 = "ABC"
    print(sol.gcdOfStrings(str1, str2))


if __name__ == '__main__':
    main()
