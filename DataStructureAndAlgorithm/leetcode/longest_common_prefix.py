from functools import reduce


class Solution(object):
    @staticmethod
    def lcp(self, str1, str2):
        i = 0
        while i < len(str1 and i < len(str2)):
            if str1[i] == str2[i]:
                i = i + 1
            else:
                break
        return str1[:i]

    # @return a string
    def longest_common_prefix(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp, strs)

if __name__ == '__main__':
    s = Solution()
    str = ['hgk', 'hgkuu', 'hgj']
    print(s.longest_common_prefix(str))
