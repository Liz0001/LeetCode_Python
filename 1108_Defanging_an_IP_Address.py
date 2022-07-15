"""
1108. Defanging an IP Address from Leetcode.

Given a valid (IPv4) IP address,
return a defanged version of that IP address.

A defanged IP address replaces every
period "." with "[.]".
"""


class Solution:
    """Defanging an IP Address Class."""

    def defangIPaddr(self, address) -> str:
        """Defanging an IP Address Function."""
        return address.replace(".", "[.]")


def main():
    """Solution."""
    s = Solution()
    ip4 = "1.1.1.1"
    answer = s.defangIPaddr(ip4)
    print(answer)


if __name__ == "__main__":
    main()
