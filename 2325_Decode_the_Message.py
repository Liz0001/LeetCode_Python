"""
2325. Decode the Message from Leetcode.

You are given the strings key and message, which represent a cipher
key and a secret message, respectively. The steps to decode message
are as follows:

Use the first appearance of all 26 lowercase English letters in
key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least
one instance of each letter in the alphabet), we have the partial
substitution table of
('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.
"""


class Solution:
    """Decode the Message Class."""

    def decodeMessage(self, key: str, message: str) -> str:
        """Decode the Message."""
        alp = "abcdefghijklmnopqrstuvwxyz"
        jibber = ""
        used = []
        message2 = ""
        key = key.replace(" ", "")
        for i in key:
            if i not in used:
                jibber += i
                used.append(i)
        for i in range(0, len(message)):
            if message[i] == " ":
                message2 += " "
            else:
                v = message[i]
                ind = jibber.find(v)
                message2 += alp[ind]
        return message2


def main():
    """Solution."""
    s = Solution()
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    answer = s.decodeMessage(key, message)
    print(answer)


if __name__ == "__main__":
    main()
