"""
2418. Sort the People.

You are given an array of strings names,
and an array heights that consists of distinct positive integers.
Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and
height of the ith person.

Return names sorted in descending order by the people's heights.
"""
from typing import List


class Solution:
    """Sort the People."""

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """Sort the People."""
        names2 = []
        for i in range(0, len(names)):
            index = heights.index(max(heights))
            names2.append(names[index])
            heights[index] = -1
        return names2


def main():
    """Solution."""
    solution = Solution()
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    answer = solution.sortPeople(names, heights)
    print(answer)


if __name__ == "__main__":
    main()
