from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        even = head.next
        e = even
        odd = head
        o = odd

        while odd.next is not None or even.next is not None:
            nxt_o = odd.next
            nxt_e = even.next

            if nxt_o.next is not None:
                odd.next = odd.next.next
            else:
                odd.next = None
                break

            if nxt_e.next is not None:
                even.next = even.next.next
            else:
                even.next = None
                break

            odd = odd.next
            even = even.next

        if odd.next is not None:
            odd = odd.next
        odd.next = e

        return o


def main():
    """328. Odd Even Linked List."""
    sol = Solution()

    # 1st example
    n1 = ListNode(2)
    n2 = ListNode(1)
    n3 = ListNode(3)
    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)
    n7 = ListNode(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    exp = [2,3,6,7,1,5,4]
    out = sol.oddEvenList(n1)
    out_num = []

    while out:
        out_num.append(out.val)
        out = out.next
    print("out", out_num)

    if out_num == exp:
        print("TRUE")
    else:
        print("False")
    print()

    # sec example
    n10 = ListNode(1)
    n11 = ListNode(2)
    n12 = ListNode(3)
    n13 = ListNode(4)
    n14 = ListNode(5)
    n10.next = n11
    n11.next = n12
    n12.next = n13
    n13.next = n14

    exp2 = [1,3,5,2,4]
    out = sol.oddEvenList(n10)
    out_num2 = []

    while out:
        out_num2.append(out.val)
        out = out.next
    print("out", out_num2)

    if out_num2 == exp2:
        print("TRUE")
    else:
        print("False")
    print()

    l0 = ListNode(2)
    l1 = ListNode(1)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l4 = ListNode(6)
    l5 = ListNode(5)
    l6 = ListNode(7)
    l7 = ListNode(8)
    l0.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7

    exp3 = [2,4,6,7,1,3,5,8]
    out3 = sol.oddEvenList(l0)
    o3 = []

    while out3:
        o3.append(out3.val)
        out3 = out3.next
    print("out", o3)

    if o3 == exp3:
        print("TRUE")
    else:
        print("False")


if __name__ == '__main__':
    main()
