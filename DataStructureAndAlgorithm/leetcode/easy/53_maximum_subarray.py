class Solution:
    def maxSubArray(self, nums):
        self.maxSubArray2(nums, 0, len(nums) - 1)

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

    def maxCrossSubArray(self, nums, low, mid, high):
        i = mid
        j = i

        sum_sub_right = nums[i]
        large_right = nums[i]

        for k in range(mid + 1, high + 1):
            if sum_sub_right + nums[k] > large_right:
                j = k
                large_right = sum_sub_right + nums[k]
            sum_sub_right = sum_sub_right + nums[k]

        large_left = nums[i]
        sum_sub_left = nums[i]
        for k in range(mid - 1, low - 1, -1):
            if sum_sub_left + nums[k] > large_left:
                i = k
                large_left = sum_sub_left + nums[k]
            sum_sub_left = sum_sub_left + nums[k]
        print(sum_sub_left + sum_sub_right - nums[mid], i, j)
        return i, j, sum_sub_left + sum_sub_right - nums[mid]


if __name__ == '__main__':
    x = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray2(x, 0, len(x) - 1))
