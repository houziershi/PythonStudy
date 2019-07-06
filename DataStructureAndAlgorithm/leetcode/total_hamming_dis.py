import traceback


class Solution(object):
    @staticmethod
    def total_hamming_distance(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        traceback.print_stack()
        ans = 0
        mask = 1
        for j in range(0, 32):
            ones = zeros = 0
            for num in nums:
                if num & mask:
                    ones += 1
                else:
                    zeros += 1
            ans += ones * zeros
            mask = mask << 1
        return ans


if __name__ == '__main__':
    n = [4, 14, 2]
    s = Solution()
    print(s.total_hamming_distance(n))
