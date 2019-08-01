class Solution:
    def maxSubArray(self, nums):
        return self.maxSubArray2(nums, 0, len(nums) - 1)[2]

    def maxSubArray2(self, nums, p, r):
        if p == r:
            return p, r, nums[p]
        else:
            q = (r + p) // 2
            left_start, left_right, left_sum = self.maxSubArray2(nums, p, q)
            right_start, right_end, right_sum = self.maxSubArray2(nums, q + 1, r)
            middle_start, middle_end, middle_sum = self.maxCrossSubArray(nums, p, q, r)
        if left_sum >= right_sum and left_sum >= middle_sum:
            return left_start, left_right, left_sum
        elif right_sum >= left_sum and right_sum >= middle_sum:
            return right_start, right_end, right_sum
        else:
            return middle_start, middle_end, middle_sum

    def maxCrossSubArray(self, a, start, mid, end):
        left_sum = -1
        sum = 0
        cross_left = mid
        for i in range(mid, start - 1, -1):
            sum += a[i]
            if sum > left_sum:
                left_sum = sum
                cross_left = i

        right_sum = -1
        sum = 0
        cross_right = mid
        for i in range(mid + 1, end + 1):
            sum += a[i]
            if sum > right_sum:
                right_sum = sum
                cross_right = i
        return cross_left, cross_right, left_sum + right_sum


if __name__ == '__main__':
    x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(x))
