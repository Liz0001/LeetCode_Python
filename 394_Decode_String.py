import unittest


class Solution:
    def decodeString(self, s: str) -> str:
        ss = []
        num = ''
        for i in s:
            if i.isnumeric():
                num += i
                continue

            if i == ']':
                txt = []

                while True and len(ss) > 0:
                    val = ss.pop()
                    if val.isnumeric():
                        x = int(val)
                        txt = txt[::-1]
                        ss += (x * txt)
                        break

                    elif val != '[':
                        txt.append(val)

            else:
                if len(num) > 0:
                    ss.append(num)
                    num = ''
                ss.append(i)

        return "".join(ss)


class TestSolution(unittest.TestCase):
    """394. Decode String."""

    def test_decodeString(self):
        sol = Solution()
        # s = "3[a]2[bc]"
        # exp = "aaabcbc"
        # out = sol.decodeString(s)
        # self.assertEqual(out, exp)

        # s = "3[a2[c]]"
        # exp = "accaccacc"
        # out = sol.decodeString(s)
        # self.assertEqual(out, exp)

        # s = "2[abc]3[cd]ef"
        # exp =  "abcabccdcdcdef"
        # out = sol.decodeString(s)
        # self.assertEqual(out, exp)

        s = "100[leetcode]"
        exp = "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
        out = sol.decodeString(s)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
