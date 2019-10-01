class Solution:
    def plusOne(self, digits):
        s = digits[len(digits) - 1] + 1
        if s < 10:
            digits[len(digits) - 1] = s
            return digits
        else:
            carry = 1
            digits[len(digits) - 1] = s - 10
            for num in range(len(digits) - 2, -1, -1):
                temp = digits[num] + carry
                if temp > 9:
                    digits[num] = s - 10
                    carry = 1
                else:
                    digits[num] = temp
                    carry = 0
                    break
            if carry == 1:
                digits.insert(0, carry)

            return digits


if __name__ == '__main__':
    digit = [9]
    rs = Solution().plusOne(digit)
    print('')
