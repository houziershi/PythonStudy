class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if str.strip(s) is '':
            return 0

        i = 0
        for j in range(len(s)):
            if s[j] is " " and j != len(s) - 1:
                i = 0
            else:
                i = i + 1
        return i


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("a "))
