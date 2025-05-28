class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        missing=0
        for i in range(n+1):
            if i not in nums:
                missing=i
        return missing