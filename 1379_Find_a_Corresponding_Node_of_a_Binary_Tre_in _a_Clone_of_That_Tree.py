"""
1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree from Leetcode.          # noqa

Given two binary trees original and cloned and given a reference
to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the
target node and the answer must be a reference to a node in the cloned tree.
"""


# Definition for a binary tree node
class TreeNode:
    """TreeNode."""

    def __init__(self, x):
        """TreeNode."""
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        """Print value."""
        return "Node (" + str(self.val) + ")"


class Solution:
    """Find a Corresponding Node of a Binary Tree in a Clone of That Tree Class."""         # noqa

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:         # noqa
        """Find a Corresponding Node of a Binary Tree in a Clone of That Tree Function."""       # noqa
        if original is None:
            return None
        if original != target and original is not None:
            return self.getTargetCopy(original.right, cloned.right, target) or self.getTargetCopy(original.left, cloned.left, target)
        return cloned

        # queue = []
        # def rec(nodes, target, queue):
        #     """Find the node in the hayqueue :D."""
        #     if nodes is not None:
        #         rec(nodes.left, target, queue)
        #         rec(nodes.right, target, queue)
        #         if nodes.val == target.val:
        #             queue.append(nodes)

        #     return queue
        # return rec(cloned, target, queue).pop()


def main():
    """Solution."""
    s = Solution()
    node1 = TreeNode(7)
    node2 = TreeNode(4)
    node3 = TreeNode(3)
    node4 = TreeNode(6)
    node5 = TreeNode(19)
    node1.left = node3
    node1.right = node2
    node3.left = node4
    node3.right = node5
    # nodes_list = [7, 4, 3, None, None, 6, 19]
    answer = s.getTargetCopy(node1, node1, node5)
    print(answer)


if __name__ == "__main__":
    main()
