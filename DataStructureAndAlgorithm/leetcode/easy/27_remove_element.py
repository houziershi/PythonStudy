class Solution:
    def removeElement(self, nums, val) -> int:
        head = 0
        tail = len(nums) - 1

        while head <= tail:
            if nums[head] == val and nums[tail] != val:
                nums[head], nums[tail] = nums[tail], nums[head]
                head += 1
                tail -= 1
            elif nums[head] == val and nums[tail] == val:
                tail -= 1
            elif nums[tail] != val and nums[tail] != val:
                head += 1
            else:
                tail -= 1

        return head


if __name__ == '__main__':
    print(Solution().removeElement([2], 3))
