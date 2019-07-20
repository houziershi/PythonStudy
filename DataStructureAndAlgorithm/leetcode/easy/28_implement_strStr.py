class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        elif len(needle) > len(haystack):
            return -1
        else:
            index = -1
            first = needle[0]
            for i in range(len(haystack)):
                if haystack[i] == first:
                    if i + len(needle) - 1 >= len(haystack):
                        index = -1
                        break
                    elif needle[1:] == haystack[i + 1:i + len(needle)]:
                        index = i
                        break

            return index


if __name__ == '__main__':
    print(Solution().strStr('aaa', 'a'))

    """
        Time Complexity = O(M*N)
        Space Complexity = O(1)
        Implement strStr().
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        Example:
        Input: haystack = "hello", needle = "ll"
        Output: 2
    """
