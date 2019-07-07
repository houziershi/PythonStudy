class Solution:

    def twoSum(self, nums, target):
        for i in nums:
            subTarget = target - i
            start = nums.index(i)
            next = start + 1
            subNum = nums[next:]
            if subTarget in subNum:
                return [nums.index(i), next + subNum.index(subTarget)]


if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))
