from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        s, prev = "", ""
        count = 1
        for i in range(len(chars)):
            if i == 0:
                prev = chars[i]
                s += chars[i]
                continue

            if chars[i] == prev:
                count += 1
            else:
                if count > 1:
                    s += str(count)
                s += chars[i]
                count = 1

            if i == len(chars)-1 and count > 1:    
                s += str(count)
            prev = chars[i]

            c = 0
            for j in s:
                chars[c] = j
                c += 1

        return len(s)


def main():
    """Solution."""
    sol = Solution()
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    chars2 = ["a"]
    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    chars4 = ["a","b","c"]
    # print("Answer:", sol.compress(chars1))
    # print("Answer:", sol.compress(chars2))
    # print("Answer:", sol.compress(chars3))
    print("Answer:", sol.compress(chars4))
    


if __name__ == "__main__":
    main()
