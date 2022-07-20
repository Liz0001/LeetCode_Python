"""
1678. Goal Parser Interpretation from Leetcode.

You own a Goal Parser that can interpret a string command.
The command consists of an alphabet of "G", "()" and/or "(al)"
in some order. The Goal Parser will interpret "G" as the string "G",
"()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
"""


class Solution:
    """Goal Parser Interpretation Class."""

    def interpret(self, command: str) -> str:
        """Goal Parser Interpretation."""
        return command.replace("()", "o").replace("(al)", "al")


def main():
    """Solution."""
    s = Solution()
    sen = "G()(al)"
    answer = s.interpret(sen)
    print(answer)


if __name__ == "__main__":
    main()
