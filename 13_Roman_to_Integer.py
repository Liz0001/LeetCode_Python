
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        sum = roman[s[0]]
        for i in range(1, len(s)):
            
            prev = roman[s[i-1]]
            curr = roman[s[i]]
            
            if (prev >= curr):
                sum += curr
            
            if (prev < curr):
                sum += curr - (prev*2)
                
        return sum
        


def main():
    """Solution."""
    sol = Solution()
    x = "MCMXCIV"
    print(sol.romanToInt(x))


if __name__ == "__main__":
    main()
