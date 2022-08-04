"""
1656. Design an Ordered Stream from Leetcode.

There is a stream of n (idKey, value) pairs arriving in an
arbitrary order, where idKey is an integer between 1 and n
and value is a string. No two pairs have the same id.

Design a stream that returns the values in increasing order of
their IDs by returning a chunk (list) of values after each insertion.
The concatenation of all the chunks should result
in a list of the sorted values.

Implement the OrderedStream class:

OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int idKey, String value) Inserts the pair (idKey, value)
into the stream, then returns the largest possible chunk of currently
inserted values that appear next in the order.
"""
from typing import List


class OrderedStream:
    """Design an Ordered Stream."""

    def __init__(self, n: int):
        """Init."""
        self.arr = [None] * n
        self.ptr = 0

    def __str__(self) -> str:
        """Print value."""
        print(str(self.arr))

    def insert(self, idKey: int, value: str) -> List[str]:
        """Design an Ordered Stream."""
        idKey -= 1
        self.arr[idKey] = value

        if idKey > self.ptr:
            return []

        while self.ptr < len(self.arr) and self.arr[self.ptr]:
            self.ptr += 1

        return self.arr[idKey:self.ptr]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


def main():
    """Solution."""
    os = OrderedStream(5)
    answer = os.insert(3, "ccccc")   # Inserts (3, "ccccc"), returns [].
    print(answer)
    answer = os.insert(1, "aaaaa")   # Inserts (1, "aaaaa"), returns ["aaaaa"].
    print(answer)
    answer = os.insert(2, "bbbbb")   # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    print(answer)
    answer = os.insert(5, "eeeee")   # Inserts (5, "eeeee"), returns [].
    print(answer)
    answer = os.insert(4, "ddddd")   # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
    print(answer)
    # Concatentating all the chunks returned:
    # [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
    # print(answer)


if __name__ == "__main__":
    main()
