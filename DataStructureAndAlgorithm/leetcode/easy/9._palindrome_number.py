class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = x
        y = 0
        while num != 0:
            a = num % 10
            num = num // 10
            y = y * 10 + a

        if x == y:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPalindrome(0))

    """
        Time Complexity = O(log(x))
        Space Complexity = O(1)
        Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
        Example:
        Input: 121
        Output: true
    """
