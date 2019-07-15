class Solution:
    def romanToInt(self, s):
        romanDic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = romanDic[s[0]]
        for i in range(1, len(s)):
            if romanDic[s[i]] > romanDic[s[i - 1]]:
                result = result + romanDic[s[i]] - 2 * romanDic[s[i - 1]]
            else:
                result += romanDic[s[i]]

        return result


if __name__ == '__main__':
    print(Solution().romanToInt('IV'))
