class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            t = target- nums[i]
            if t in nums and nums.index(t)!=i:
                ans = [nums.index(t),i]
                ans.sort()
                return ans
