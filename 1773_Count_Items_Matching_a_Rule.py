"""
1773. Count Items Matching a Rule from Leetcode.

You are given an array items, where each items[i] = [typei, colori, namei]
describes the type, color, and name of the ith item. You are also given a
rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
"""
from typing import List


class Solution:
    """Count Items Matching a Rule class."""

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """Count Items Matching a Rule."""
        hmm = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        count = 0
        for i in range(len(items)):
            if items[i][hmm[ruleKey]] == ruleValue:
                count += 1
        return count


def main():
    """Solution."""
    s = Solution()
    items = [["phone", "blue", "pixel"],
             ["computer", "silver", "lenovo"],
             ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    answer = s.countMatches(items, ruleKey, ruleValue)
    print(answer)


if __name__ == "__main__":
    main()
