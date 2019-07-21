class Solution:
    def searchInsert(self, nums, target) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        # return self.binarySearch2(nums, 0, len(nums) - 1, target)

        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
            else:
                return middle

        return low

    def binarySearch(self, nums, low, high, target):
        if low > high:
            return low
        else:
            middle = (low + high) // 2
            if target > nums[middle]:
                return self.binarySearch(nums, middle + 1, high, target)
            elif target < nums[middle]:
                return self.binarySearch(nums, low, middle - 1, target)
            else:
                return middle

    def binarySearch2(self, nums, low, high, target):
        while low <= high:
            middle = (low + high) // 2
            if target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle - 1
            else:
                return middle

        return low


if __name__ == '__main__':
    print(Solution().searchInsert([1, 3], 2))

    """
        Time Complexity = O(log(x))
        Space Complexity = O(1)
        Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        You may assume no duplicates in the array.
        Example:
        Input: [1,3,5,6], 5
        Output: 2
        
        Input: [1,3,5,6], 2
        Output: 1
    """
