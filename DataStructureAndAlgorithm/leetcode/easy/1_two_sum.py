class Solution:

    def twoSum(self, nums, target):
        for i in nums:
            subTarget = target - i
            start = nums.index(i)
            next = start + 1
            subNum = nums[next:]
            if subTarget in subNum:
                return [nums.index(i), next + subNum.index(subTarget)]

    def twoSum2(self, nums, target):
        index = {}
        for i in range(len(nums)):
            sub_target = target - nums[i]
            if sub_target in index:
                return [i, index[sub_target]]
            else:
                index[nums[i]] = i


if __name__ == '__main__':
    print(Solution().twoSum2((2, 7, 11, 15), 26))

    """
        Time Complexity = O(N^2)
        Space Complexity = O(1)
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
    """
