class Solution:
    """
    -2147483648  2147483647 1534236469
    """

    def reverse(self, x):
        if x < -2147483648 or x > 2147483647:
            return 0

        num = abs(x)
        size = len(str(num))
        y = 0
        for i in range(size):
            a = num % 10
            num = num // 10
            y = y * 10 + a

        if y < -2147483648 or y > 2147483647:
            return 0

        if x < 0:
            return -y
        else:
            return y

    def reverse2(self, x):
        if x < -2147483648 or x > 2147483647:
            return 0
        num = abs(x)
        y = 0
        while num != 0:
            a = num % 10
            num = num // 10
            y = y * 10 + a

        if y < -2147483648 or y > 2147483647:
            return 0

        if x < 0:
            return -y
        else:
            return y


if __name__ == '__main__':
    print(Solution().reverse2(-153))
