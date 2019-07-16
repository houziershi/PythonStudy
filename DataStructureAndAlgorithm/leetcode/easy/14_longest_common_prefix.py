class Solution:
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ''
        else:
            x = strs[0]
            result = ''

            for i in range(len(x)):
                if not all(i < len(y) and x[i] == y[i] for y in strs[1:]):
                    break
                else:
                    result += x[i]
            return result


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "fliwht"]))
