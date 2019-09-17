class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastIndex = 0
        j = 0
        for i in range(len(s)):
            if s[i] is " ":
                if j != 0:
                    lastIndex = j
                j = 0
                continue
            else:
                j = j + 1
        if j == 0 and lastIndex != 0:
            return lastIndex
        else:
            return j


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("  "))

    """
        Time Complexity = O(N^2)
        Space Complexity = O(1)
        Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
        If the last word does not exist, return 0.
        Note: A word is defined as a character sequence consists of non-space characters only.
        Example:
        Input: "Hello World"
        Output: 5
    """
