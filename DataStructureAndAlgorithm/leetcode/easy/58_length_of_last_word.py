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
