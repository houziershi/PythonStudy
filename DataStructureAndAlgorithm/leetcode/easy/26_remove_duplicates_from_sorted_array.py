class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        index = 1
        prev_char = nums[0]

        for current in nums[1:]:
            if prev_char != current:
                nums[index] = current
                index += 1
                prev_char = current
        return index


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 2]))
