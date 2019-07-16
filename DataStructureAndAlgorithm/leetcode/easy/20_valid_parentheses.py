class Solution:
    def isValid(self, s):
        lefty = '({['
        righty = ')}]'
        stack = []
        for c in s:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if not stack:
                    return False
                if righty.index(c) != lefty.index(stack.pop()):
                    return False
        return not stack


if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
