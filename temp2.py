class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        left, right = 0, 0
        found = False
        for left in range(len(nums) - 1): 
            found, right = self.found_right(nums, left, target - nums[left])
            if found:
                return [left + 1, right + 1]
        return

    def found_right(self, nums, left, target):
        start, end = left + 1, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return True, start
        if nums[end] == target:
            return True, end        

        return False, 0

s = Solution()
print(s.twoSum([-111,-100,-98,-11,-6,-5,-4,-3,-2,-1],-111))
