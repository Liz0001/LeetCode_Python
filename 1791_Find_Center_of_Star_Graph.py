"""
1791. Find Center of Star Graph from Leetcode.

There is an undirected star graph consisting of
n nodes labeled from 1 to n. A star graph is a
graph where there is one center node and exactly
n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each
edges[i] = [ui, vi] indicates that there is an edge
between the nodes ui and vi. Return the center of the given star graph.
"""
from typing import List


class Solution:
    """Find Center of Star Graph Class."""

    def findCenter(self, edges: List[List[int]]) -> int:
        """Find Center of Star Graph."""
        sublists = len(edges)
        c = 0
        for i in edges:
            if edges[0][0] in i:
                c += 1
        if c == sublists:
            return edges[0][0]
        else:
            return edges[0][1]


def main():
    """Solution."""
    s = Solution()
    edges = [[1, 2], [2, 3], [4, 2]]
    answer = s.findCenter(edges)
    print(answer)


if __name__ == "__main__":
    main()
